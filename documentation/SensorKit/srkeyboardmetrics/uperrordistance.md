# upErrorDistance

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The distance from the touch up to the center of any key.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var upErrorDistance: SRKeyboardMetrics.ProbabilityMetric<UnitLength> { get }
```

```objc
@property (strong, readonly) SRKeyboardProbabilityMetric<NSUnitLength *> * upErrorDistance;
```

## See Also

### Measuring Key Use
- [var longWordUpErrorDistance: [SRKeyboardMetrics.ProbabilityMetric<UnitLength>]](./longworduperrordistance.md)
  The distance from the touch up to the center of the intended key of the characters of a long word.
- [var longWordDownErrorDistance: [SRKeyboardMetrics.ProbabilityMetric<UnitLength>]](./longworddownerrordistance.md)
  The distance from the touch down to the center of the intended key of the characters of a long word.
- [var downErrorDistance: SRKeyboardMetrics.ProbabilityMetric<UnitLength>](./downerrordistance.md)
  The distance from the touch down to the center of any key.
- [var spaceUpErrorDistance: SRKeyboardMetrics.ProbabilityMetric<UnitLength>](./spaceuperrordistance.md)
  The distance from the touch up to the right centroid of the Space bar.
- [var spaceDownErrorDistance: SRKeyboardMetrics.ProbabilityMetric<UnitLength>](./spacedownerrordistance.md)
  The distance from the touch down to the right centroid of the Space bar.
- [var deleteUpErrorDistance: SRKeyboardMetrics.ProbabilityMetric<UnitLength>](./deleteuperrordistance.md)
  The distance from the touch up to the center of the Delete key.
- [var deleteDownErrorDistance: SRKeyboardMetrics.ProbabilityMetric<UnitLength>](./deletedownerrordistance.md)
  The distance from the touch down to the center of the Delete key.
- [var shortWordCharKeyUpErrorDistance: SRKeyboardMetrics.ProbabilityMetric<UnitLength>](./shortwordcharkeyuperrordistance.md)
  The distance from the touch up to the center of the intended key of a character in a short word.
- [var shortWordCharKeyDownErrorDistance: SRKeyboardMetrics.ProbabilityMetric<UnitLength>](./shortwordcharkeydownerrordistance.md)
  The distance from the touch down to the center of the intended key of a character in a short word.
- [var pathErrorDistanceRatio: [NSNumber]](./patherrordistanceratio.md)
  Sample values of the ratio of error distance between the intended and actual path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/uperrordistance)*