# maximum(_:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) maximumWithNoise:(GKNoise *) noise;
```

## Discussion

In a grayscale texture, higher values are brighter and lower values are darker.

![](https://developer.apple.com/tutorials/images/com.apple.gameplaykit/media-2556403@2x.png)

## Parameters

- `noise`: The noise object from which to compare and replace values.

## See Also

### Applying Operations that Combine Noise
- [func add(GKNoise)](./add%28_%29.md)
  Replaces values in the noise field by adding them to values from the specified noise object.
- [func multiply(GKNoise)](./multiply%28_%29.md)
  Replaces values in the noise field by multiplying them with values from the specified noise object.
- [func raiseToPower(GKNoise)](./raisetopower%28_%29-zm5g.md)
  Replaces values in the noise field by exponentiating them with values from the specified noise object.
- [func minimum(GKNoise)](./minimum%28_%29.md)
  Replaces values in the noise field by choosing the lesser of each value and a corresponding value in the specified noise object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/maximum(_:))*