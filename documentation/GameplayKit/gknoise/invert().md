# invert()

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) invert;
```

## Discussion

For example, a value of `1.0` becomes `-1.0`, a value of `-0.5` becomes `0.5`, and so on.

![](https://developer.apple.com/tutorials/images/com.apple.gameplaykit/media-2556378@2x.png)

## See Also

### Applying Operations to Noise Values
- [func applyAbsoluteValue()](./applyabsolutevalue%28%29.md)
  Replaces all negative values in the noise field with their positive absolute values.
- [func raiseToPower(Double)](./raisetopower%28_%29-14715.md)
  Replaces all values in the noise field by raising each value to the specified power.
- [func clamp(lowerBound: Double, upperBound: Double)](./clamp%28lowerbound,upperbound%29.md)
  Replaces values in the noise field outside the specified range with the values at the endpoints of that range.
- [func remapValues(toCurveWithControlPoints: [NSNumber : NSNumber])](./remapvalues%28tocurvewithcontrolpoints%29.md)
  Replaces values in the noise field by mapping them to a curve that passes through the specified control points.
- [func remapValues(toTerracesWithPeaks: [NSNumber], terracesInverted: Bool)](./remapvalues%28toterraceswithpeaks,terracesinverted%29.md)
  Replaces values in the noise field by mapping them to a terrace-like curve that passes through the specified control points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/invert())*