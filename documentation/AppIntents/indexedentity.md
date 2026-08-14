# IndexedEntity

**Framework**: App Intents  
**Kind**: protocol

An interface that allows you to include an entity in your app’s Spotlight index.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol IndexedEntity : AppEntity
```

## Mentions

- [Making app entities available in Spotlight](making-app-entities-available-in-spotlight.md)
- [Defining app entities for your custom data types](defining-app-entities-for-your-custom-data-types.md)

#### Overview

Adopt this protocol in app entities you want to include in your app’s Spotlight index. Adding entities to Spotlight makes them discoverable by Apple Intelligence, and also serves as the first step in letting Spotlight launch your app and display items that appear in search results. Use the properties of this protocol to configure additional Spotlight metadata to accompany your app entity in the index.

For more information about adding entities to your app’s Spotlight index, see [`Making app entities available in Spotlight`](making-app-entities-available-in-spotlight.md).

## Topics

### Specifying entity-related attributes
- [var attributeSet: CSSearchableItemAttributeSet](indexedentity/attributeset.md)
  A custom attribute set that you include with your entity to improve search accuracy.
- [var defaultAttributeSet: CSSearchableItemAttributeSet](indexedentity/defaultattributeset.md)
  The default set of attributes to include with your app entity in the Spotlight index.
### Hiding an entity from search results
- [var hideInSpotlight: Bool](indexedentity/hideinspotlight.md)
  A Boolean value that indicates whether Spotlight prevents the inclusion of the entity in the index.

## Relationships

### Inherits From
- [AppEntity](appentity.md)
- [AppValue](appvalue.md)
- [CustomLocalizedStringResourceConvertible](../foundation/customlocalizedstringresourceconvertible.md)
- [DisplayRepresentable](displayrepresentable.md)
- [Identifiable](../swift/identifiable.md)
- [InstanceDisplayRepresentable](instancedisplayrepresentable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)

## See Also

- [protocol AppEntity](appentity.md)
  An interface for making a custom type or app-specific concept discoverable by Apple Intelligence and experiences like Siri or the Shortcuts app.
- [protocol FileEntity](fileentity.md)
  An entity that refers to a document or other file.
- [protocol SyncableEntity](syncableentity.md)
  An interface that indicates your entity has an identifier that’s consistent across devices.
- [protocol TransientAppEntity](transientappentity.md)
  A type that represents a transient model object which exposes its interface to App Intents via properties. Note that `TransientAppEntity` types are not meant to be queried.
- [protocol UniqueAppEntity](uniqueappentity.md)
  An entity that will only ever have one value, such as global settings.
- [protocol OwnershipProvidingEntity](ownershipprovidingentity.md)
  A type that provides the system with ownership and sharing context for an app entity.
- [macro UnionValue()](unionvalue().md)
- [protocol AppUnionValue](appunionvalue.md)
  A protocol that provides nominal type identity and metadata for union values.
- [protocol AppUnionValueCasesProviding](appunionvaluecasesproviding.md)
  A protocol for the cases enumeration of an `AppUnionValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/indexedentity)*