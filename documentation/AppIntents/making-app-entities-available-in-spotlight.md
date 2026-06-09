# Making app entities available in Spotlight

**Framework**: App Intents

Update your app entity types to support Spotlight indexing, and donate entities to make them findable in searches.

#### Overview

Spotlight is Apple’s search technology, and when you index your content using the Core Spotlight framework, you gain the ability to perform fast lexical and semantic searches of that content. Apple Intelligence can also apply your app’s indexed content to other system experiences like Siri. You provide the help these system features need by including [`AppEntity`](appentity.md) types with the other data in your app’s index. These types offer a common way for your app and features like Siri to refer to your data, and their structure lets the system make better use of your data.

To include entities in your app’s Spotlight indexes, you need to make a few modifications to your [`AppEntity`](appentity.md) types. These modifications are mostly additive and can actually simplify the process of indexing your app’s content. For example, Spotlight can index properties of your entity directly with only a small change to how you declare those properties. Spotlight also offers ways to index your entities directly, without the need of creating a [`CSSearchableItemAttributeSet`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet) for your content.

##### Add Support for Indexing Your Entity Types

To support Spotlight indexing, your entity types need to conform to the [`IndexedEntity`](indexedentity.md) protocol. Adding this protocol to your entity’s declaration is the only requirement for support. The following example shows the `LandmarkEntity` type from [`Adopting App Intents to support system experiences`](adopting-app-intents-to-support-system-experiences.md), which includes this protocol in its declaration:

```swift
struct LandmarkEntity: IndexedEntity {
    // ...
}
```

The [`IndexedEntity`](indexedentity.md) protocol defines several properties, but provides default implementations for all of them. You can implement some of the properties yourself and use them to provide Spotlight with additional information about your entity.

##### Specify Which Properties of Your Entity to Index

Conformance to the [`IndexedEntity`](indexedentity.md) protocol unlocks support for indexing your app’s entities, but conformance also provides some important automatic behaviors. When you define an entity type, you typically apply property wrappers to specific properties to make them discoverable by the system. Protocols like [`DisplayRepresentable`](displayrepresentable.md) also provide descriptive information about your entity. Spotlight uses the information from these protocols to generate an initial set of attributes for your entity types.

In an app entity type, you apply the `@Property`, `@ComputedProperty`, and `@DeferredProperty` property wrappers to specific properties to make them discoverable by the system. These property wrappers add metadata to your type that features like Siri and Shortcuts can use when displaying your entity in conversations. Variants of these property wrappers accept an `indexingKey` or `customIndexingKey` parameter, which tells Spotlight to include the data from the property in your app’s search index. Use the `indexingKey` variant to associate the property with an existing Spotlight key, and use the `customIndexingKey` to associate it with a key that’s custom to your app.

The following code from the [`Adopting App Intents to support system experiences`](adopting-app-intents-to-support-system-experiences.md) sample shows the `LandmarkEntity` type, which makes the app’s landmark data available to the system. The property wrapper for `description` tells Spotlight to index the property using the Spotlight-provided [`contentDescription`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet/contentDescription) key, while the `continent` property uses an app-defined key. For existing Spotlight keys, specify the key name using a Swift key path by prepending a slash and period (`\.`) to the key name.

```swift
struct LandmarkEntity: IndexedEntity {
    // ...


    // Maps the description variable to the Spotlight indexing key `contentDescription`.
    @ComputedProperty(indexingKey: \.contentDescription)
    var description: String { landmark.description }


    // Maps the continent variable to a custom Spotlight indexing key. 
    @ComputedProperty(
        customIndexingKey: CSCustomAttributeKey(
            keyName: "com_AppIntentsTravelTracking_LandmarkEntity_continent"
        )!
    )
    var continent: String { landmark.continent }
    var landmark: Landmark
    var modelData: ModelData

    // ...
}
```

> **Note**: If you wrap properties with the `@DeferredProperty` wrapper, be aware that Spotlight resolves the property’s value in order to add that value to the index. For properties that are expensive to compute, this can add time to the indexing process.

