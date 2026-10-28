# add(_:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addWithNoise:(GKNoise *) noise;
```

## Discussion

Note that adding noise values can result in values outside the [-1.0, 1.0] range used for colorizing noise. If you plan to procduce colorized textures from the noise object, use the [`remapValues(toCurveWithControlPoints:)`](./remapvalues%28tocurvewithcontrolpoints%29.md) method to return results to that range first.

![](https://developer.apple.com/tutorials/images/com.apple.gameplaykit/media-2556393@2x.png)

## Parameters

- `noise`: The noise object from which to add noise values.

## See Also

### Applying Operations that Combine Noise
- [func multiply(GKNoise)](./multiply%28_%29.md)
  Replaces values in the noise field by multiplying them with values from the specified noise object.
- [func raiseToPower(GKNoise)](./raisetopower%28_%29-zm5g.md)
  Replaces values in the noise field by exponentiating them with values from the specified noise object.
- [func maximum(GKNoise)](./maximum%28_%29.md)
  Replaces values in the noise field by choosing the lesser of each value and a corresponding value in the specified noise object.
- [func minimum(GKNoise)](./minimum%28_%29.md)
  Replaces values in the noise field by choosing the lesser of each value and a corresponding value in the specified noise object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/add(_:))*