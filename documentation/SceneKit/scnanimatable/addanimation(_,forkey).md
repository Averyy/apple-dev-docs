# addAnimation(_:forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds an animation object for the specified key.

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
func addAnimation(_ animation: any SCNAnimationProtocol, forKey key: String?)
```

```objc
- (void) addAnimation:(id<SCNAnimation>) animation forKey:(NSString *) key;
```

## Discussion

Newly added animations begin executing after the current run loop cycle ends.

SceneKit does not define any requirements for the contents of the `key` parameter—it need only be unique among the keys for other animations you add. If you add an animation with an existing key, this method overwrites the existing animation.

## Parameters

- `animation`: The animation object to be added.
- `key`: An string identifying the animation for later retrieval. You may pass `nil` if you don’t need to reference the animation later.

## See Also

### Managing Animations
- [func animation(forKey: String) -> CAAnimation?](./animation%28forkey%29.md)
  Returns the animation with the specified key.
- [var animationKeys: [String]](./animationkeys.md)
  An array containing the keys of all animations currently attached to the object.
- [func removeAllAnimations()](./removeallanimations%28%29.md)
  Removes all the animations currently attached to the object.
- [func removeAnimation(forKey: String)](./removeanimation%28forkey%29.md)
  Removes the animation attached to the object with the specified key.
- [func removeAnimation(forKey: String, fadeOutDuration: CGFloat)](./removeanimation%28forkey,fadeoutduration%29.md)
  Removes the animation attached to the object with the specified key, smoothly transitioning out of the animation’s effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimatable/addanimation(_:forkey:))*