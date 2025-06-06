# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this supervised tabular estimator with a tabular transformer.

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
func appending<Other>(_ other: Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>, Self.Annotation> where Other : TabularTransformer, Self.Annotation : Equatable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeregressor/appending(_:)-6n1ry)*