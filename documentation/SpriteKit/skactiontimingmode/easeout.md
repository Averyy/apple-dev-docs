# SKActionTimingMode.easeOut

**Framework**: SpriteKit  
**Kind**: case

Specifies ease-out pacing. Ease-out pacing causes the animation to begin quickly and then slow as it completes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case easeOut
```

#### Discussion

By creating two separate actions, a [`moveTo(x:duration:)`](skaction/moveto(x:duration:).md) and a [`moveTo(y:duration:)`](skaction/moveto(y:duration:).md), and setting the former to [`SKActionTimingMode.easeOut`](skactiontimingmode/easeout.md), you can visualize the effect of this timing mode by tracing the path of a circular shape node running the actions in a group:

![Visualizing ease-out pacing](https://docs-assets.developer.apple.com/published/6ab64b2a3a37905fd0711cf788c1e02c/media-2743419%402x.png)

## See Also

- [SKActionTimingMode.linear](skactiontimingmode/linear.md)
  Specifies linear pacing. Linear pacing causes an animation to occur evenly over its duration.
- [SKActionTimingMode.easeIn](skactiontimingmode/easein.md)
  Specifies ease-in pacing. Ease-in pacing causes the animation to begin slowly and then speed up as it progresses.
- [SKActionTimingMode.easeInEaseOut](skactiontimingmode/easeineaseout.md)
  Specifies ease-in ease-out pacing. An ease-in ease-out animation begins slowly, accelerates through the middle of its duration, and then slows again before completing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skactiontimingmode/easeout)*