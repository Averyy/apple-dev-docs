# charKeyToAnyTapKey

**Framework**: SensorKit  
**Kind**: property

The duration between touch up on a character key and touch down on the next sequential key.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var charKeyToAnyTapKey: ProbabilityMetric<UnitDuration> { get }
```

#### Discussion

The next sequential key may be any key.

## See Also

- [SRKeyboardMetrics.ProbabilityMetric](srkeyboardmetrics/probabilitymetric.md)
  A likelihood of occurrence.
- [var touchDownUp: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/touchdownup.md)
  The duration between touch down to touch up for any key.
- [var touchUpDown: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/touchupdown.md)
  The duration between touch up and touch down for any key.
- [var spaceTouchDownUp: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/spacetouchdownup.md)
  The duration between touch down and touch up of all Space bar events for the keyboard.
- [var deleteTouchDownUp: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/deletetouchdownup.md)
  The duration between touch down and touch up of all Delete key events for the keyboard.
- [var shortWordCharKeyTouchDownUp: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/shortwordcharkeytouchdownup.md)
  The duration between touch down and touch up of all character keys in short words for the keyboard.
- [var touchDownDown: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/touchdowndown.md)
  The duration between touch down and touch down for any key.
- [var charKeyToPrediction: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/charkeytoprediction.md)
  The duration between touch up on a character key and touch down on a word in the prediction bar.
- [var shortWordCharKeyToCharKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/shortwordcharkeytocharkey.md)
  The duration between touch up on a character key and touch down on any sequential character key in a short word.
- [var anyTapToCharKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/anytaptocharkey.md)
  The duration between touch up of any key and touch down on a sequential character key.
- [var spaceToCharKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/spacetocharkey.md)
  The duration between touch up of the Space bar and touch down of a sequential character key.
- [var charKeyToSpaceKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/charkeytospacekey.md)
  The duration between touch up of a character key and touch down of a sequential Space bar.
- [var spaceToDeleteKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/spacetodeletekey.md)
  The duration between touch up of the Space bar and touch down of a sequential Delete key.
- [var deleteToSpaceKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/deletetospacekey.md)
  The duration between touch up of the Delete key and touch down of a sequential Space bar.
- [var spaceToSpaceKey: ProbabilityMetric<UnitDuration>](srkeyboardmetrics/spacetospacekey.md)
  The duration between touch up of the Space bar and touch down of a sequential Space bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/charkeytoanytapkey)*