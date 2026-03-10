# IndexedEntity

**Framework**: App Intents  
**Kind**: protocol

`IndexedEntity` represents an App Entity decorated with an attribute set. A set of attributes that enable the system to perform structured indexing  and queries of entities.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol IndexedEntity : AppEntity
```

## Mentions

- [Making app entities available in Spotlight](making-app-entities-available-in-spotlight.md)

## Topics

### Specifying entity-related attributes
- [var attributeSet: CSSearchableItemAttributeSet](indexedentity/attributeset.md)
  The custom Spotlight attributes to associate with the entity.
- [var defaultAttributeSet: CSSearchableItemAttributeSet](indexedentity/defaultattributeset.md)
  The default Spotlight attributes to associate with an entity.
### Hiding an entity from search results
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
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)

## See Also

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
- [macro UnionValue()](unionvalue().md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/indexedentity)*