# clamp(lowerBound:upperBound:)

**Framework**: GameplayKit  
**Kind**: method

Replaces values in the noise field outside the specified range with the values at the endpoints of that range.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func clamp(lowerBound: Double, upperBound: Double)
```

#### Discussion

For example, if you specify lower and upper bounds of `-0.5` and `0.5`, this operation replaces values less than `-0.5` with `-0.5` and values greater than `0.5` with `0.5`.

![None](https://docs-assets.developer.apple.com/published/9f9145f7e60b452d961a7ab64f6a4aab/media-2556384%402x.png)

## Parameters

- `lowerBound`: The minimum value to keep in processed noise.
- `upperBound`: The maximum value to keep in processed noise.

## See Also

- [func applyAbsoluteValue()](gknoise/applyabsolutevalue.md)
  Replaces all negative values in the noise field with their positive absolute values.
- [func invert()](gknoise/invert.md)
  Replaces all values in the noise field with their opposite, reversing the range of noise values.
- [func raiseToPower(Double)](gknoise/raisetopower(_:)-14715.md)
  Replaces all values in the noise field by raising each value to the specified power.
- [func remapValues(toCurveWithControlPoints: [NSNumber : NSNumber])](gknoise/remapvalues(tocurvewithcontrolpoints:).md)
  Replaces values in the noise field by mapping them to a curve that passes through the specified control points.
- [func remapValues(toTerracesWithPeaks: [NSNumber], terracesInverted: Bool)](gknoise/remapvalues(toterraceswithpeaks:terracesinverted:).md)
  Replaces values in the noise field by mapping them to a terrace-like curve that passes through the specified control points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/clamp(lowerbound:upperbound:))*