Wrapped properties contain your entity’s most important data, but they might contain only a subset of the data you want to index for your entity. Provide data for any non-wrapped properties in the [`attributeSet`](indexedentity/attributeset.md) property of your entity type. In your implementation create a [`CSSearchableItemAttributeSet`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet) type and fill it with the extra information you want Spotlight to have. The following example shows how you might extend the `LandmarkEntity` type to include latitude and longitude information from the landmark-specific data structure:

```swift
extension LandmarkEntity {
    var attributeSet: CSSearchableItemAttributeSet {
        let attributes = CSSearchableItemAttributeSet()
                
        attributes.latitude = NSNumber(value: landmark.latitude)
        attributes.longitude = NSNumber(value: landmark.longitude)
        attributes.supportsNavigation = true
        
        return attributes
    }
}
```

> **Note**: If a wrapped property uses the same indexing key as an attribute in your [`attributeSet`](indexedentity/attributeset.md) property, Spotlight prefers the wrapped property’s value. Similarly, Spotlight prefers the title, subtitle, and image data from your entity’s [`displayRepresentation`](instancedisplayrepresentable/displayrepresentation.md) property over the same items in the [`attributeSet`](indexedentity/attributeset.md) property.

##### Add App Entities Directly to Your Spotlight Index

To make your app’s entities available to the system, add them to your app’s Spotlight index. If your app doesn’t currently support Spotlight, index your entities directly by creating a named [`CSSearchableIndex`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableIndex) object and passing them to its [`indexAppEntities(_:priority:)`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableIndex/indexAppEntities(_:priority:)) method, as shown in the following example:

```swift
static func donateLandmarks(modelData: ModelData) async throws {
    // Fetch the entities for the app.
    let landmarkEntities = await modelData.landmarkEntities
    
    // Index the entities using a named index.
    try await CSSearchableIndex(name: "AppIntentsTravelTracking_Landmarks").indexAppEntities(landmarkEntities)
}
```

When you index entities directly, Spotlight uses the entity’s properties to build a set of indexable attributes. It then adds those attributes to the index, as if you created a [`CSSearchableItemAttributeSet`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet) and [`CSSearchableItem`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItem) type for each entity. To differentiate entities from one another in the index, Spotlight uses the entity’s unique identifier, which the [`AppEntity`](appentity.md) protocol requires you to provide. If you call [`indexAppEntities(_:priority:)`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableIndex/indexAppEntities(_:priority:)) with an entity and its identifier is already in the index, Spotlight updates the existing entry instead of creating a new one.

> **Note**: When indexing your app’s content, use a named [`CSSearchableIndex`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableIndex) type and not the default index. Use the default index only for prototyping and testing your code during development.

##### Modify Your Existing Spotlight Code to Include Entities

If you already integrated Core Spotlight support into your app, you might not want to replace your existing code with new code based on entities. Fortunately, Core Spotlight provides a way for you to reuse your current code and add entities to your existing [`CSSearchableItem`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItem) types. The following steps explain the process:

1. Create a [`CSSearchableItemAttributeSet`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet) for one of your app’s data items, and fill it with information.
2. Create or locate an app entity for the item.
3. Call the [`associateAppEntity(_:priority:)`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet/associateAppEntity(_:priority:)) method to add the entity to the attribute set.
4. Create the [`CSSearchableItem`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItem) using the attribute set.
5. Index the item with the rest of your content.

The following example creates an array of searchable items for an app that manages hiking trails. For each trail, the code creates an app entity for the trail and associates it with the trail’s search attributes. When calling the [`associateAppEntity(_:priority:)`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet/associateAppEntity(_:priority:)) method, the code includes a priority value to indicate the importance of that trail to the person. Spotlight elevates items with higher priority values in suggestions and search results to make them more readily available.

```swift
let searchableItems = trails.map { trail in
    let attributes = trail.searchableAttributes
            
    let isFavorite = favoritesCollection.members.contains(trail.id)
    let weight = isFavorite ? 10 : 1
    let intent = TrailEntity(trail: trail)
    attributes.associateAppEntity(intent, priority: weight)

    let item = CSSearchableItem(uniqueIdentifier: String(trail.id),
                                        domainIdentifier: nil,
                                        attributeSet: attributes)
                        
    return item
}
```

