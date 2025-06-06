# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this updatable tabular estimator with a tabular transformer.

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
func appending<Other>(_ other: Other) -> some UpdatableTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>> where Other : TabularTransformer
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatabletabularestimator/appending(_:)-4p7u0)*