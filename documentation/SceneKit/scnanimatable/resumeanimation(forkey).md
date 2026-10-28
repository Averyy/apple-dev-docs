# resumeAnimation(forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Resumes a previously paused animation attached to the object with the specified key.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

> **Deprecated**: Use -[SCNAnimationPlayer setPaused:] instead

## Declaration

```swift
func resumeAnimation(forKey key: String)
```

```objc
- (void) resumeAnimationForKey:(NSString *) key;
```

## Discussion

This method has no effect if no animation is attached to the object with the specified key or if the specified animation is not currently paused.

## Parameters

- `key`: A string identifying an attached animation.

## See Also

### Pausing and Resuming Animations
- [func pauseAnimation(forKey: String)](./pauseanimation%28forkey%29.md)
  Pauses the animation attached to the object with the specified key.
- [func isAnimationPaused(forKey: String) -> Bool](./isanimationpaused%28forkey%29.md)
  Returns a Boolean value indicating whether the animation attached to the object with the specified key is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimatable/resumeanimation(forkey:))*