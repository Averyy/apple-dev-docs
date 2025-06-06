# raiseToPower(_:)

**Framework**: GameplayKit  
**Kind**: method

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

#### Discussion

Noise values are generally in the range [-1.0, 1.0], so exponentiating some points in a noise field can result in values outside the floating-point domain. Depending on the stylistic result you’re looking for, choose your base and exponent noises carefully or use other noise operations (such as the [`clamp(lowerBound:upperBound:)`](gknoise/clamp(lowerbound:upperbound:).md) and [`remapValues(toCurveWithControlPoints:)`](gknoise/remapvalues(tocurvewithcontrolpoints:).md) methods) to conform the exponent noise to a specific range before using this method.

![None](https://docs-assets.developer.apple.com/published/3043706ebd299a81cd10a5884ece1f88/media-2556399%402x.png)

## Parameters

- `noise`: The noise object from which to use values as exponents.

## See Also

- [func add(GKNoise)](gknoise/add(_:).md)
  Replaces values in the noise field by adding them to values from the specified noise object.
- [func multiply(GKNoise)](gknoise/multiply(_:).md)
  Replaces values in the noise field by multiplying them with values from the specified noise object.
- [func maximum(GKNoise)](gknoise/maximum(_:).md)
  Replaces values in the noise field by choosing the lesser of each value and a corresponding value in the specified noise object.
- [func minimum(GKNoise)](gknoise/minimum(_:).md)
  Replaces values in the noise field by choosing the lesser of each value and a corresponding value in the specified noise object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/raisetopower(_:)-zm5g)*