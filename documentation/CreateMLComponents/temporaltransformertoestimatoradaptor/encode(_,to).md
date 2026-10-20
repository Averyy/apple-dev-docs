# encode(_:to:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Does nothing since this estimator uses a pre-defined transformer.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func encode(_ transformer: Transformer, to encoder: inout any EstimatorEncoder) throws
```

## See Also

### Encoding and decoding
- [func decode(from: inout any EstimatorDecoder) throws -> Transformer](./decode%28from%29.md)
  Returns the pre-defined transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformertoestimatoradaptor/encode(_:to:))*