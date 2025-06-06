# invert()

**Framework**: GameplayKit  
**Kind**: method

Replaces all values in the noise field with their opposite, reversing the range of noise values.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func invert()
```

#### Discussion

For example, a value of `1.0` becomes `-1.0`, a value of `-0.5` becomes `0.5`, and so on.

![None](https://docs-assets.developer.apple.com/published/be0782532bbccce465c4910d2a585c15/media-2556378%402x.png)

## See Also

- [func applyAbsoluteValue()](gknoise/applyabsolutevalue.md)
  Replaces all negative values in the noise field with their positive absolute values.
- [func raiseToPower(Double)](gknoise/raisetopower(_:)-14715.md)
  Replaces all values in the noise field by raising each value to the specified power.
- [func clamp(lowerBound: Double, upperBound: Double)](gknoise/clamp(lowerbound:upperbound:).md)
  Replaces values in the noise field outside the specified range with the values at the endpoints of that range.
- [func remapValues(toCurveWithControlPoints: [NSNumber : NSNumber])](gknoise/remapvalues(tocurvewithcontrolpoints:).md)
  Replaces values in the noise field by mapping them to a curve that passes through the specified control points.
- [func remapValues(toTerracesWithPeaks: [NSNumber], terracesInverted: Bool)](gknoise/remapvalues(toterraceswithpeaks:terracesinverted:).md)
  Replaces values in the noise field by mapping them to a terrace-like curve that passes through the specified control points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/invert())*