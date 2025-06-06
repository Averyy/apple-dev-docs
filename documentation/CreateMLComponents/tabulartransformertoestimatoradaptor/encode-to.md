# encode(_:to:)

**Framework**: Create ML Components  
**Kind**: method

Does nothing since this tabular estimator uses a pre-defined tabular transformer.

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

- [func decode(from: inout any EstimatorDecoder) throws -> Transformer](tabulartransformertoestimatoradaptor/decode(from:).md)
  Returns the pre-defined tabular transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabulartransformertoestimatoradaptor/encode(_:to:))*