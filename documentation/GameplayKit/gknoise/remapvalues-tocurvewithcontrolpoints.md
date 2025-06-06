# remapValues(toCurveWithControlPoints:)

**Framework**: GameplayKit  
**Kind**: method

Replaces values in the noise field by mapping them to a curve that passes through the specified control points.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func remapValues(toCurveWithControlPoints controlPoints: [NSNumber : NSNumber])
```

#### Discussion

When you call this method, the [`GKNoise`](gknoise.md) class first interpolates the values specified in the `controlPoints` parameter to create a smooth curve. Then, this method uses the curve to replace values in the noise field. For example, passing the control points `[-1.0: -1.0, -0.5: 0.5, 0.5: -0.5, 1.0: 1.0]` defines an S-shaped curve that leaves the lowest and highest values in the noise field unchanged, but replaces moderately low values with moderately high values and vice versa.

![None](https://docs-assets.developer.apple.com/published/9b3a3fb1539dceb756f4564e553397eb/media-2556387%402x.png)

## Parameters

- `controlPoints`: A dictionary whose keys are input values in the existing noise, and whose values are the output values to replace the input values with.

## See Also

- [func applyAbsoluteValue()](gknoise/applyabsolutevalue.md)
  Replaces all negative values in the noise field with their positive absolute values.
- [func invert()](gknoise/invert.md)
  Replaces all values in the noise field with their opposite, reversing the range of noise values.
- [func raiseToPower(Double)](gknoise/raisetopower(_:)-14715.md)
  Replaces all values in the noise field by raising each value to the specified power.
- [func clamp(lowerBound: Double, upperBound: Double)](gknoise/clamp(lowerbound:upperbound:).md)
  Replaces values in the noise field outside the specified range with the values at the endpoints of that range.
- [func remapValues(toTerracesWithPeaks: [NSNumber], terracesInverted: Bool)](gknoise/remapvalues(toterraceswithpeaks:terracesinverted:).md)
  Replaces values in the noise field by mapping them to a terrace-like curve that passes through the specified control points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/remapvalues(tocurvewithcontrolpoints:))*