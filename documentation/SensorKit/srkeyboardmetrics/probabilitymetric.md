# SRKeyboardMetrics.ProbabilityMetric

**Framework**: SensorKit  
**Kind**: class  
**Role**: Class

A likelihood of occurrence.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class ProbabilityMetric<UnitType> where UnitType : Unit
```

```objc
@interface SRKeyboardProbabilityMetric : NSObject
```

#### Overview

The framework derives these values based on raw sensor data.

## Topics

### Sample Values
- [var distributionSampleValues: [Measurement<UnitType>]](./probabilitymetric/distributionsamplevalues.md)
  An array of sample values from the probability distribution.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Timing Key Use
- [var touchDownUp: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](./touchdownup.md)
  The duration between touch down to touch up for any key.
- [var touchUpDown: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](./touchupdown.md)
  The duration between touch up and touch down for any key.
- [var spaceTouchDownUp: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](./spacetouchdownup.md)
  The duration between touch down and touch up of all Space bar events for the keyboard.
- [var deleteTouchDownUp: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](./deletetouchdownup.md)
  The duration between touch down and touch up of all Delete key events for the keyboard.
- [var shortWordCharKeyTouchDownUp: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](./shortwordcharkeytouchdownup.md)
  The duration between touch down and touch up of all character keys in short words for the keyboard.
- [var touchDownDown: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](./touchdowndown.md)
  The duration between touch down and touch down for any key.
- [var charKeyToPrediction: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](./charkeytoprediction.md)
  The duration between touch up on a character key and touch down on a word in the prediction bar.
- [var shortWordCharKeyToCharKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](./shortwordcharkeytocharkey.md)
  The duration between touch up on a character key and touch down on any sequential character key in a short word.
- [var charKeyToAnyTapKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](./charkeytoanytapkey.md)
  The duration between touch up on a character key and touch down on the next sequential key.
- [var anyTapToCharKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](./anytaptocharkey.md)
  The duration between touch up of any key and touch down on a sequential character key.
- [var spaceToCharKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](./spacetocharkey.md)
  The duration between touch up of the Space bar and touch down of a sequential character key.
- [var charKeyToSpaceKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](./charkeytospacekey.md)
  The duration between touch up of a character key and touch down of a sequential Space bar.
- [var spaceToDeleteKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](./spacetodeletekey.md)
  The duration between touch up of the Space bar and touch down of a sequential Delete key.
- [var deleteToSpaceKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](./deletetospacekey.md)
  The duration between touch up of the Delete key and touch down of a sequential Space bar.
- [var spaceToSpaceKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>](./spacetospacekey.md)
  The duration between touch up of the Space bar and touch down of a sequential Space bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/probabilitymetric)*