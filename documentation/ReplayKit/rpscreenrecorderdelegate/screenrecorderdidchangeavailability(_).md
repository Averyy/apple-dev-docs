# screenRecorderDidChangeAvailability(_:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Indicates that the recorder has changed states between disabled and enabled.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use ScreenCaptureKit instead

## Declaration

```swift
optional func screenRecorderDidChangeAvailability(_ screenRecorder: RPScreenRecorder)
```

```objc
- (void) screenRecorderDidChangeAvailability:(RPScreenRecorder *) screenRecorder;
```

## Discussion

Screen recording can be unavailable due to unsupported hardware, the user’s device displaying information over Airplay or through a TVOut session, or another app using the shared recorder.

## Parameters

- `screenRecorder`: The [`RPScreenRecorder`](../rpscreenrecorder.md) instance that has changed state.

## See Also

### Responding to Recording Changes
- [func screenRecorder(RPScreenRecorder, didStopRecordingWith: RPPreviewViewController?, error: (any Error)?)](./screenrecorder%28_,didstoprecordingwith,error%29.md)
  Indicates that the screen recording has stopped.
- [func screenRecorder(RPScreenRecorder, didStopRecordingWithError: any Error, previewViewController: RPPreviewViewController?)](./screenrecorder%28_,didstoprecordingwitherror,previewviewcontroller%29.md)
  Indicates that the screen recording has stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate/screenrecorderdidchangeavailability(_:))*