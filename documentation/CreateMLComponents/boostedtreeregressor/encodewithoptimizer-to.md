# encodeWithOptimizer(_:to:)

**Framework**: Create ML Components  
**Kind**: method

Encodes the transformer and optimizer to an encoder.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func encodeWithOptimizer(_ transformer: TreeRegressorModel, to encoder: inout any EstimatorEncoder) throws
```

## Parameters

- `transformer`: A transformer this estimator creates.
- `encoder`: An encoder.

## See Also

- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> TreeRegressorModel](boostedtreeregressor/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeregressor/encodewithoptimizer(_:to:))*