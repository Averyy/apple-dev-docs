# remapValues(toTerracesWithPeaks:terracesInverted:)

**Framework**: GameplayKit  
**Kind**: method

Replaces values in the noise field by mapping them to a terrace-like curve that passes through the specified control points.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func remapValues(toTerracesWithPeaks peakInputValues: [NSNumber], terracesInverted inverted: Bool)
```

#### Discussion

When you call this method, the [`GKNoise`](gknoise.md) class first creates a curve between the points in the `peakInputValues` array. Each point in the array is a value that remains unchanged, and the `inverted` parameter determines the shape of the curve in between those points. Then, this method uses the curve to replace values in the noise field. The resulting effect can be useful for generating textures that resemble realistic terrain, replacing sloping hills with dramatic plateaus and ridges.

![None](https://docs-assets.developer.apple.com/published/31604a8e83ff7fb74e6c941afbcc97a1/media-2556390%402x.png)

## Parameters

- `peakInputValues`: An array of noise values to use as the sharp points of the mapping curve.
- `inverted`:   for curves that start rising slowly and become more steep;   for curves that start rising quickly and become more shallow.

## See Also

- [func applyAbsoluteValue()](gknoise/applyabsolutevalue.md)
  Replaces all negative values in the noise field with their positive absolute values.
- [func invert()](gknoise/invert.md)
  Replaces all values in the noise field with their opposite, reversing the range of noise values.
- [func raiseToPower(Double)](gknoise/raisetopower(_:)-14715.md)
  Replaces all values in the noise field by raising each value to the specified power.
- [func clamp(lowerBound: Double, upperBound: Double)](gknoise/clamp(lowerbound:upperbound:).md)
  Replaces values in the noise field outside the specified range with the values at the endpoints of that range.
- [func remapValues(toCurveWithControlPoints: [NSNumber : NSNumber])](gknoise/remapvalues(tocurvewithcontrolpoints:).md)
  Replaces values in the noise field by mapping them to a curve that passes through the specified control points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/remapvalues(toterraceswithpeaks:terracesinverted:))*