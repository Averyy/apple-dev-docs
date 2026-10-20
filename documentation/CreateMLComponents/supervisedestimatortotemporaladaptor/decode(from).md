# decode(from:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Decodes the transformer.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func decode(from decoder: inout any EstimatorDecoder) throws -> SupervisedEstimatorToTemporalAdaptor<Base>.Transformer
```

## See Also

### Encoding and decoding
- [func encode(SupervisedEstimatorToTemporalAdaptor<Base>.Transformer, to: inout any EstimatorEncoder) throws](./encode%28_,to%29.md)
  Encodes a fitted transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedestimatortotemporaladaptor/decode(from:))*