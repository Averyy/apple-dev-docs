# raiseToPower(_:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Replaces values in the noise field by exponentiating them with values from the specified noise object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func raiseToPower(_ noise: GKNoise)
```

```objc
- (void) raiseToPowerWithNoise:(GKNoise *) noise;
```

## Discussion

Noise values are generally in the range [-1.0, 1.0], so exponentiating some points in a noise field can result in values outside the floating-point domain. Depending on the stylistic result you’re looking for, choose your base and exponent noises carefully or use other noise operations (such as the [`clamp(lowerBound:upperBound:)`](./clamp%28lowerbound,upperbound%29.md) and [`remapValues(toCurveWithControlPoints:)`](./remapvalues%28tocurvewithcontrolpoints%29.md) methods) to conform the exponent noise to a specific range before using this method.

![](https://developer.apple.com/tutorials/images/com.apple.gameplaykit/media-2556399@2x.png)

## Parameters

- `noise`: The noise object from which to use values as exponents.

## See Also

### Applying Operations that Combine Noise
- [func add(GKNoise)](./add%28_%29.md)
  Replaces values in the noise field by adding them to values from the specified noise object.
- [func multiply(GKNoise)](./multiply%28_%29.md)
  Replaces values in the noise field by multiplying them with values from the specified noise object.
- [func maximum(GKNoise)](./maximum%28_%29.md)
  Replaces values in the noise field by choosing the lesser of each value and a corresponding value in the specified noise object.
- [func minimum(GKNoise)](./minimum%28_%29.md)
  Replaces values in the noise field by choosing the lesser of each value and a corresponding value in the specified noise object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/raisetopower(_:)-zm5g)*