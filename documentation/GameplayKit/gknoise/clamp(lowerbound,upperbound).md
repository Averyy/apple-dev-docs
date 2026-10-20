# clamp(lowerBound:upperBound:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) clampWithLowerBound:(double) lowerBound upperBound:(double) upperBound;
```

#### Discussion

For example, if you specify lower and upper bounds of `-0.5` and `0.5`, this operation replaces values less than `-0.5` with `-0.5` and values greater than `0.5` with `0.5`.

![](https://developer.apple.com/tutorials/images/com.apple.gameplaykit/media-2556384@2x.png)

## Parameters

- `lowerBound`: The minimum value to keep in processed noise.
- `upperBound`: The maximum value to keep in processed noise.

## See Also

### Applying Operations to Noise Values
- [func applyAbsoluteValue()](./applyabsolutevalue%28%29.md)
  Replaces all negative values in the noise field with their positive absolute values.
- [func invert()](./invert%28%29.md)
  Replaces all values in the noise field with their opposite, reversing the range of noise values.
- [func raiseToPower(Double)](./raisetopower%28_%29-14715.md)
  Replaces all values in the noise field by raising each value to the specified power.
- [func remapValues(toCurveWithControlPoints: [NSNumber : NSNumber])](./remapvalues%28tocurvewithcontrolpoints%29.md)
  Replaces values in the noise field by mapping them to a curve that passes through the specified control points.
- [func remapValues(toTerracesWithPeaks: [NSNumber], terracesInverted: Bool)](./remapvalues%28toterraceswithpeaks,terracesinverted%29.md)
  Replaces values in the noise field by mapping them to a terrace-like curve that passes through the specified control points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/clamp(lowerbound:upperbound:))*