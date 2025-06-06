# decode(from:)

**Framework**: Create ML Components  
**Kind**: method

Decodes the transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func decode(from decoder: inout any EstimatorDecoder) throws -> SupervisedEstimatorToTemporalAdaptor<Base>.Transformer
```

## See Also

- [func encode(SupervisedEstimatorToTemporalAdaptor<Base>.Transformer, to: inout any EstimatorEncoder) throws](supervisedestimatortotemporaladaptor/encode(_:to:).md)
  Encodes a fitted transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedestimatortotemporaladaptor/decode(from:))*