# encode(_:to:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

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
func encode(_ transformer: Transformer, to encoder: inout any EstimatorEncoder) throws
```

## See Also

### Encoding and decoding
- [func decode(from: inout any EstimatorDecoder) throws -> Transformer](./decode%28from%29.md)
  Returns the pre-defined transformer.
- [func encodeWithOptimizer(Transformer, to: inout any EstimatorEncoder) throws](./encodewithoptimizer%28_,to%29.md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> Transformer](./decodewithoptimizer%28from%29.md)
  Returns the pre-defined transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabulartransformertoupdatableestimatoradaptor/encode(_:to:))*