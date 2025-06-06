# calculationMode

**Framework**: Core Animation  
**Kind**: property

Specifies how intermediate keyframe values are calculated by the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var calculationMode: CAAnimationCalculationMode { get set }
```

#### Discussion

The possible values are described in [`Value calculation modes`](value-calculation-modes.md). The default value of this property is [`linear`](caanimationcalculationmode/linear.md).

## See Also

- [var keyTimes: [NSNumber]?](cakeyframeanimation/keytimes.md)
  An optional array of `NSNumber` objects that define the time at which to apply a given keyframe segment.
- [var timingFunctions: [CAMediaTimingFunction]?](cakeyframeanimation/timingfunctions.md)
  An optional array of `CAMediaTimingFunction` objects that define the pacing for each keyframe segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/calculationmode)*