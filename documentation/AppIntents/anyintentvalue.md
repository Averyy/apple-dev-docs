# AnyIntentValue

**Framework**: App Intents  
**Kind**: protocol

A type the system uses to access a parameter or property value.

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
protocol AnyIntentValue : Sendable
```

## Topics

### Getting the value type
- [associatedtype Value : _IntentValue, Sendable](anyintentvalue/value.md)
### Getting type-specific information
- [var title: LocalizedStringResource](anyintentvalue/title.md)
- [var isOptional: Bool](anyintentvalue/isoptional.md)

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [EntityProperty](entityproperty.md)
- [IntentParameter](intentparameter.md)
- [IntentParameterContext](intentparametercontext.md)

## See Also

- [class EntityProperty](entityproperty.md)
  A property wrapper that exposes the associated property to the system.
- [protocol AppValue](appvalue.md)
  An interface that describes conceptual types you use in app intents.
- [protocol AppEnum](appenum.md)
  An interface to express that a custom type has a predefined, static set of valid values to display.
- [protocol URLRepresentableEnum](urlrepresentableenum.md)
  An app enum with a URL representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/anyintentvalue)*