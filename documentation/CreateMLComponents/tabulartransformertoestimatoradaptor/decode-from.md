# decode(from:)

**Framework**: Create ML Components  
**Kind**: method

Returns the pre-defined tabular transformer.

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
func decode(from decoder: inout any EstimatorDecoder) throws -> Transformer
```

## See Also

- [func encode(Transformer, to: inout any EstimatorEncoder) throws](tabulartransformertoestimatoradaptor/encode(_:to:).md)
  Does nothing since this tabular estimator uses a pre-defined tabular transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabulartransformertoestimatoradaptor/decode(from:))*