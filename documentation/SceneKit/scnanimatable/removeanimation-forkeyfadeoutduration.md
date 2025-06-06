# removeAnimation(forKey:fadeOutDuration:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Removes the animation attached to the object with the specified key, smoothly transitioning out of the animation’s effect.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func removeAnimation(forKey key: String, fadeOutDuration duration: CGFloat)
```

#### Discussion

Use this method to create smooth transitions between the effects of multiple animations. For example, the geometry loaded from a scene file for a game character may have associated animations for player actions such as walking and jumping. When the player lands from a jump, you remove the jump animation so the character continues walking. If you use the [`removeAnimation(forKey:)`](scnanimatable/removeanimation(forkey:).md) method to remove the jump animation, SceneKit abruptly switches from the current frame of the jump animation to the current frame of the walk animation. If you use the [`removeAnimation(forKey:fadeOutDuration:)`](scnanimatable/removeanimation(forkey:fadeoutduration:).md) method instead, SceneKit plays both animations at once during that duration and interpolates vertex positions from one animation to the other, creating a smooth transition.

## Parameters

- `key`: A string identifying an attached animation to remove.
- `duration`: The duration for transitioning out of the animation’s effect before it is removed.

## See Also

- [func addAnimation(any SCNAnimationProtocol, forKey: String?)](scnanimatable/addanimation(_:forkey:).md)
  Adds an animation object for the specified key.
- [func animation(forKey: String) -> CAAnimation?](scnanimatable/animation(forkey:).md)
  Returns the animation with the specified key.
- [var animationKeys: [String]](scnanimatable/animationkeys.md)
  An array containing the keys of all animations currently attached to the object.
- [func removeAllAnimations()](scnanimatable/removeallanimations.md)
  Removes all the animations currently attached to the object.
- [func removeAnimation(forKey: String)](scnanimatable/removeanimation(forkey:).md)
  Removes the animation attached to the object with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimatable/removeanimation(forkey:fadeoutduration:))*