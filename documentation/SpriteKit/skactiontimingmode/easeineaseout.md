# SKActionTimingMode.easeInEaseOut

**Framework**: SpriteKit  
**Kind**: case  
**Role**: Case

Specifies ease-in ease-out pacing. An ease-in ease-out animation begins slowly, accelerates through the middle of its duration, and then slows again before completing.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case easeInEaseOut
```

```c
SKActionTimingEaseInEaseOut
```

#### Discussion

By creating two separate actions, a [`moveTo(x:duration:)`](../skaction/moveto%28x,duration%29.md) and a [`moveTo(y:duration:)`](../skaction/moveto%28y,duration%29.md), and setting the former to [`SKActionTimingMode.easeInEaseOut`](./easeineaseout.md), you can visualize the effect of this timing mode by tracing the path of a circular shape node running the actions in a group:

![Visualizing ease-in ease-out pacing](https://developer.apple.com/tutorials/images/com.apple.spritekit/media-2743420@2x.png)

## See Also

### Constants
- [SKActionTimingMode.linear](./linear.md)
  Specifies linear pacing. Linear pacing causes an animation to occur evenly over its duration.
- [SKActionTimingMode.easeIn](./easein.md)
  Specifies ease-in pacing. Ease-in pacing causes the animation to begin slowly and then speed up as it progresses.
- [SKActionTimingMode.easeOut](./easeout.md)
  Specifies ease-out pacing. Ease-out pacing causes the animation to begin quickly and then slow as it completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skactiontimingmode/easeineaseout)*