# decodeWithOptimizer(from:)

**Framework**: Create ML Components  
**Kind**: method

Reads the encoded transformer and optimizer with a decoder.

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
func decodeWithOptimizer(from decoder: inout any EstimatorDecoder) throws -> LogisticRegressionClassifier<Scalar, Label>.Transformer
```

#### Return Value

The decoded transformer.

## Parameters

- `decoder`: A decoder.

## See Also

- [func encodeWithOptimizer(LogisticRegressionClassifier<Scalar, Label>.Transformer, to: inout any EstimatorEncoder) throws](logisticregressionclassifier/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifier/decodewithoptimizer(from:))*