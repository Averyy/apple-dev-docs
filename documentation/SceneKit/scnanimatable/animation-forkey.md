# animation(forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Returns the animation with the specified key.

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
func animation(forKey key: String) -> CAAnimation?
```

#### Return Value

An animation object matching the key, or `nil` if no such animation exists.

#### Discussion

Attempting to modify any properties of the returned object results in undefined behavior.

## Parameters

- `key`: A string identifying a previously added animation.

## See Also

- [func addAnimation(any SCNAnimationProtocol, forKey: String?)](scnanimatable/addanimation(_:forkey:).md)
  Adds an animation object for the specified key.
- [var animationKeys: [String]](scnanimatable/animationkeys.md)
  An array containing the keys of all animations currently attached to the object.
- [func removeAllAnimations()](scnanimatable/removeallanimations.md)
  Removes all the animations currently attached to the object.
- [func removeAnimation(forKey: String)](scnanimatable/removeanimation(forkey:).md)
  Removes the animation attached to the object with the specified key.
- [func removeAnimation(forKey: String, fadeOutDuration: CGFloat)](scnanimatable/removeanimation(forkey:fadeoutduration:).md)
  Removes the animation attached to the object with the specified key, smoothly transitioning out of the animation’s effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimatable/animation(forkey:))*