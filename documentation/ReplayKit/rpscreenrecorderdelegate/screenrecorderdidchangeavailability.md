# screenRecorderDidChangeAvailability(_:)

**Framework**: ReplayKit  
**Kind**: method

Indicates that the recorder has changed states between disabled and enabled.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func screenRecorderDidChangeAvailability(_ screenRecorder: RPScreenRecorder)
```

#### Discussion

Screen recording can be unavailable due to unsupported hardware, the user’s device displaying information over Airplay or through a TVOut session, or another app using the shared recorder.

## Parameters

- `screenRecorder`: The   instance that has changed state.

## See Also

- [func screenRecorder(RPScreenRecorder, didStopRecordingWith: RPPreviewViewController?, error: (any Error)?)](rpscreenrecorderdelegate/screenrecorder(_:didstoprecordingwith:error:).md)
  Indicates that the screen recording has stopped.
- [func screenRecorder(RPScreenRecorder, didStopRecordingWithError: any Error, previewViewController: RPPreviewViewController?)](rpscreenrecorderdelegate/screenrecorder(_:didstoprecordingwitherror:previewviewcontroller:).md)
  Indicates that the screen recording has stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate/screenrecorderdidchangeavailability(_:))*