# decode(from:)

**Framework**: Create ML Components  
**Kind**: method

Decodes a previously fitted transformer.

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
func decode(from decoder: inout any EstimatorDecoder) throws -> MultivariateLinearRegressor<Scalar>.Model
```

## See Also

- [func encode(MultivariateLinearRegressor<Scalar>.Model, to: inout any EstimatorEncoder) throws](multivariatelinearregressor/encode(_:to:).md)
  Encodes a fitted transformer.
- [func encodeWithOptimizer(MultivariateLinearRegressor<Scalar>.Model, to: inout any EstimatorEncoder) throws](multivariatelinearregressor/encodewithoptimizer(_:to:).md)
  Encodes the model and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/decodewithoptimizer(from:).md)
  Reads the encoded model and optimizer with a decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/decode(from:))*