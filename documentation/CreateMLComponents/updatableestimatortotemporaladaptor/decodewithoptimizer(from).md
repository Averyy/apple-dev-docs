# decodeWithOptimizer(from:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Reads the encoded transformer and optimizer with a decoder.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func decodeWithOptimizer(from decoder: inout any EstimatorDecoder) throws -> UpdatableEstimatorToTemporalAdaptor<Base>.Transformer
```

## Return Value

The decoded transformer.

## Parameters

- `decoder`: A decoder.

## See Also

### Encoding and decoding
- [func encode(UpdatableEstimatorToTemporalAdaptor<Base>.Transformer, to: inout any EstimatorEncoder) throws](./encode%28_,to%29.md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> UpdatableEstimatorToTemporalAdaptor<Base>.Transformer](./decode%28from%29.md)
  Decodes the transformer.
- [func encodeWithOptimizer(UpdatableEstimatorToTemporalAdaptor<Base>.Transformer, to: inout any EstimatorEncoder) throws](./encodewithoptimizer%28_,to%29.md)
  Encodes the transformer and optimizer to an encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatableestimatortotemporaladaptor/decodewithoptimizer(from:))*