# encode(_:to:)

**Framework**: Create ML Components  
**Kind**: method

Encodes a fitted transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func encode(_ transformer: SupervisedEstimatorToTemporalAdaptor<Base>.Transformer, to encoder: inout any EstimatorEncoder) throws
```

## See Also

- [func decode(from: inout any EstimatorDecoder) throws -> SupervisedEstimatorToTemporalAdaptor<Base>.Transformer](supervisedestimatortotemporaladaptor/decode(from:).md)
  Decodes the transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedestimatortotemporaladaptor/encode(_:to:))*