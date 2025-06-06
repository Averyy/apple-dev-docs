# stop(_:)

**Framework**: SceneKit  
**Kind**: method

Stops playback of the view’s scene and resets the scene time to its start time.

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
@MainActor func stop(_ sender: Any?)
```

## Parameters

- `sender`: The object requesting the action (used when connecting a control in Interface Builder). SceneKit ignores this parameter.

## See Also

- [func pause(Any?)](scnview/pause(_:).md)
  Pauses playback of the view’s scene.
- [func play(Any?)](scnview/play(_:).md)
  Resumes playback of the view’s scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/stop(_:))*