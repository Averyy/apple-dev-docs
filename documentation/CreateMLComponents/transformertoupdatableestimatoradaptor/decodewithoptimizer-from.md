# decodeWithOptimizer(from:)

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
func decodeWithOptimizer(from decoder: inout any EstimatorDecoder) throws -> Transformer
```

## See Also

- [func encode(Transformer, to: inout any EstimatorEncoder) throws](transformertoupdatableestimatoradaptor/encode(_:to:).md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> Transformer](transformertoupdatableestimatoradaptor/decode(from:).md)
  Returns the pre-defined transformer.
- [func encodeWithOptimizer(Transformer, to: inout any EstimatorEncoder) throws](transformertoupdatableestimatoradaptor/encodewithoptimizer(_:to:).md)
  Does nothing since this estimator uses a pre-defined transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertoupdatableestimatoradaptor/decodewithoptimizer(from:))*