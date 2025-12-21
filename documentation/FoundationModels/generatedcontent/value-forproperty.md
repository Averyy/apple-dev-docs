# value(_:forProperty:)

**Framework**: Foundation Models  
**Kind**: method

Reads a concrete `Generable` type from named property.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func value<Value>(_ type: Value.Type = Value.self, forProperty property: String) throws -> Value where Value : ConvertibleFromGeneratedContent
```

## See Also

- [func value<Value>(Value.Type) throws -> Value](generatedcontent/value(_:).md)
  Reads a top level, concrete partially `Generable` type from a named property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/value(_:forproperty:))*