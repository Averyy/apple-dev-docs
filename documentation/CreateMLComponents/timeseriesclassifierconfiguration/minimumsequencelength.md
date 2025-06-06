# minimumSequenceLength

**Framework**: Create ML Components  
**Kind**: property

The minimum number of samples required to produce a classification.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var minimumSequenceLength: Int
```

#### Discussion

This configuration parameter controls the size of the model. Set it to the largest value that is reasonable for your task. For example if your input is accelerometer data sampled at 100Hz and you want to recognize actions, the minimum action duration may be one second, so the minimum sequence length is `100Hz * 1s = 100`. Defaults to 100.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifierconfiguration/minimumsequencelength)*