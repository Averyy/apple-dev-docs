# screenRecorder(_:didStopRecordingWith:error:)

**Framework**: ReplayKit  
**Kind**: method

Indicates that the screen recording has stopped.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func screenRecorder(_ screenRecorder: RPScreenRecorder, didStopRecordingWith previewViewController: RPPreviewViewController?, error: (any Error)?)
```

#### Discussion

This method is called when recording stops due to an error or a change in recording availability. If any part of the stopped recording is available, an instance of [`RPPreviewViewController`](rppreviewviewcontroller.md) is returned.

## Parameters

- `screenRecorder`: The   instance.
- `previewViewController`: An   interface object that is returned if anything at all was recorded. The interface allows the user to preview and edit the recording.
- `error`: An   describing why the recording stopped. This method is   when no error occurs.

## See Also

- [func screenRecorderDidChangeAvailability(RPScreenRecorder)](rpscreenrecorderdelegate/screenrecorderdidchangeavailability(_:).md)
  Indicates that the recorder has changed states between disabled and enabled.
- [func screenRecorder(RPScreenRecorder, didStopRecordingWithError: any Error, previewViewController: RPPreviewViewController?)](rpscreenrecorderdelegate/screenrecorder(_:didstoprecordingwitherror:previewviewcontroller:).md)
  Indicates that the screen recording has stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate/screenrecorder(_:didstoprecordingwith:error:))*