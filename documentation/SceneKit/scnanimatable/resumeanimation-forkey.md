# resumeAnimation(forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Resumes a previously paused animation attached to the object with the specified key.

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
func resumeAnimation(forKey key: String)
```

#### Discussion

This method has no effect if no animation is attached to the object with the specified key or if the specified animation is not currently paused.

## Parameters

- `key`: A string identifying an attached animation.

## See Also

- [func pauseAnimation(forKey: String)](scnanimatable/pauseanimation(forkey:).md)
  Pauses the animation attached to the object with the specified key.
- [func isAnimationPaused(forKey: String) -> Bool](scnanimatable/isanimationpaused(forkey:).md)
  Returns a Boolean value indicating whether the animation attached to the object with the specified key is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimatable/resumeanimation(forkey:))*