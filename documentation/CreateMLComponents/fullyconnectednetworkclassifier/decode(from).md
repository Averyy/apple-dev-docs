# decode(from:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Decodes the estimator.

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
func decode(from decoder: inout any EstimatorDecoder) throws -> FullyConnectedNetworkClassifierModel<Scalar, Label>
```

Available when `Scalar` conforms to `MLShapedArrayScalar`, `Scalar` conforms to `BinaryFloatingPoint`, `Label` conforms to `Comparable`, `Label` conforms to `Decodable`, `Label` conforms to `Encodable`, and `Label` conforms to `Hashable`.

## Return Value

A fully connected network classifier model.

## Parameters

- `decoder`: A decoder for the estimator.

## See Also

### Encoding and decoding
- [func encodeWithOptimizer(FullyConnectedNetworkClassifier<Scalar, Label>.Transformer, to: inout any EstimatorEncoder) throws](./encodewithoptimizer%28_,to%29.md)
  Encodes a fitted transformer with an optimizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkclassifier/decode(from:))*