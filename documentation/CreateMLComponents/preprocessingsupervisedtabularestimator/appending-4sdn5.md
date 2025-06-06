# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this supervised tabular estimator with another supervised tabular estimator.

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
func appending<Other>(_ other: Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation> where Other : SupervisedTabularEstimator, Self.Annotation == Other.Annotation
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingsupervisedtabularestimator/appending(_:)-4sdn5)*