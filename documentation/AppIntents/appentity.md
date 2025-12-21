# AppEntity

**Framework**: App Intents  
**Kind**: protocol

An interface for exposing a custom type or app-specific concept to system experiences like Siri and the Shortcuts app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
protocol AppEntity : AppValue, DisplayRepresentable, Identifiable where Self == Self.ValueType, Self.ID : EntityIdentifierConvertible, Self.ID : Sendable
```

## Mentions

- [Integrating actions with Siri and Apple Intelligence](integrating-actions-with-siri-and-apple-intelligence.md)
- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)
- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)
- [Making app entities available in Spotlight](making-app-entities-available-in-spotlight.md)

#### Overview

To use a data model object to app intents, update it to conform to the `AppEntity` protocol. Declare properties using the `@Property` property wrapper to make them visible to the system. The following example from the [`Accelerating app interactions with App Intents`](acceleratingappinteractionswithappintents.md) sample app shows a data model for a trail:

```swift
struct TrailEntity: AppEntity {
    // Provide the system with the interface required to query `TrailEntity` structures.
    static let defaultQuery = TrailEntityQuery()

    // The system requires the `AppEntity` identifier to be unique and persistant because the system may save it in a shortcut.
    var id: Trail.ID

    @Property var name: String

    @Property(title: "Region")
    var regionDescription: String

    @Property var trailLength: Measurement<UnitLength>

    var imageName: String

    var currentConditions: String

    /**
    Information on how to display the entity to people — for example, a string like the trail name. Include the optional subtitle
    and image for a visually rich display.
    */
    var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation(title: "\(name)",
                              subtitle: "\(regionDescription)",
                              image: DisplayRepresentation.Image(named: imageName))
    }

    init(trail: Trail) {
        self.id = trail.id
        self.imageName = trail.featuredImage
        self.currentConditions = trail.currentConditions
        self.name = trail.name
        self.regionDescription = trail.regionDescription
        self.trailLength = trail.trailLength
    }
}

extension TrailEntity: URLRepresentableEntity {
    static var urlRepresentation: URLRepresentation {
        // Use string interpolation to fill values from your entity necessary for constructing the universal link URL.
        // This example URL uses the unique and persistant identifier for the `TrailEntity` in the URL.
        "https://example.com/trail/\(.id)/details"
    }
}
```

For additional property types, see [`EntityProperty`](entityproperty.md).

It is up to you whether you want to conform to the `AppEntity` protocol directly on the data models of your app, or if you create data models specific to your app intents implementation. In many cases, it’s a good idea to create models specific to app intents that shadow your app data models to keep entities separate from the rest of your app’s logic.

## Topics

### Specifying properties
- [AppEntity.Property](appentity/property.md)
### Making the entity queryable
- [static var defaultQuery: Self.DefaultQuery](appentity/defaultquery-4khg7.md)
  The default query to use to retrieve entity property instances.
- [associatedtype DefaultQuery : EntityQuery](appentity/defaultquery-swift.associatedtype.md)
- [static var defaultResolverSpecification: EmptyResolverSpecification<Self>](appentity/defaultresolverspecification-2dpf2.md)
- [static var defaultResolverSpecification: some ResolverSpecification](appentity/defaultresolverspecification-589eq.md)
### Default Implementations
- [Identifiable Implementations](appentity/identifiable-implementations.md)

## Relationships

### Inherits From
- [AppValue](appvalue.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [DisplayRepresentable](displayrepresentable.md)
- [Identifiable](../Swift/Identifiable.md)
- [InstanceDisplayRepresentable](instancedisplayrepresentable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)
### Inherited By
- [AssistantEntity](assistantentity.md)
- [AssistantSchemaEntity](assistantschemaentity.md)
- [FileEntity](fileentity.md)
- [IndexedEntity](indexedentity.md)
- [TransientAppEntity](transientappentity.md)
- [URLRepresentableEntity](urlrepresentableentity.md)
- [UniqueAppEntity](uniqueappentity.md)

## See Also

- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)
  Provide the system with information about the types your app uses to model its data so that your intents can use those types as parameters.
- [protocol FileEntity](fileentity.md)
  An entity that refers to a document or other file.
- [protocol IndexedEntity](indexedentity.md)
  `IndexedEntity` represents an App Entity decorated with an attribute set. A set of attributes that enable the system to perform structured indexing  and queries of entities.
- [protocol TransientAppEntity](transientappentity.md)
  A type that represents a transient model object which exposes its interface to App Intents via properties. Note that `TransientAppEntity` types are not meant to be queried.
- [protocol UniqueAppEntity](uniqueappentity.md)
  An entity that will only ever have one value, such as global settings.
- [protocol URLRepresentableEntity](urlrepresentableentity.md)
  An app entity with a URL representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentity)*