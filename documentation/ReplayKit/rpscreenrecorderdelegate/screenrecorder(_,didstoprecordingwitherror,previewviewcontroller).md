# screenRecorder(_:didStopRecordingWithError:previewViewController:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Indicates that the screen recording has stopped.

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 10.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: No longer supported

## Declaration

```swift
optional func screenRecorder(_ screenRecorder: RPScreenRecorder, didStopRecordingWithError error: any Error, previewViewController: RPPreviewViewController?)
```

```objc
- (void) screenRecorder:(RPScreenRecorder *) screenRecorder didStopRecordingWithError:(NSError *) error previewViewController:(RPPreviewViewController *) previewViewController;
```

#### Discussion

[`screenRecorder(_:didStopRecordingWithError:previewViewController:)`](./screenrecorder%28_,didstoprecordingwitherror,previewviewcontroller%29.md) is called when recording stops due to an error or a change in recording availability. If any part of the stopped recording is available, an instance of [`RPPreviewViewController`](../rppreviewviewcontroller.md) is returned.

## Parameters

- `screenRecorder`: The [`RPScreenRecorder`](../rpscreenrecorder.md) instance.
- `error`: An [`NSError`](../../Foundation/nserror.md) describing why the recording stopped.
- `previewViewController`: An [`RPPreviewViewController`](../rppreviewviewcontroller.md) interface object that is returned if anything at all was recorded. The interface allows the user to preview and edit the recording.

## See Also

### Responding to Recording Changes
- [func screenRecorder(RPScreenRecorder, didStopRecordingWith: RPPreviewViewController?, error: (any Error)?)](./screenrecorder%28_,didstoprecordingwith,error%29.md)
  Indicates that the screen recording has stopped.
- [func screenRecorderDidChangeAvailability(RPScreenRecorder)](./screenrecorderdidchangeavailability%28_%29.md)
  Indicates that the recorder has changed states between disabled and enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate/screenrecorder(_:didstoprecordingwitherror:previewviewcontroller:))*