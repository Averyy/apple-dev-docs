# value(_:forProperty:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Reads a concrete generable type from a named property.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
func value<Value>(_ type: Value.Type = Value.self, forProperty property: String) throws -> Value where Value : ConvertibleFromGeneratedContent
```

**Other overloads**:

```swift
func value<Value>(_ type: Value?.Type = Value?.self, forProperty property: String) throws -> Value? where Value : ConvertibleFromGeneratedContent
```

## Mentions

- [Generating Swift data structures with guided generation](../generating-swift-data-structures-with-guided-generation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/value(_:forproperty:)-3xsez)*