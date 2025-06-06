# addAnimation(_:forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Adds an animation object for the specified key.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func addAnimation(_ animation: any SCNAnimationProtocol, forKey key: String?)
```

#### Discussion

Newly added animations begin executing after the current run loop cycle ends.

SceneKit does not define any requirements for the contents of the `key` parameter—it need only be unique among the keys for other animations you add. If you add an animation with an existing key, this method overwrites the existing animation.

## Parameters

- `animation`: The animation object to be added.
- `key`: An string identifying the animation for later retrieval. You may pass   if you don’t need to reference the animation later.

## See Also

- [func animation(forKey: String) -> CAAnimation?](scnanimatable/animation(forkey:).md)
  Returns the animation with the specified key.
- [var animationKeys: [String]](scnanimatable/animationkeys.md)
  An array containing the keys of all animations currently attached to the object.
- [func removeAllAnimations()](scnanimatable/removeallanimations.md)
  Removes all the animations currently attached to the object.
- [func removeAnimation(forKey: String)](scnanimatable/removeanimation(forkey:).md)
  Removes the animation attached to the object with the specified key.
- [func removeAnimation(forKey: String, fadeOutDuration: CGFloat)](scnanimatable/removeanimation(forkey:fadeoutduration:).md)
  Removes the animation attached to the object with the specified key, smoothly transitioning out of the animation’s effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimatable/addanimation(_:forkey:))*