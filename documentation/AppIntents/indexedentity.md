# IndexedEntity

**Framework**: App Intents  
**Kind**: protocol

`IndexedEntity` represents an App Entity decorated with an attribute set. A set of attributes that enable the system to perform structured indexing  and queries of entities.

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

## Topics

### Instance Properties
- [var attributeSet: CSSearchableItemAttributeSet](indexedentity/attributeset.md)
  Provide a customized attribute set for improved search accuracy.
- [var defaultAttributeSet: CSSearchableItemAttributeSet](indexedentity/defaultattributeset.md)
  Custom attributes that improve search accuracy in Spotlight.
- [var hideInSpotlight: Bool](indexedentity/hideinspotlight.md)
  Controls whether this entity will be displayed in search results in the Spotlight UI.

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
- [TypeDisplayRepresentable](typedisplayrepresentable.md)

## See Also

- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)
  Provide the system with information about the types your app uses to model its data so that your intents can use those types as parameters.
- [protocol AppEntity](appentity.md)
  An interface for exposing a custom type or app-specific concept to system experiences like Siri and the Shortcuts app.
- [protocol FileEntity](fileentity.md)
  An entity that refers to a document or other file.
- [protocol TransientAppEntity](transientappentity.md)
  A type that represents a transient model object which exposes its interface to App Intents via properties. Note that `TransientAppEntity` types are not meant to be queried.
- [protocol UniqueAppEntity](uniqueappentity.md)
  An entity that will only ever have one value, such as global settings.
- [protocol URLRepresentableEntity](urlrepresentableentity.md)
  An app entity with a URL representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/indexedentity)*