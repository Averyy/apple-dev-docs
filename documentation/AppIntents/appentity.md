# AppEntity

**Framework**: App Intents  
**Kind**: protocol

An interface for exposing a custom type or app-specific concept to system experiences like Siri and the Shortcuts app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
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

#### Overview

To use a data model object to app intents, update it to conform to the `AppEntity` protocol. Declare two static properties to make them visible to the system. The following example shows a data model for soup:

For example:

```swift
struct Soup: AppEntity {
   let id: String

   @Property(title: "Type of soup")
   let type: SoupType = .miso
}
```

For additional types, see [`EntityProperty`](entityproperty.md).

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