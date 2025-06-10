# spaceToPredictionKey

**Framework**: SensorKit  
**Kind**: property

The duration between touch up of the Space bar and touch down of a sequential selection from the prediction bar.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var spaceToPredictionKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration> { get }
```

## See Also

- [SRKeyboardMetrics.ProbabilityMetric](srkeyboardmetrics/probabilitymetric.md)
  A likelihood of occurrence.
- [var touchDownUp: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](srkeyboardmetrics/touchdownup.md)
  The duration between touch down to touch up for any key.
- [var touchUpDown: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](srkeyboardmetrics/touchupdown.md)
  The duration between touch up and touch down for any key.
- [var spaceTouchDownUp: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](srkeyboardmetrics/spacetouchdownup.md)
  The duration between touch down and touch up of all Space bar events for the keyboard.
- [var deleteTouchDownUp: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](srkeyboardmetrics/deletetouchdownup.md)
  The duration between touch down and touch up of all Delete key events for the keyboard.
- [var shortWordCharKeyTouchDownUp: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](srkeyboardmetrics/shortwordcharkeytouchdownup.md)
  The duration between touch down and touch up of all character keys in short words for the keyboard.
- [var touchDownDown: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](srkeyboardmetrics/touchdowndown.md)
  The duration between touch down and touch down for any key.
- [var charKeyToPrediction: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](srkeyboardmetrics/charkeytoprediction.md)
  The duration between touch up on a character key and touch down on a word in the prediction bar.
- [var shortWordCharKeyToCharKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](srkeyboardmetrics/shortwordcharkeytocharkey.md)
  The duration between touch up on a character key and touch down on any sequential character key in a short word.
- [var charKeyToAnyTapKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](srkeyboardmetrics/charkeytoanytapkey.md)
  The duration between touch up on a character key and touch down on the next sequential key.
- [var anyTapToCharKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](srkeyboardmetrics/anytaptocharkey.md)
  The duration between touch up of any key and touch down on a sequential character key.
- [var spaceToCharKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](srkeyboardmetrics/spacetocharkey.md)
  The duration between touch up of the Space bar and touch down of a sequential character key.
- [var charKeyToSpaceKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](srkeyboardmetrics/charkeytospacekey.md)
  The duration between touch up of a character key and touch down of a sequential Space bar.
- [var spaceToDeleteKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](srkeyboardmetrics/spacetodeletekey.md)
  The duration between touch up of the Space bar and touch down of a sequential Delete key.
- [var deleteToSpaceKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](srkeyboardmetrics/deletetospacekey.md)
  The duration between touch up of the Delete key and touch down of a sequential Space bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/spacetopredictionkey)*