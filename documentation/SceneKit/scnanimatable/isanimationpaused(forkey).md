# isAnimationPaused(forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value indicating whether the animation attached to the object with the specified key is paused.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

> **Deprecated**: Use -[SCNAnimationPlayer paused] instead

## Declaration

```swift
func isAnimationPaused(forKey key: String) -> Bool
```

```objc
- (BOOL) isAnimationForKeyPaused:(NSString *) key;
```

#### Return Value

[`true`](../../Swift/true.md) if the specified animation is paused. [`false`](../../Swift/false.md) if the animation is running or no animation is attached to the object with that key.

## Parameters

- `key`: A string identifying an attached animation.

## See Also

### Pausing and Resuming Animations
- [func pauseAnimation(forKey: String)](./pauseanimation%28forkey%29.md)
  Pauses the animation attached to the object with the specified key.
- [func resumeAnimation(forKey: String)](./resumeanimation%28forkey%29.md)
  Resumes a previously paused animation attached to the object with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimatable/isanimationpaused(forkey:))*