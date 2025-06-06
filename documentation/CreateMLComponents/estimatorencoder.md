# EstimatorEncoder

**Framework**: Create ML Components  
**Kind**: protocol

A type that can encode values into a model representation.

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
protocol EstimatorEncoder
```

## Topics

### Encoding values
- [func encode<T>(T) throws](estimatorencoder/encode(_:).md)
  Encodes a value.
- [func encodeOptimizer<T>(T) throws](estimatorencoder/encodeoptimizer(_:).md)
  Encodes an estimator optimizer.

## See Also

- [protocol EstimatorDecoder](estimatordecoder.md)
  A type that can decode values from a model representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimatorencoder)*