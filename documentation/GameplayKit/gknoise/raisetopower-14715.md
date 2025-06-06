# raiseToPower(_:)

**Framework**: GameplayKit  
**Kind**: method

Replaces all values in the noise field by raising each value to the specified power.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func raiseToPower(_ power: Double)
```

#### Discussion

Noise values range from `-1.0` to `1.0`, so exponentiating always results in lower values than in the original noise, with a greater effect on low original values than on high values.

![None](https://docs-assets.developer.apple.com/published/50760d93d511890921c54d121ce668ba/media-2556382%402x.png)

## Parameters

- `power`: The exponent to raise each noise value to.

## See Also

- [func applyAbsoluteValue()](gknoise/applyabsolutevalue.md)
  Replaces all negative values in the noise field with their positive absolute values.
- [func invert()](gknoise/invert.md)
  Replaces all values in the noise field with their opposite, reversing the range of noise values.
- [func clamp(lowerBound: Double, upperBound: Double)](gknoise/clamp(lowerbound:upperbound:).md)
  Replaces values in the noise field outside the specified range with the values at the endpoints of that range.
- [func remapValues(toCurveWithControlPoints: [NSNumber : NSNumber])](gknoise/remapvalues(tocurvewithcontrolpoints:).md)
  Replaces values in the noise field by mapping them to a curve that passes through the specified control points.
- [func remapValues(toTerracesWithPeaks: [NSNumber], terracesInverted: Bool)](gknoise/remapvalues(toterraceswithpeaks:terracesinverted:).md)
  Replaces values in the noise field by mapping them to a terrace-like curve that passes through the specified control points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/raisetopower(_:)-14715)*