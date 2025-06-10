# removeAllAnimations()

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Removes all the animations currently attached to the object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func removeAllAnimations()
```

## See Also

- [func addAnimation(any SCNAnimationProtocol, forKey: String?)](scnanimatable/addanimation(_:forkey:).md)
  Adds an animation object for the specified key.
- [func animation(forKey: String) -> CAAnimation?](scnanimatable/animation(forkey:).md)
  Returns the animation with the specified key.
- [var animationKeys: [String]](scnanimatable/animationkeys.md)
  An array containing the keys of all animations currently attached to the object.
- [func removeAnimation(forKey: String)](scnanimatable/removeanimation(forkey:).md)
  Removes the animation attached to the object with the specified key.
- [func removeAnimation(forKey: String, fadeOutDuration: CGFloat)](scnanimatable/removeanimation(forkey:fadeoutduration:).md)
  Removes the animation attached to the object with the specified key, smoothly transitioning out of the animation’s effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimatable/removeallanimations())*