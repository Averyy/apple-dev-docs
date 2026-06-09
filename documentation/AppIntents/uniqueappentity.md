# UniqueAppEntity

**Framework**: App Intents  
**Kind**: protocol

An entity that will only ever have one value, such as global settings.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol UniqueAppEntity : AppEntity where Self.DefaultQuery : UniqueAppEntityQuery
```

## Relationships

### Inherits From
- [AppEntity](appentity.md)
- [AppValue](appvalue.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [DisplayRepresentable](displayrepresentable.md)
- [Identifiable](../Swift/Identifiable.md)
- [InstanceDisplayRepresentable](instancedisplayrepresentable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)

## See Also

- [protocol AppEntity](appentity.md)
  An interface for making a custom type or app-specific concept discoverable by Apple Intelligence and experiences like Siri or the Shortcuts app.
- [protocol FileEntity](fileentity.md)
  An entity that refers to a document or other file.
- [protocol IndexedEntity](indexedentity.md)
  An interface that allows you to include an entity in your app’s Spotlight index.
- [protocol SyncableEntity](syncableentity.md)
  An interface that indicates your entity has an identifier that’s consistent across devices.
- [protocol TransientAppEntity](transientappentity.md)
  A type that represents a transient model object which exposes its interface to App Intents via properties. Note that `TransientAppEntity` types are not meant to be queried.
- [protocol OwnershipProvidingEntity](ownershipprovidingentity.md)
  A type that provides the system with ownership and sharing context for an app entity.
- [macro UnionValue()](unionvalue().md)
- [protocol AppUnionValue](appunionvalue.md)
  A protocol that provides nominal type identity and metadata for union values.
- [protocol AppUnionValueCasesProviding](appunionvaluecasesproviding.md)
  A protocol for the cases enumeration of an `AppUnionValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/uniqueappentity)*