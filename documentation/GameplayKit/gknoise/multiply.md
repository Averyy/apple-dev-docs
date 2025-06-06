# multiply(_:)

**Framework**: GameplayKit  
**Kind**: method

Replaces values in the noise field by multiplying them with values from the specified noise object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func multiply(_ noise: GKNoise)
```

#### Discussion

Noise values are generally in the range [-1.0, 1.0], so multiplying typically results in moving values toward zero (in grayscale textures, a darkening effect).

![None](https://docs-assets.developer.apple.com/published/f17ac6d8c33ac254d5254f199c0c750c/media-2556395%402x.png)

## Parameters

- `noise`: The noise object from which to multiply noise values.

## See Also

- [func add(GKNoise)](gknoise/add(_:).md)
  Replaces values in the noise field by adding them to values from the specified noise object.
- [func raiseToPower(GKNoise)](gknoise/raisetopower(_:)-zm5g.md)
  Replaces values in the noise field by exponentiating them with values from the specified noise object.
- [func maximum(GKNoise)](gknoise/maximum(_:).md)
  Replaces values in the noise field by choosing the lesser of each value and a corresponding value in the specified noise object.
- [func minimum(GKNoise)](gknoise/minimum(_:).md)
  Replaces values in the noise field by choosing the lesser of each value and a corresponding value in the specified noise object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/multiply(_:))*