# EstimatorDecoder

**Framework**: Create ML Components  
**Kind**: protocol

A type that can decode values from a model representation.

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
protocol EstimatorDecoder
```

## Topics

### Decoding values
- [func decode<T>(T.Type) throws -> T](estimatordecoder/decode(_:).md)
  Decodes a value.
- [func decodeOptimizer<T>(T.Type) throws -> T](estimatordecoder/decodeoptimizer(_:).md)
  Decodes an optimizer value.

## See Also

- [protocol EstimatorEncoder](estimatorencoder.md)
  A type that can encode values into a model representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimatordecoder)*