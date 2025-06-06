# SKActionTimingMode.easeIn

**Framework**: SpriteKit  
**Kind**: case

Specifies ease-in pacing. Ease-in pacing causes the animation to begin slowly and then speed up as it progresses.

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
case easeIn
```

#### Discussion

By creating two separate actions, a [`moveTo(x:duration:)`](skaction/moveto(x:duration:).md) and a [`moveTo(y:duration:)`](skaction/moveto(y:duration:).md), and setting the former to [`SKActionTimingMode.easeIn`](skactiontimingmode/easein.md), you can visualize the effect of this timing mode by tracing the path of a circular shape node running the actions in a group:

![Visualizing ease-in pacing](https://docs-assets.developer.apple.com/published/7895212b238c557342d596909bd37941/media-2743318%402x.png)

## See Also

- [SKActionTimingMode.linear](skactiontimingmode/linear.md)
  Specifies linear pacing. Linear pacing causes an animation to occur evenly over its duration.
- [SKActionTimingMode.easeOut](skactiontimingmode/easeout.md)
  Specifies ease-out pacing. Ease-out pacing causes the animation to begin quickly and then slow as it completes.
- [SKActionTimingMode.easeInEaseOut](skactiontimingmode/easeineaseout.md)
  Specifies ease-in ease-out pacing. An ease-in ease-out animation begins slowly, accelerates through the middle of its duration, and then slows again before completing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skactiontimingmode/easein)*