# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Compose this tabular estimator with another tabular estimator.

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
func appending<Other>(_ other: Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>> where Other : TabularEstimator
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingtabularestimator/appending(_:)-5w500)*