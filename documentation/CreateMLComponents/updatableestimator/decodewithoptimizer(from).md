# decodeWithOptimizer(from:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Reads the encoded transformer and optimizer with a decoder.

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
func decodeWithOptimizer(from decoder: inout any EstimatorDecoder) throws -> Self.Transformer
```

## Return Value

The decoded transformer.

## Parameters

- `decoder`: A decoder.

## See Also

### Encoding and decoding
- [func encodeWithOptimizer(Self.Transformer, to: inout any EstimatorEncoder) throws](./encodewithoptimizer%28_,to%29.md)
  Encodes the transformer and optimizer to an encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatableestimator/decodewithoptimizer(from:))*