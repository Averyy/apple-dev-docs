# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Compose this tabular transformer with a tabular estimator.

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
func appending<Other>(_ other: Other) -> some TabularEstimator<ComposedTabularTransformer<Self, Other.Transformer>> where Other : TabularEstimator
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/treeclassifiermodel/appending(_:)-2wik9)*