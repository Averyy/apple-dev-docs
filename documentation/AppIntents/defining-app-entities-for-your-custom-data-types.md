# Defining app entities for your custom data types

**Framework**: App Intents

Provide the system with information about the types your app uses to model its data so that your intents can use those types as parameters.

#### Overview

People create, manage, and view their data primarily using your app’s interface, but sometimes they might want to access that data from outside your app. System features like Siri make it possible for people to perform actions using your app and interact with your app’s data. However, those features interact only with the data you provide using app entities.

An *app entity* is a type that adopts the [`AppEntity`](appentity.md) protocol and reflects a portion of your app’s data. Typically, you define app entity types only for the subset of data people are likely to use outside your app. For example, an email app might define an app entity type for email messages and a separate type for mailboxes. Someone interacting with the app using Siri can instruct it to create emails, read incoming messages, or move them to a particular mailbox.

In your code, include app entities in places where the system can use them. In app intents, include entities as parameters when an action requires your app’s custom data. In your app’s Spotlight indexes, include entities alongside the rest of your data so Spotlight has a way to navigate to that data from search results. Indexing your content also makes your entities discoverable by Apple Intelligence and Siri, which can use the data to process requests involving your content. You can also suggest entities to the system and make your content more visible in relevant system interfaces.

##### Create the Initial Code for Your App Entity Type

When defining your app’s entities, you need to determine whether the underlying data is well-known to the system or specific to your app. The system is already familiar with many types of well-known data, such as photos, mail, books, files, and more. To promote consistency, the App Intents framework defines schemas that specify the properties to include in entities for these types. Supporting a schema makes it easier for Apple Intelligence to reason over your content and provide consistent responses. If your data doesn’t align with a particular schema, you can still define custom app entities that contain any data you want.

To define an app entity type, create a structure that conforms to the [`AppEntity`](appentity.md) or [`IndexedEntity`](indexedentity.md) type and add it to your app. For schema-based entities, precede your type declaration with the `@AppEntity` macro and specify the schema name as a parameter. In your type, add variables for the data your entity manages. The following example creates an entity for a photo album and adds the required properties for that schema. You provide the album type information using an [`AppEnum`](appenum.md) that conforms to the [`albumType`](appschema/photosenum/albumtype.md) schema.

```swift
@AppEntity(schema: .photos.album)
struct PhotoAlbumEntity: AppEntity {

    // Properties from the schema.
    var name: String
    var creationDate: Date?
    var albumType: MyPhotoAlbumType
}
```

> **Note**: To define a custom app entity, create your structure in the same way as above, but omit the `@AppEntity` macro and schema information. Reserve custom entity types for data that doesn’t have a schema-based equivalent.

Although you use entities to reflect your app’s underlying data, you don’t have to reflect all of that data. When you define an entity, you can choose whether to create a standalone structure or add the [`AppEntity`](appentity.md) protocol to one of your app’s existing data types. A standalone structure provides more flexibility to include only a subset of the data that makes sense. It also offers a cleaner separation between your app’s data structures and the rest of the system. The only time it makes sense to integrate the [`AppEntity`](appentity.md) protocol into one of your existing types is when that type is lightweight and you can create new instances of it quickly. For most other types, it’s better to create a separate entity structure and cache existing data values in it.

