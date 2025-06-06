# fadeInDuration

**Framework**: Core Animation  
**Kind**: property

For animations attached to SceneKit objects, the duration for transitioning into the animation’s effect as it begins.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var fadeInDuration: CGFloat { get set }
```

#### Discussion

Use this property to create smooth transitions between the effects of multiple animations. These transitions are especially useful for geometry animations created with external 3D authoring tools.

For example, the geometry loaded from a scene file for a game character may have associated animations for player actions such as walking and jumping. When the player jumps, if the fade duration is zero, SceneKit abruptly switches from the current frame of the walk animation to the first frame of the jump animation. If the fade duration is greater than zero, SceneKit plays both animations at once during that duration and interpolates vertex positions from one animation to the other, creating a smooth transition.

To attach animations to SceneKit objects, see [`SCNAnimatable`](https://developer.apple.com/documentation/SceneKit/SCNAnimatable).

## See Also

- [var fadeOutDuration: CGFloat](caanimation/fadeoutduration.md)
  For animations attached to SceneKit objects, the duration for transitioning out of the animation’s effect as it ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimation/fadeinduration)*