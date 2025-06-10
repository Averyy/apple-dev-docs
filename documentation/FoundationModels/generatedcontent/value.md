# value(_:)

**Framework**: Foundation Models  
**Kind**: method

Reads a top level, concrete partially generable type.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func value<Value>(_ type: Value.Type = Value.self) throws -> Value where Value : ConvertibleFromGeneratedContent
```

## See Also

- [func value(_:forProperty:)](generatedcontent/value(_:forproperty:).md)
  Reads a concrete generable type from named property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/value(_:))*