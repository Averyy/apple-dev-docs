# screenRecorder(_:didStopRecordingWithError:previewViewController:)

**Framework**: ReplayKit  
**Kind**: method

Indicates that the screen recording has stopped.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func screenRecorder(_ screenRecorder: RPScreenRecorder, didStopRecordingWithError error: any Error, previewViewController: RPPreviewViewController?)
```

#### Discussion

[`screenRecorder(_:didStopRecordingWithError:previewViewController:)`](rpscreenrecorderdelegate/screenrecorder(_:didstoprecordingwitherror:previewviewcontroller:).md) is called when recording stops due to an error or a change in recording availability. If any part of the stopped recording is available, an instance of [`RPPreviewViewController`](rppreviewviewcontroller.md) is returned.

## Parameters

- `screenRecorder`: The   instance.
- `error`: An   describing why the recording stopped.
- `previewViewController`: An   interface object that is returned if anything at all was recorded. The interface allows the user to preview and edit the recording.

## See Also

- [func screenRecorder(RPScreenRecorder, didStopRecordingWith: RPPreviewViewController?, error: (any Error)?)](rpscreenrecorderdelegate/screenrecorder(_:didstoprecordingwith:error:).md)
  Indicates that the screen recording has stopped.
- [func screenRecorderDidChangeAvailability(RPScreenRecorder)](rpscreenrecorderdelegate/screenrecorderdidchangeavailability(_:).md)
  Indicates that the recorder has changed states between disabled and enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate/screenrecorder(_:didstoprecordingwitherror:previewviewcontroller:))*