# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this temporal estimator with a supervised temporal estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@preconcurrency
func appending<Other>(_ other: Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Other.Annotation> where Other : SupervisedEstimator, Other.Annotation : Sendable, Self.Transformer.Output == Other.Transformer.Input
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformertoupdatableestimatoradaptor/appending(_:)-1bv78)*