For information about how to index content using the Core Spotlight APIs, see [`Adding your app’s content to Spotlight indexes`](https://developer.apple.com/documentation/CoreSpotlight/adding-your-app-s-content-to-spotlight-indexes).

##### Add Support for Reindexing Your App Entities

If an issue arises with your app’s index, Spotlight can ask your app to index its content again — a process known as reindexing. If you donate app entities to a [`CSSearchableIndex`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableIndex) using its [`indexAppEntities(_:priority:)`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableIndex/indexAppEntities(_:priority:)) method, implement the [`IndexedEntityQuery`](indexedentityquery.md) protocol in your entity’s query object to handle reindexing.

The methods of the [`IndexedEntityQuery`](indexedentityquery.md) protocol tell you whether to index a subset of your app entity instances or all of them. Each method also receives a [`CSSearchableIndexDescription`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableIndexDescription) type you can use to determine which of your app’s searchable indexes to update. The following example shows an implementation of this protocol for an app that indexes the app entities for photos. Each method fetches the requested app entities from the app’s data store and passes them back to the [`indexAppEntities(_:priority:)`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableIndex/indexAppEntities(_:priority:)) method.

```swift
struct PhotoQuery: IndexedEntityQuery {
    func reindexEntities(for identifiers: [PhotoEntity.ID], indexDescription: CSSearchableIndexDescription) async throws {
        let photos = try await photoStore.fetch(ids: identifiers)
        try await CSSearchableIndex(name: “MyPhotosApp”).indexAppEntities(photos)
    }

    func reindexAllEntities(indexDescription: CSSearchableIndexDescription) async throws {
        let allPhotos = try await photoStore.fetchAll()
        try await CSSearchableIndex(name: “MyPhotosApp”).indexAppEntities(allPhotos)
    }

   // Other query-related methods.
}
```

If you create [`CSSearchableItem`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItem) types for your content and assign entities to them, continue to reindex your content using the delegate of your searchable index. The [`CSSearchableIndexDelegate`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableIndexDelegate) protocol offers methods for reindexing some or all of your app’s content. Upon receiving a reindexing request, recreate the items and their attributes, add the entity to the attribute set, and add the item back to your index.

For more information about regenerating your app’s search indexes, see [`Regenerating your app’s indexes on demand`](https://developer.apple.com/documentation/CoreSpotlight/regenerating-your-app-s-indexes-on-demand).

##### Provide App Intents to Open Your Entites From Search Results

For each [`AppEntity`](appentity.md) type that you define and donate to Spotlight, create an [`OpenIntent`](openintent.md) type that opens that entity in your app. When Spotlight returns one of your app’s entities in a search result, you want people to be able to tap that result and navigate to the associated content in your app. When an open intent is present, Spotlight can use it to provide that behavior. The following example from [`Adopting App Intents to support system experiences`](adopting-app-intents-to-support-system-experiences.md) shows the open intent for the app’s `LandmarkEntity` type. When someone taps a landmark in search results, Spotlight uses the intent to open the app and display the chosen landmark.

```swift
struct OpenLandmarkIntent: OpenIntent {
    static let title: LocalizedStringResource = "Open Landmark"

    @Parameter(title: "Landmark", requestValueDialog: "Which landmark?")
    var target: LandmarkEntity
}
```

If your app has a dedicated search view, also define an app intent that supports the [`ShowInAppSearchResultsIntent`](showinappsearchresultsintent.md) protocol. When a search query yields more than ten results, Spotlight can use this intent to launch your app and display the results in your custom search interface. For more information about how to implement this type, see [`ShowInAppSearchResultsIntent`](showinappsearchresultsintent.md).

## See Also

- [Defining app entities for your custom data types](defining-app-entities-for-your-custom-data-types.md)
  Provide the system with information about the types your app uses to model its data so that your intents can use those types as parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/making-app-entities-available-in-spotlight)*