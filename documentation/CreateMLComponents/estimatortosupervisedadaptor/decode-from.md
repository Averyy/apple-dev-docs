# decode(from:)

**Framework**: Create ML Components  
**Kind**: method

Returns the pre-defined transformer.

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
func decode(from decoder: inout any EstimatorDecoder) throws -> EstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer
```

## See Also

- [func encode(EstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, to: inout any EstimatorEncoder) throws](estimatortosupervisedadaptor/encode(_:to:).md)
  Does nothing since this estimator uses a pre-defined transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimatortosupervisedadaptor/decode(from:))*