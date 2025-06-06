# add(_:)

**Framework**: GameplayKit  
**Kind**: method

Replaces values in the noise field by adding them to values from the specified noise object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func add(_ noise: GKNoise)
```

#### Discussion

Note that adding noise values can result in values outside the [-1.0, 1.0] range used for colorizing noise. If you plan to procduce colorized textures from the noise object, use the [`remapValues(toCurveWithControlPoints:)`](gknoise/remapvalues(tocurvewithcontrolpoints:).md) method to return results to that range first.

![None](https://docs-assets.developer.apple.com/published/6b036bda2456d6722e247192920f5a8f/media-2556393%402x.png)

## Parameters

- `noise`: The noise object from which to add noise values.

## See Also

- [func multiply(GKNoise)](gknoise/multiply(_:).md)
  Replaces values in the noise field by multiplying them with values from the specified noise object.
- [func raiseToPower(GKNoise)](gknoise/raisetopower(_:)-zm5g.md)
  Replaces values in the noise field by exponentiating them with values from the specified noise object.
- [func maximum(GKNoise)](gknoise/maximum(_:).md)
  Replaces values in the noise field by choosing the lesser of each value and a corresponding value in the specified noise object.
- [func minimum(GKNoise)](gknoise/minimum(_:).md)
  Replaces values in the noise field by choosing the lesser of each value and a corresponding value in the specified noise object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/add(_:))*