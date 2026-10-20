# removeAnimation(forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Removes the animation attached to the object with the specified key.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
func removeAnimation(forKey key: String)
```

```objc
- (void) removeAnimationForKey:(NSString *) key;
```

## Parameters

- `key`: A string identifying an attached animation to remove.

## See Also

### Managing Animations
- [func addAnimation(any SCNAnimationProtocol, forKey: String?)](./addanimation%28_,forkey%29.md)
  Adds an animation object for the specified key.
- [func animation(forKey: String) -> CAAnimation?](./animation%28forkey%29.md)
  Returns the animation with the specified key.
- [var animationKeys: [String]](./animationkeys.md)
  An array containing the keys of all animations currently attached to the object.
- [func removeAllAnimations()](./removeallanimations%28%29.md)
  Removes all the animations currently attached to the object.
- [func removeAnimation(forKey: String, fadeOutDuration: CGFloat)](./removeanimation%28forkey,fadeoutduration%29.md)
  Removes the animation attached to the object with the specified key, smoothly transitioning out of the animation’s effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimatable/removeanimation(forkey:))*