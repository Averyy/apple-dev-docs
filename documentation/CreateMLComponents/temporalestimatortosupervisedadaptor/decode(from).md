# decode(from:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Returns the pre-defined transformer.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func decode(from decoder: inout any EstimatorDecoder) throws -> TemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer
```

## See Also

### Encoding and decoding
- [func encode(TemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, to: inout any EstimatorEncoder) throws](./encode%28_,to%29.md)
  Does nothing since this estimator uses a pre-defined transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporalestimatortosupervisedadaptor/decode(from:))*