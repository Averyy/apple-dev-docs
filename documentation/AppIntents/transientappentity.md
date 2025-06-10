# TransientAppEntity

**Framework**: App Intents  
**Kind**: protocol

A type that represents a transient model object which exposes its interface to App Intents via properties. Note that `TransientAppEntity` types are not meant to be queried.

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
protocol TransientAppEntity : AppEntity
```

## Topics

### Initializers
- [init()](transientappentity/init.md)
  Transient entities must be initializable so they can be initialized and populated by the system.

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

- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)
  Provide the system with information about the types your app uses to model its data so that your intents can use those types as parameters.
- [protocol AppEntity](appentity.md)
  An interface for exposing a custom type or app-specific concept to system experiences like Siri and the Shortcuts app.
- [protocol FileEntity](fileentity.md)
  An entity that refers to a document or other file.
- [protocol IndexedEntity](indexedentity.md)
  `IndexedEntity` represents an App Entity decorated with an attribute set. A set of attributes that enable the system to perform structured indexing  and queries of entities.
- [protocol UniqueAppEntity](uniqueappentity.md)
  An entity that will only ever have one value, such as global settings.
- [protocol URLRepresentableEntity](urlrepresentableentity.md)
  An app entity with a URL representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/transientappentity)*