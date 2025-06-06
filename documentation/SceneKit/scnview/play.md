# play(_:)

**Framework**: SceneKit  
**Kind**: method

Resumes playback of the view’s scene.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@IBAction
@MainActor func play(_ sender: Any?)
```

#### Discussion

This method has no effect if the scene is not paused.

## Parameters

- `sender`: The object requesting the action (used when connecting a control in Interface Builder). SceneKit ignores this parameter.

## See Also

- [func pause(Any?)](scnview/pause(_:).md)
  Pauses playback of the view’s scene.
- [func stop(Any?)](scnview/stop(_:).md)
  Stops playback of the view’s scene and resets the scene time to its start time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/play(_:))*