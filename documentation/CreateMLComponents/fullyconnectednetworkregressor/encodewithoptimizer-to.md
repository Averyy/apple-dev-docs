# encodeWithOptimizer(_:to:)

**Framework**: Create ML Components  
**Kind**: method

Encodes a fitted transformer with an optimizer.

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
func encodeWithOptimizer(_ transformer: FullyConnectedNetworkRegressor<Scalar>.Transformer, to encoder: inout any EstimatorEncoder) throws
```

## Parameters

- `transformer`: A fully connected network regressor model.
- `encoder`: An encoder for the estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkregressor/encodewithoptimizer(_:to:))*