# value(_:)

**Framework**: Foundation Models  
**Kind**: method

Reads a top level, concrete partially `Generable` type from a named property.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func value<Value>(_ type: Value.Type = Value.self) throws -> Value where Value : ConvertibleFromGeneratedContent
```

## See Also

- [func value(_:forProperty:)](generatedcontent/value(_:forproperty:).md)
  Reads a concrete `Generable` type from named property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/value(_:))*