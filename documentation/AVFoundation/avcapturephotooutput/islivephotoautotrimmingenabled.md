# isLivePhotoAutoTrimmingEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether to automatically trim Live Photo movie captures to avoid excessive movement.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isLivePhotoAutoTrimmingEnabled: Bool { get set }
```

#### Discussion

This value defaults to [`true`](https://developer.apple.com/documentation/Swift/true) when [`isLivePhotoCaptureSupported`](avcapturephotooutput/islivephotocapturesupported.md) is [`true`](https://developer.apple.com/documentation/Swift/true).

Use this option to enable the same automatic trimming behavior found in the Camera app. By default, a Live Photo capture is about three seconds in duration, centered on the time of the capture request. If the user moves the camera during capture, iOS analyzes the capture and automatically trims the duration of the Live Photo to avoid capturing excess movement.

Changing this value while your session is running requires a lengthy reconfiguration of the session. If you intend to take any Live Photo captures, set this value to [`true`](https://developer.apple.com/documentation/Swift/true) before calling [`AVCaptureSession`](avcapturesession.md) [`startRunning()`](avcapturesession/startrunning().md). If you change this property while the session is running, in-progress Live Photo captures end immediately, unfulfilled photo requests cancel, and the video preview temporarily freezes.

## See Also

- [var isLivePhotoCaptureSupported: Bool](avcapturephotooutput/islivephotocapturesupported.md)
  A Boolean value that indicates whether the capture output currently supports Live Photo capture.
- [var isLivePhotoCaptureEnabled: Bool](avcapturephotooutput/islivephotocaptureenabled.md)
  A Boolean value that indicates whether to configure the capture pipeline for Live Photo capture.
- [var isLivePhotoCaptureSuspended: Bool](avcapturephotooutput/islivephotocapturesuspended.md)
  A Boolean value that indicates whether Live Photo capture is currently in a suspended state.
- [var preservesLivePhotoCaptureSuspendedOnSessionStop: Bool](avcapturephotooutput/preserveslivephotocapturesuspendedonsessionstop.md)
  A Boolean value that indicates whether to preserve the suspended state of Live Photo capture when the session stops.
- [var availableLivePhotoVideoCodecTypes: [AVVideoCodecType]](avcapturephotooutput/availablelivephotovideocodectypes.md)
  An array of video codecs currently available for Live Photo movie captures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/islivephotoautotrimmingenabled)*