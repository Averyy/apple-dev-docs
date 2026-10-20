# encode(_:to:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

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
func encode(_ transformer: Estimator.Transformer, to encoder: inout any EstimatorEncoder) throws
```

## See Also

### Encoding and decoding
- [func decode(from: inout any EstimatorDecoder) throws -> Estimator.Transformer](./decode%28from%29.md)
  Decodes a previously fitted transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabularestimatortosupervisedadaptor/encode(_:to:))*