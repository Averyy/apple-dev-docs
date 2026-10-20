# decode(_:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Decodes a value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
mutating func decode<T>(_ type: T.Type) throws -> T where T : Decodable
```

## See Also

### Decoding values
- [func decodeOptimizer<T>(T.Type) throws -> T](./decodeoptimizer%28_%29.md)
  Decodes an optimizer value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimatordecoder/decode(_:))*