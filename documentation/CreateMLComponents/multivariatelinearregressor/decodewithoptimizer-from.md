# decodeWithOptimizer(from:)

**Framework**: Create ML Components  
**Kind**: method

Reads the encoded model and optimizer with a decoder.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func decodeWithOptimizer(from decoder: inout any EstimatorDecoder) throws -> MultivariateLinearRegressor<Scalar>.Model
```

#### Return Value

The decoded model.

## Parameters

- `decoder`: A decoder.

## See Also

- [func encodeWithOptimizer(MultivariateLinearRegressor<Scalar>.Model, to: inout any EstimatorEncoder) throws](multivariatelinearregressor/encodewithoptimizer(_:to:).md)
  Encodes the model and optimizer to an encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/decodewithoptimizer(from:))*