# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this temporal transformer with a temporal estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func appending<Other>(_ other: Other) -> PreprocessingTemporalEstimator<Self, Other> where Other : TemporalEstimator, Self.Output == Other.Transformer.Input
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/model/appending(_:)-1q42d)*