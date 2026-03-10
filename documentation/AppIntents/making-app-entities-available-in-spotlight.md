# Making app entities available in Spotlight

**Framework**: App Intents

Annotate your app entity types to support Spotlight indexing, and donate entities to make them findable in searches.

#### Overview

Spotlight provides systemwide search capabilities and integrates with Apple Intelligence, Siri, and other system technologies. To make your app’s content findable by Spotlight, you need to add information about your content to the Spotlight indexes. If your app defines [`AppEntity`](appentity.md) types, index them so that Spotlight can use them to open your app and display that content.

During the indexing process, you provide Spotlight with information about your app’s content. The standard indexing process entails building a [`CSSearchableItemAttributeSet`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet) for each type. However, the App Intents framework offers a more declarative approach for specifying that information. This approach requires less code because it leverages existing code you use to create your entities.

##### Add Support for Indexing Your Entity Types

To index your app’s entities, each [`AppEntity`](appentity.md) type you define needs to conform to the [`IndexedEntity`](indexedentity.md) protocol. The following example shows the `LandmarkEntity` type from [`Adopting App Intents to support system experiences`](adopting-app-intents-to-support-system-experiences.md), which includes this protocol in its declaration:

```swift
struct LandmarkEntity: IndexedEntity {

    // ...

}
```

The [`IndexedEntity`](indexedentity.md) protocol provides default implementations of its properties, so you don’t need to add any code by default. However, you can override the implementations of those properties to customize the information you pass to Spotlight during indexing.

##### Specify Which Properties of Your Entity to Index

Conformance to the [`IndexedEntity`](indexedentity.md) protocol unlocks support for indexing entities, but you need to take additional steps to specify what content to index. When you create an entity, you add certain properties to your type and annotate other properties with macros the App Intents framework requires. Spotlight uses this same information when indexing your type. For example, Spotlight automatically indexes the contents of your entity’s [`displayRepresentation`](instancedisplayrepresentable/displayrepresentation.md) property, including the title, subtitle, and image values you provide.

If you adorn properties with the [`AppEntity.Property`](appentity/property.md) or [`ComputedProperty(indexingKey:)`](computedproperty(indexingkey:).md) property wrappers, you can use those same wrappers to tell Spotlight what content to index. When you include an indexing key with those property wrappers, Spotlight automatically adds the data in that property to your app’s index. Specify an indexing key using Swift key paths and one of the property names in the [`CSSearchableItemAttributeSet`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet) type. To create this path, specify a slash and period (`\.`) followed by the property name. You can also use this approach to specify key paths for your app’s custom indexing keys.

