# value(_:forProperty:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Reads an optional, concrete generable type from a named property.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
func value<Value>(_ type: Value?.Type = Value?.self, forProperty property: String) throws -> Value? where Value : ConvertibleFromGeneratedContent
```

**Other overloads**:

```swift
func value<Value>(_ type: Value.Type = Value.self, forProperty property: String) throws -> Value where Value : ConvertibleFromGeneratedContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/value(_:forproperty:)-6gy2p)*