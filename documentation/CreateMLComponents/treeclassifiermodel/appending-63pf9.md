# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this transformer with an updatable supervised estimator.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func appending<Other>(_ other: Other) -> PreprocessingUpdatableSupervisedTabularEstimator<Self, Other> where Other : UpdatableSupervisedTabularEstimator
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/treeclassifiermodel/appending(_:)-63pf9)*