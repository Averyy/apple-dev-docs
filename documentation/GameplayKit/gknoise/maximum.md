# maximum(_:)

**Framework**: GameplayKit  
**Kind**: method

Replaces values in the noise field by choosing the lesser of each value and a corresponding value in the specified noise object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func maximum(_ noise: GKNoise)
```

#### Discussion

In a grayscale texture, higher values are brighter and lower values are darker.

![None](https://docs-assets.developer.apple.com/published/c5c04e6f3a331d2371799338c9978d76/media-2556403%402x.png)

## Parameters

- `noise`: The noise object from which to compare and replace values.

## See Also

- [func add(GKNoise)](gknoise/add(_:).md)
  Replaces values in the noise field by adding them to values from the specified noise object.
- [func multiply(GKNoise)](gknoise/multiply(_:).md)
  Replaces values in the noise field by multiplying them with values from the specified noise object.
- [func raiseToPower(GKNoise)](gknoise/raisetopower(_:)-zm5g.md)
  Replaces values in the noise field by exponentiating them with values from the specified noise object.
- [func minimum(GKNoise)](gknoise/minimum(_:).md)
  Replaces values in the noise field by choosing the lesser of each value and a corresponding value in the specified noise object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/maximum(_:))*