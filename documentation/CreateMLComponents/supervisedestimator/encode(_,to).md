# encode(_:to:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a fitted transformer.

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
func encode(_ transformer: Self.Transformer, to encoder: inout any EstimatorEncoder) throws
```

## Default Implementations

### SupervisedEstimator Implementations
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](./encode%28_,to%29-6hrgs.md)
  Encodes a fitted encodable transformer.

## See Also

### Encoding and decoding
- [func decode(from: inout any EstimatorDecoder) throws -> Self.Transformer](./decode%28from%29.md)
  Decodes a previously fitted transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedestimator/encode(_:to:))*