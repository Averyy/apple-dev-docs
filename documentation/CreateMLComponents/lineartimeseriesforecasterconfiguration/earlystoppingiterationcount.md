# earlyStoppingIterationCount

**Framework**: Create ML Components  
**Kind**: property

The number of iterations to use when evaluating whether to stop early.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var earlyStoppingIterationCount: Int
```

#### Discussion

The `fitted` method will stop if no significant progress is made for this many iterations. Significant progress happens when the validation error decreases by at least `convergenceThreshold`.

> **Note**: Early stopping only happens when using the `fitted` method with validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecasterconfiguration/earlystoppingiterationcount)*