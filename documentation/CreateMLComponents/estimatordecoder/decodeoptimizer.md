# decodeOptimizer(_:)

**Framework**: Create ML Components  
**Kind**: method  
**Required**: Yes

Decodes an optimizer value.

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
mutating func decodeOptimizer<T>(_ value: T.Type) throws -> T where T : Decodable
```

#### Discussion

Decoding an optimizer lets you resume fitting.

## See Also

- [func decode<T>(T.Type) throws -> T](estimatordecoder/decode(_:).md)
  Decodes a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimatordecoder/decodeoptimizer(_:))*