# remapValues(toTerracesWithPeaks:terracesInverted:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) remapValuesToTerracesWithPeaks:(NSArray<NSNumber *> *) peakInputValues terracesInverted:(BOOL) inverted;
```

## Discussion

When you call this method, the [`GKNoise`](../gknoise.md) class first creates a curve between the points in the `peakInputValues` array. Each point in the array is a value that remains unchanged, and the `inverted` parameter determines the shape of the curve in between those points. Then, this method uses the curve to replace values in the noise field. The resulting effect can be useful for generating textures that resemble realistic terrain, replacing sloping hills with dramatic plateaus and ridges.

![](https://developer.apple.com/tutorials/images/com.apple.gameplaykit/media-2556390@2x.png)

## Parameters

- `peakInputValues`: An array of noise values to use as the sharp points of the mapping curve.
- `inverted`: [`true`](../../Swift/true.md) for curves that start rising slowly and become more steep; [`false`](../../Swift/false.md) for curves that start rising quickly and become more shallow.

## See Also

### Applying Operations to Noise Values
- [func applyAbsoluteValue()](./applyabsolutevalue%28%29.md)
  Replaces all negative values in the noise field with their positive absolute values.
- [func invert()](./invert%28%29.md)
  Replaces all values in the noise field with their opposite, reversing the range of noise values.
- [func raiseToPower(Double)](./raisetopower%28_%29-14715.md)
  Replaces all values in the noise field by raising each value to the specified power.
- [func clamp(lowerBound: Double, upperBound: Double)](./clamp%28lowerbound,upperbound%29.md)
  Replaces values in the noise field outside the specified range with the values at the endpoints of that range.
- [func remapValues(toCurveWithControlPoints: [NSNumber : NSNumber])](./remapvalues%28tocurvewithcontrolpoints%29.md)
  Replaces values in the noise field by mapping them to a curve that passes through the specified control points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/remapvalues(toterraceswithpeaks:terracesinverted:))*