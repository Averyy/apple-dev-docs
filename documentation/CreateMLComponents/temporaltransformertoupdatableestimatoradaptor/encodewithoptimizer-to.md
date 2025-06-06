# encodeWithOptimizer(_:to:)

**Framework**: Create ML Components  
**Kind**: method

This method is part of the conformance. It doesn’t encode anything since the transformer is pre-defined, so don’t call it.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func encodeWithOptimizer(_ transformer: Transformer, to encoder: inout any EstimatorEncoder) throws
```

## See Also

- [func encode(Transformer, to: inout any EstimatorEncoder) throws](temporaltransformertoupdatableestimatoradaptor/encode(_:to:).md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> Transformer](temporaltransformertoupdatableestimatoradaptor/decode(from:).md)
  Returns the pre-defined transformer.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> Transformer](temporaltransformertoupdatableestimatoradaptor/decodewithoptimizer(from:).md)
  Returns the pre-defined transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformertoupdatableestimatoradaptor/encodewithoptimizer(_:to:))*