# value(_:forProperty:)

**Framework**: Foundation Models  
**Kind**: method

Reads a concrete generable type from named property.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func value<Value>(_ type: Value.Type = Value.self, forProperty property: String) throws -> Value where Value : ConvertibleFromGeneratedContent
```

## See Also

- [func value<Value>(Value.Type) throws -> Value](generatedcontent/value(_:).md)
  Reads a top level, concrete partially generable type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/value(_:forproperty:))*