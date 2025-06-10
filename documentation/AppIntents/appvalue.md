# AppValue

**Framework**: App Intents  
**Kind**: protocol

An interface that describes conceptual types you use in app intents.

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
protocol AppValue : PersistentlyIdentifiable, TypeDisplayRepresentable, _IntentValue, Sendable
```

#### Overview

This protocol serves as the base type for conceptual interfaces like [`AppEntity`](appentity.md) or [`AppEnum`](appenum.md).

## Relationships

### Inherits From
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)
### Inherited By
- [AppEntity](appentity.md)
- [AppEnum](appenum.md)
- [AssistantEntity](assistantentity.md)
- [AssistantEnum](assistantenum.md)
- [AssistantSchemaEntity](assistantschemaentity.md)
- [AssistantSchemaEnum](assistantschemaenum.md)
- [FileEntity](fileentity.md)
- [IndexedEntity](indexedentity.md)
- [TransientAppEntity](transientappentity.md)
- [URLRepresentableEntity](urlrepresentableentity.md)
- [URLRepresentableEnum](urlrepresentableenum.md)
- [UniqueAppEntity](uniqueappentity.md)
### Conforming Types
- [StringSearchScope](stringsearchscope.md)
- [VideoCategory](videocategory.md)

## See Also

- [class EntityProperty](entityproperty.md)
  A property wrapper that exposes the associated property to the system.
- [protocol AnyIntentValue](anyintentvalue.md)
  A type the system uses to access a parameter or property value.
- [protocol AppEnum](appenum.md)
  An interface to express that a custom type has a predefined, static set of valid values to display.
- [protocol URLRepresentableEnum](urlrepresentableenum.md)
  An app enum with a URL representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appvalue)*