The [`IndexedEntity`](indexedentity.md) type makes it possible to include your entities in your app’s Spotlight index. Apps use the [`Core Spotlight`](https://developer.apple.com/documentation/CoreSpotlight) framework to build a fast, searchable index of their content. Including entities in your app’s index provides a better experience with system search features. It also makes those entities available to Apple Intelligence. For more information about adding this support, see [`Making app entities available in Spotlight`](making-app-entities-available-in-spotlight.md).

##### Provide a Unique Identifier for Your Type

A requirement for all app entities is that they provide a unique identifier to distinguish one instance from another. Whether you have only one entity or tens of thousands, a unique identifier helps you differentiate entities of the same type. When the system needs a specific entity, it provides you with the identifier and expects you to return the matching entity instance.

The [`AppEntity`](appentity.md) already conforms to the [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable) protocol, so you need to implement the [`id`](https://developer.apple.com/documentation/Swift/Identifiable/id-8t2ws) property from this protocol to define your unique identifier. Set the type of this property to [`UUID`](https://developer.apple.com/documentation/Foundation/UUID), [`String`](https://developer.apple.com/documentation/Swift/String), or [`Int`](https://developer.apple.com/documentation/Swift/Int) type whenever possible. The App Intents framework contains built-in support for identifying entities using these types, so using them is the simplest way to implement your entity. The following example shows an entity that uses a unique identifier for its `id` property.

```swift
@AppEntity(schema: .photos.album)
struct PhotoAlbumEntity: AppEntity {
    let id: UUID

    // Properties from the schema.
    var name: String
    var creationDate: Date?
    var albumType: MyPhotoAlbumType
}
```

The [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable) protocol requires each entity instance to have a unique identifier value, but enforces that uniqueness only on the current device. If your app runs on multiple devices, you need to provide an identifier that’s stable across devices. If you store your data in CloudKit or generate UUIDs from your server, you can use the identifiers from those technologies in your entities. However, if you create a local identiifer for each entity that’s separate from the one you share with other devices, set the type of your `id` property to [`SyncableEntityIdentifier`](syncableentityidentifier.md) instead. You can use this type with the [`SyncableEntity`](syncableentity.md) protocol to tell the system that the identifer for each entity is the same on each of the person’s devices.

##### Add Properties for Your Key Data Variables

An entity type contains app-specific data you want to make available to the system. When declaring your type, add properties to store the relevant information. If your entity types are separate from your app’s data structures, design your type to store a copy of your app’s actual data. When you need to make changes to your app’s data, continue to modify your app-specific data structures and copy your changes to any existing entities.

In each entity type, apply property wrappers to the properties you want to make available to the system. The system doesn’t introspect your entity types automatically. Instead, you use property wrappers to mark the specific properties you want the system to use. Typically, you apply the `@Property` wrapper to your type, but other wrappers are available too. The following example, shows an entity with several wrapped properties that provide the system with the name, description, and length of a trail. The type also contains several unwrapped property with additional information about the trail from the app’s internal data structures..

```swift
struct TrailEntity: AppEntity {
    var id: Trail.ID
    var imageName: String
    var currentConditions: String
    var trailStartLocation : CLLocationCoordinate2D

    // Wrapped properties.
    @Property var name: String
    @Property var trailLength: Measurement<UnitLength>

    @Property(title: "Region")
    var regionDescription: String

    // Type initializer.
    init(trail: Trail) {
        self.id = trail.id
        self.imageName = trail.featuredImage
        self.currentConditions = trail.currentConditions
        self.name = trail.name
        self.regionDescription = trail.regionDescription
        self.trailLength = trail.trailLength
    }
}
```

> ❗ **Important**: If you implemented your entity using a schema, you don’t need to add property wrappers to the required schema properties. The schema automatically implicitly wraps relevant properties.

The App Intents framework supports several different property wrappers, each of which imparts specific behaviors on that property. The following table lists the supported property wrappers and when to use them.

| Macro | Description |
| --- | --- |
| `@Property` | Apply this wrapper to properties with values you can set directly. See the [`EntityProperty`](entityproperty.md) type for a list of initializers. |
| `@ComputedProperty` | Apply this wrapper when you need a getter or setter method to compute the property’s value. |
| `@DeferredProperty` | Apply this wrapper if the property stores a large value you want to load lazily. When archiving your entity, the system doesn’t include this property in the archive. |

Include parameters in a property wrapper when you want to provide a custom title for your property or add other information like a Spotlight indexing key. For some parameters, the system infers default information from the property declaration. For example, if you don’t specify a `title` parameter for the macro, the macro uses the name of the property as the title. For other parameters, the system treats a missing parameter value as a sign you don’t support the feature.

If a property contains an array of entities, use an [`EntityCollection`](entitycollection.md) as the property’s type to improve performance in specific situations. An entity collection stores only the unique identifier of each entity in the collection initially. The collection doesn’t load the rest of the entity unless you specifically request it. If your array includes thousands of entities, this behavior can save measurable time during critical operations such as parameter resolution of an app intent. For more information about how to use entity collections, see [`EntityCollection`](entitycollection.md).

For a list of property wrappers and how to use them, see [`Property declarations`](app-entities#Property-declarations.md).

##### Define Properties Using Only the Supported Types

For every property you add to your app entity, choose only types that the App Intents framework supports. The system needs to know how to handle your chosen types because it customizes interactions based on those types. The following table lists the supported types.

| Category | Types | Notes |
| --- | --- | --- |
| Primitive value types | [`Bool`](https://developer.apple.com/documentation/Swift/Bool), [`Int`](https://developer.apple.com/documentation/Swift/Int), [`Double`](https://developer.apple.com/documentation/Swift/Double), [`String`](https://developer.apple.com/documentation/Swift/String), [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString), [`Duration`](https://developer.apple.com/documentation/Swift/Duration), [`Date`](https://developer.apple.com/documentation/Foundation/Date), [`Decimal`](https://developer.apple.com/documentation/Foundation/Decimal), [`Measurement`](https://developer.apple.com/documentation/Foundation/Measurement), and [`URL`](https://developer.apple.com/documentation/Foundation/URL) | None |
| Collection types | [`Array`](https://developer.apple.com/documentation/Swift/Array), [`Set`](https://developer.apple.com/documentation/Swift/Set) | Make sure the collection’s elements are of a type that’s compatible with [`IntentParameter`](intentparameter.md). |
| App Intents framework types | [`EntityCollection`](entitycollection.md), [`IntentPerson`](intentperson.md), [`IntentFile`](intentfile.md), [`IntentCurrencyAmount`](intentcurrencyamount.md), [`IntentPaymentMethod`](intentpaymentmethod.md), [`SystemShortcut`](systemshortcut.md), [`UnionValue()`](unionvalue().md) | For additional information, see [`Common data types`](common-data-types.md). |
| Other system types | [`AudioSearch`](https://developer.apple.com/documentation/MediaIntents/AudioSearch), [`DateComponents`](https://developer.apple.com/documentation/Foundation/DateComponents), [`LinkMetadata`](https://developer.apple.com/documentation/LinkPresentation/LinkMetadata), [`PersonNameComponents`](https://developer.apple.com/documentation/Foundation/PersonNameComponents), [`PHAsset`](https://developer.apple.com/documentation/Photos/PHAsset), [`PlaceDescriptor`](https://developer.apple.com/documentation/GeoToolbox/PlaceDescriptor), [`Calendar.RecurrenceRule`](https://developer.apple.com/documentation/Foundation/Calendar/RecurrenceRule), [`SemanticContentDescriptor`](https://developer.apple.com/documentation/VisualIntelligence/SemanticContentDescriptor) | None |
| Custom app data | [`AppEntity`](appentity.md), [`AppEnum`](appenum.md) | Use these types to store app-specific data. |

When you want to store app-specific data in a property, create an [`AppEntity`](appentity.md) or [`AppEnum`](appenum.md) type and use it to specify your data.

##### Create a Query Type to Handle Searches

To help the system find your app’s entities, provide a query type for each entity type you define. The system uses your query type to search your app’s content at relevant times. For example, when an app intent parameter contains an entity, the parameter resolution process uses your query type to find the right entity. The system also runs your queries at other times to locate relevant entities in your app.

Implement your query type as a structure that conforms to the [`EntityQuery`](entityquery.md) protocol. The minimal implementation of this protocol requires you to locate or create an entity using only its unique identifier. Use additional protocols to support text- or property-based searches of your entities. For example, the [`EntityPropertyQuery`](entitypropertyquery.md) protocol adds support for advanced searches using values from one or more properties of your entity type.

> **Note**: If your app adds entities to its Spotlight index, adopt the [`IndexedEntityQuery`](indexedentityquery.md) protocol in your query types in addition to any other protocols. For more information about indexing entities, see [`Making app entities available in Spotlight`](making-app-entities-available-in-spotlight.md).

The following example shows a query type that searches for hiking trails based on their unique identifier. In this case, the unique identifier for each entity matches the unique identifier the app assigns to its internal trail data structures. The [`entities(for:)`](entityquery/entities(for:).md) method uses the app’s internal data manager to find the trails with the requested identifiers. It then uses the trail information to initialize and return one or more new entity instances.

```swift
struct TrailEntityQuery: EntityQuery {
    
    @Dependency
    var trailManager: TrailDataManager

    func entities(for identifiers: [TrailEntity.ID]) async throws -> [TrailEntity] {
        Logger.entityQueryLogging.debug("[TrailEntityQuery] Query for IDs \(identifiers)")
        
        return trailManager.trails(with: identifiers)
                .map { TrailEntity(trail: $0) }
    }
}
```

To associate your query with your entity, implement the [`defaultQuery`](appentity/defaultquery-4khg7.md) property in your entity and initialize it with an instance of your query type. The following example shows an updated version of the `TrailEntity` type that includes an instance of its query type.

```swift
struct TrailEntity: AppEntity {
    var id: Trail.ID
    var imageName: String
    var currentConditions: String
    var trailStartLocation : CLLocationCoordinate2D

    // Wrapped properties.
    @Property var name: String
    @Property var trailLength: Measurement<UnitLength>

    @Property(title: "Region")
    var regionDescription: String

    // Type initializer.
    init(trail: Trail) {
        self.id = trail.id
        self.imageName = trail.featuredImage
        self.currentConditions = trail.currentConditions
        self.name = trail.name
        self.regionDescription = trail.regionDescription
        self.trailLength = trail.trailLength
    }

    // Query type.
    static let defaultQuery = TrailEntityQuery()
}
```

For information about performing additional types of searches, see [`EntityStringQuery`](entitystringquery.md) and [`EntityPropertyQuery`](entitypropertyquery.md).

##### Provide Alternate Representations of Your Content

The system occasionally needs to incorporate your entities into conversations with people or other apps. During a Siri conversation, the system might describe the contents of the entity verbally to someone. During a multi-step operation, Apple Intelligence or Shortcuts might transfer well-known information from your entity to another app to process. For example, if your entity represents a geographical location, the system might send that location to Maps to generate directions. When implementing your entity types, describe your content to the system using specific types:

- **[`DisplayRepresentation`](displayrepresentation.md)**: Provides the displayable version of your entity, and offers a title, subtitle, and image the system can incorporate into dialogs. Assign this type to the [`displayRepresentation`](instancedisplayrepresentable/displayrepresentation.md) property of your entity.
- **[`TypeDisplayRepresentation`](typedisplayrepresentation.md)**: Describes the type of content your entity contains. Assign this type to the [`typeDisplayRepresentation`](typedisplayrepresentable/typedisplayrepresentation.md) property of your entity.
- **[`IntentValueRepresentation`](intentvaluerepresentation.md)**: Bridges the value of your entity to common types like [`IntentPerson`](intentperson.md) or [`PlaceDescriptor`](https://developer.apple.com/documentation/GeoToolbox/PlaceDescriptor). If you can express your entity as one of these types, add support for the [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) protocol and include an [`IntentValueRepresentation`](intentvaluerepresentation.md) as one of the representations.

The following example shows the representations for the `TrailEntity` type, which describes a hiking trail. The display representation incorporates data from the entity into the description, whereas the type representation specifies the type of information in the entity. The transfer representation uses the trail coordinates to create a [`PlaceDescriptor`](https://developer.apple.com/documentation/GeoToolbox/PlaceDescriptor) type, allowing someone to locate the trail on a map.

```swift
extension TrailEntity {
    var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation(title: "\(name)",
                              subtitle: "\(regionDescription)",
                              image: DisplayRepresentation.Image(named: imageName))
    }

    static var typeDisplayRepresentation: TypeDisplayRepresentation {
        TypeDisplayRepresentation(
            name: LocalizedStringResource("Trail", table: "AppIntents"),
            numericFormat: LocalizedStringResource("\(placeholder: .int) trails", table: "AppIntents")
        )
    }

    // This representation makes use of a coordinate value stored in the entity.
    static var transferRepresentation: some TransferRepresentation {
        IntentValueRepresentation(
            exporting: { trail in
                PlaceDescriptor(
                    representations: [.coordinate(trail.trailStartLocation)],
                    commonName: trail.name)
            }
        )
    }
}
```

## See Also

- [Making app entities available in Spotlight](making-app-entities-available-in-spotlight.md)
  Update your app entity types to support Spotlight indexing, and donate entities to make them findable in searches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/defining-app-entities-for-your-custom-data-types)*