# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this updatable temporal estimator with a temporal transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func appending<Other>(_ other: Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>> where Other : TemporalTransformer, Other.Input == Self.Transformer.Output
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatabletemporalestimator/appending(_:)-6o3uc)*