# SessionPropertyKey

**Framework**: Foundation Models  
**Kind**: protocol

A protocol for defining a custom session property key.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol SessionPropertyKey : SendableMetatype
```

## Topics

### Inspecting a property key
- [static var defaultValue: Self.Value](sessionpropertykey/defaultvalue.md)
  The default value of the property key.
- [associatedtype Value](sessionpropertykey/value.md)
  The type of value that represent this property key.

## Relationships

### Inherits From
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [LanguageModelSession.SessionProperty](languagemodelsession/sessionproperty.md)
  A property wrapper that provides access to properties from within profiles,  dynamic instructions, and tools.
- [class SessionPropertyValues](sessionpropertyvalues.md)
  A container for property values.
- [macro SessionPropertyEntry()](sessionpropertyentry().md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/sessionpropertykey)*