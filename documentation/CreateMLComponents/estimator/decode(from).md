# decode(from:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Decodes a previously fitted transformer.

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
func decode(from decoder: inout any EstimatorDecoder) throws -> Self.Transformer
```

## Default Implementations

### Estimator Implementations
- [func decode(from: inout any EstimatorDecoder) throws -> Self.Transformer](./decode%28from%29-7hnqc.md)
  Decodes a previously fitted decodable transformer.

## See Also

### Encoding and decoding
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](./encode%28_,to%29.md)
  Encodes a fitted transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimator/decode(from:))*