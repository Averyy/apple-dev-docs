# encodeWithOptimizer(_:to:)

**Framework**: Create ML Components  
**Kind**: method

Encodes a fitted transformer with an optimizer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func encodeWithOptimizer(_ transformer: FullyConnectedNetworkMultiLabelClassifier<Scalar, Label>.Transformer, to encoder: inout any EstimatorEncoder) throws
```

## Parameters

- `transformer`: A fully-connected network multi-label classifier model.
- `encoder`: An encoder for the estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifier/encodewithoptimizer(_:to:))*