# setSession(_:showVideoPreview:showAudioPreview:)

**Framework**: AVKit  
**Kind**: method

Sets the view’s capture session.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func setSession(_ session: AVCaptureSession?, showVideoPreview: Bool, showAudioPreview: Bool)
```

#### Discussion

The view must show audio preview, video preview, or both. Furthermore, the view may modify the capture session, for example, to access media data for preview or when the user select a new capture source.

The capture view automatically starts and stops the default session. If you set a custom capture session on the view, you need to manually manage the session’s life cycle events.

## Parameters

- `session`: The capture session.
- `showVideoPreview`: A Boolean value that indicates whether the view displays a video preview. If  , the system adds, removes, or modifies capture inputs for video data based on device availability and user selection.
- `showAudioPreview`: A Boolean value that indicates whether the view shows an audio preview. If  , the system adds, removes, or modifies capture inputs for audio data based on device availability and user selection.

## See Also

- [var session: AVCaptureSession?](avcaptureview/session.md)
  The view’s associated capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureview/setsession(_:showvideopreview:showaudiopreview:))*