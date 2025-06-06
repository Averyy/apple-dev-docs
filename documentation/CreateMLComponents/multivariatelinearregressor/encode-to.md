# encode(_:to:)

**Framework**: Create ML Components  
**Kind**: method

Encodes a fitted transformer.

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
func encode(_ model: MultivariateLinearRegressor<Scalar>.Model, to encoder: inout any EstimatorEncoder) throws
```

## See Also

- [func decode(from: inout any EstimatorDecoder) throws -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/decode(from:).md)
  Decodes a previously fitted transformer.
- [func encodeWithOptimizer(MultivariateLinearRegressor<Scalar>.Model, to: inout any EstimatorEncoder) throws](multivariatelinearregressor/encodewithoptimizer(_:to:).md)
  Encodes the model and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/decodewithoptimizer(from:).md)
  Reads the encoded model and optimizer with a decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/encode(_:to:))*