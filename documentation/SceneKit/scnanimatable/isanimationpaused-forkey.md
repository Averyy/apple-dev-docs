# isAnimationPaused(forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Returns a Boolean value indicating whether the animation attached to the object with the specified key is paused.

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
func isAnimationPaused(forKey key: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the specified animation is paused. [`false`](https://developer.apple.com/documentation/swift/false) if the animation is running or no animation is attached to the object with that key.

## Parameters

- `key`: A string identifying an attached animation.

## See Also

- [func pauseAnimation(forKey: String)](scnanimatable/pauseanimation(forkey:).md)
  Pauses the animation attached to the object with the specified key.
- [func resumeAnimation(forKey: String)](scnanimatable/resumeanimation(forkey:).md)
  Resumes a previously paused animation attached to the object with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimatable/isanimationpaused(forkey:))*