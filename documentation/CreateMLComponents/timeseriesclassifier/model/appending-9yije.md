# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this transformer with an updatable supervised temporal estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func appending<Other>(_ other: Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, UpdatableSupervisedEstimatorToTemporalAdaptor<Other>> where Other : UpdatableSupervisedEstimator, Self.Output == Other.Transformer.Input, Other.Annotation : Sendable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier/model/appending(_:)-9yije)*