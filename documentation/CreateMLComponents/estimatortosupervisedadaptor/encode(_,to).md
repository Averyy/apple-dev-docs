# encode(_:to:)

**Framework**: Create ML Components  
**Kind**: method

Does nothing since this estimator uses a pre-defined transformer.

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
func encode(_ transformer: EstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, to encoder: inout any EstimatorEncoder) throws
```

## See Also

- [func decode(from: inout any EstimatorDecoder) throws -> EstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](estimatortosupervisedadaptor/decode(from:).md)
  Returns the pre-defined transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimatortosupervisedadaptor/encode(_:to:))*