# applyAbsoluteValue()

**Framework**: GameplayKit  
**Kind**: method

Replaces all negative values in the noise field with their positive absolute values.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func applyAbsoluteValue()
```

#### Discussion

For example, a value of `-0.75` becomes `0.75`, but positive values such as `0.5` remain unchanged.

![None](https://docs-assets.developer.apple.com/published/2b77295592e93174ea3b5844840b6227/media-2556374%402x.png)

## See Also

- [func invert()](gknoise/invert.md)
  Replaces all values in the noise field with their opposite, reversing the range of noise values.
- [func raiseToPower(Double)](gknoise/raisetopower(_:)-14715.md)
  Replaces all values in the noise field by raising each value to the specified power.
- [func clamp(lowerBound: Double, upperBound: Double)](gknoise/clamp(lowerbound:upperbound:).md)
  Replaces values in the noise field outside the specified range with the values at the endpoints of that range.
- [func remapValues(toCurveWithControlPoints: [NSNumber : NSNumber])](gknoise/remapvalues(tocurvewithcontrolpoints:).md)
  Replaces values in the noise field by mapping them to a curve that passes through the specified control points.
- [func remapValues(toTerracesWithPeaks: [NSNumber], terracesInverted: Bool)](gknoise/remapvalues(toterraceswithpeaks:terracesinverted:).md)
  Replaces values in the noise field by mapping them to a terrace-like curve that passes through the specified control points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/applyabsolutevalue())*