The following code from the [`Accelerating app interactions with App Intents`](acceleratingappinteractionswithappintents.md) sample shows the `LandmarkEntity` type, which makes the app’s landmark data available to the system. The property wrapper for `description` tells Spotlight to index the property using the Spotlight-provided [`contentDescription`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet/contentDescription) key. The property wrapper for `continent` tells Spotlight to index the property using the provided custom key.

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


    // ...
}
```

If your entity doesn’t have a declared property for data you want to index, specify that data in your entity’s [`attributeSet`](indexedentity/attributeset.md) property. The [`IndexedEntity`](indexedentity.md) protocol provides the default implementation of this property, but you can implement it yourself and return a custom [`CSSearchableItemAttributeSet`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet) with additional data to index. The following example shows how you might use this property to return additional information related to a landmark that the entity doesn’t expose directly:

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

> **Note**: Core Spotlight combines the keys from your entity’s wrapped properties with the contents of its [`displayRepresentation`](instancedisplayrepresentable/displayrepresentation.md) and [`attributeSet`](indexedentity/attributeset.md) properties to create the complete set of indexable keys. If you use the same indexing key in multiple places, Spotlight prefers values from wrapped properties over others. It also prefers data from the [`displayRepresentation`](instancedisplayrepresentable/displayrepresentation.md) property over data from the [`attributeSet`](indexedentity/attributeset.md) property.

##### Add Your Entities to a Spotlight Index

When your app runs, you must deliver instances of your [`AppEntity`](appentity.md) types to Spotlight so it can index them. If your app doesn’t yet support Spotlight, index your entities directly by calling the [`indexAppEntities(_:priority:)`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableIndex/indexAppEntities(_:priority:)) method of a named [`CSSearchableIndex`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableIndex) object. This method passes the entities to Spotlight, which processes them and adds them to your app’s index. The following example donates entities containing landmark data to an app-specific index:

```swift
static func donateLandmarks(modelData: ModelData) async throws {
    let landmarkEntities = await modelData.landmarkEntities
    try await CSSearchableIndex(name: "AppIntentsTravelTracking_Landmarks").indexAppEntities(landmarkEntities)
}
```

> **Note**: When indexing your app’s content, use a named [`CSSearchableIndex`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableIndex) type, not the default index. Use the default index only for prototyping and testing your code during development.

If your app already indexes its content using [`CSSearchableItem`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItem) objects, associate your entities with those items before passing them to the indexer. For information on how to do that, see [`Integrate entities into your existing Spotlight code`](making-app-entities-available-in-spotlight#Integrate-entities-into-your-existing-Spotlight-code.md). For additional information about the Spotlight indexing process, see [`Adding your app’s content to Spotlight indexes`](https://developer.apple.com/documentation/CoreSpotlight/adding-your-app-s-content-to-spotlight-indexes).

##### Integrate Entities Into Your Existing Spotlight Code

If you already index your app’s content using [`CSSearchableItem`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItem) objects, attach matching entities to those items to improve the search experience. When you attach an entity to one of your searchable items, Spotlight can use that entity to display the search result in your app, if you also have an open intent for the entity. The following steps explain the process for how to associate an entity with a searchable item:

1. Populate the [`CSSearchableItemAttributeSet`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet) of your searchable item with the data you want Spotlight to index.
2. Create or locate the matching app entity for the item.
3. Call the [`associateAppEntity(_:priority:)`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet/associateAppEntity(_:priority:)) method to add the entity to the attribute set.
4. Create the [`CSSearchableItem`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItem) using the attribute set.
5. Index the item with the rest of your content.

The following example creates an array of searchable items for an app that manages hiking trails. For each trail, the code creates an app entity for the trail and associates it with the trail’s search attributes. When calling the [`associateAppEntity(_:priority:)`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet/associateAppEntity(_:priority:)) method, the code also specifies a priority value to indicate the importance of that trail to the person. Spotlight elevates items with higher priority values in suggestions and search results to make them more visible.

```swift
let searchableItems = trails.map { trail in
    let attributes = trail.searchableAttributes
            
    let isFavorite = favoritesCollection.members.contains(trail.id)
    let weight = isFavorite ? 10 : 1
    let entity = TrailEntity(trail: trail)
    attributes.associateAppEntity(entity, priority: weight)

    let item = CSSearchableItem(uniqueIdentifier: String(trail.id),
                                        domainIdentifier: nil,
                                        attributeSet: attributes)
                        
    return item
}
```

After running the preceding code, create a named [`CSSearchableIndex`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableIndex) object and use it to index the items. For information about how to index content using the Core Spotlight APIs, see [`Adding your app’s content to Spotlight indexes`](https://developer.apple.com/documentation/CoreSpotlight/adding-your-app-s-content-to-spotlight-indexes).

##### Provide an Intent to Open Your App From Search Results

For each [`AppEntity`](appentity.md) type that you define and donate to Spotlight, create an [`OpenIntent`](openintent.md) type that opens that entity in your app. When Spotlight returns one of your app’s entities in a search result, you want people to be able to tap that result and navigate to the associated content in your app. When an open intent is present, Spotlight can use it to provide that behavior. The following example from [`Adopting App Intents to support system experiences`](adopting-app-intents-to-support-system-experiences.md) shows the open intent for the app’s `LandmarkEntity` type. When someone taps a landmark in search results, Spotlight uses the intent to open the app and display the chosen landmark.

```swift
struct OpenLandmarkIntent: OpenIntent {
    static let title: LocalizedStringResource = "Open Landmark"

    @Parameter(title: "Landmark", requestValueDialog: "Which landmark?")
    var target: LandmarkEntity
}
```

## See Also

- [Adopting App Intents to support system experiences](adopting-app-intents-to-support-system-experiences.md)
  Create app intents and entities to incorporate system experiences such as Spotlight, visual intelligence, and Shortcuts.
- [Launching your voice-based conversational app from the side button of iPhone](launching-your-voice-based-conversational-app-from-the-side-button-of-iphone.md)
  Let people in Japan configure the side button of iPhone to launch your voice-based conversational app.
- [Siri](siri.md)
  Let people complete tasks with voice commands, search, and other system experiences by integrating your app with Siri and Apple Intelligence.
- [Visual intelligence](visual-intelligence.md)
  Integrate your app with visual intelligence and include your content in its search results.
- [App Shortcuts](app-shortcuts.md)
  Integrate your app’s intents and entities with the Shortcuts app, Siri, Spotlight, and the Action button on supported iPhone and Apple Watch models.
- [Widgets, Live Activities, and controls](widgets-and-live-activities.md)
  Use app intents make your widgets and Live Activities interactive, offer controls, and suggest widgets in Smart Stacks.
- [Action button on iPhone and Apple Watch](actionbutton.md)
  Enable people to run your App Shortcuts with the Action button on iPhone or to start your app’s workout or dive sessions using the Action button on Apple Watch.
- [Focus](focus.md)
  Adjust your app’s behavior and filter incoming notifications when the current Focus changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/making-app-entities-available-in-spotlight)*