# screenRecorder(_:didStopRecordingWith:error:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Indicates that the screen recording has stopped.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use ScreenCaptureKit SCStream with SCRecordingOutput instead

## Declaration

```swift
optional func screenRecorder(_ screenRecorder: RPScreenRecorder, didStopRecordingWith previewViewController: RPPreviewViewController?, error: (any Error)?)
```

```objc
- (void) screenRecorder:(RPScreenRecorder *) screenRecorder didStopRecordingWithPreviewViewController:(RPPreviewViewController *) previewViewController error:(NSError *) error;
```

## Discussion

This method is called when recording stops due to an error or a change in recording availability. If any part of the stopped recording is available, an instance of [`RPPreviewViewController`](../rppreviewviewcontroller.md) is returned.

## Parameters

- `screenRecorder`: The [`RPScreenRecorder`](../rpscreenrecorder.md) instance.
- `previewViewController`: An [`RPPreviewViewController`](../rppreviewviewcontroller.md) interface object that is returned if anything at all was recorded. The interface allows the user to preview and edit the recording.
- `error`: An [`NSError`](../../Foundation/nserror.md) describing why the recording stopped. This method is `nil` when no error occurs.

## See Also

### Responding to Recording Changes
- [func screenRecorderDidChangeAvailability(RPScreenRecorder)](./screenrecorderdidchangeavailability%28_%29.md)
  Indicates that the recorder has changed states between disabled and enabled.
- [func screenRecorder(RPScreenRecorder, didStopRecordingWithError: any Error, previewViewController: RPPreviewViewController?)](./screenrecorder%28_,didstoprecordingwitherror,previewviewcontroller%29.md)
  Indicates that the screen recording has stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate/screenrecorder(_:didstoprecordingwith:error:))*