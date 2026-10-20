# pause(_:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Pauses playback of the view’s scene.

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
@IBAction
func pause(_ sender: Any?)
```

```objc
- (void) pause:(id) sender;
```

#### Discussion

This method has no effect if the scene is already paused.

## Parameters

- `sender`: The object requesting the action (used when connecting a control in Interface Builder). SceneKit ignores this parameter.

## See Also

### Playing Action and Animation in a View’s Scene
- [func play(Any?)](./play%28_%29.md)
  Resumes playback of the view’s scene.
- [func stop(Any?)](./stop%28_%29.md)
  Stops playback of the view’s scene and resets the scene time to its start time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/pause(_:))*