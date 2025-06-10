# isLivePhotoCaptureSuspended

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether Live Photo capture is currently in a suspended state.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isLivePhotoCaptureSuspended: Bool { get set }
```

#### Discussion

By default, this property’s value is [`false`](https://developer.apple.com/documentation/swift/false). Set this value to [`true`](https://developer.apple.com/documentation/swift/true) to stop any current Live Photo movie captures in progress. Doing this prevents recording additional actions in the Live Photo movie. For example, if you want to capture a still photo that makes a shutter sound, you can prevent recording that action.

When you change this value to [`true`](https://developer.apple.com/documentation/swift/true), the system trims any Live Photo movie captures in progress to the current time. Likewise, when you change this value from [`true`](https://developer.apple.com/documentation/swift/true) to [`false`](https://developer.apple.com/documentation/swift/false), subsequent Live Photo movie captures won’t contain any earlier recordings.

By default, this property resets to [`false`](https://developer.apple.com/documentation/swift/false) when the [`AVCaptureSession`](avcapturesession.md) stops. You can prevent this behavior by setting [`preservesLivePhotoCaptureSuspendedOnSessionStop`](avcapturephotooutput/preserveslivephotocapturesuspendedonsessionstop.md) to [`true`](https://developer.apple.com/documentation/swift/true) before stopping the session.

> ❗ **Important**:  Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) throws an [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException) if the [`isLivePhotoCaptureEnabled`](avcapturephotooutput/islivephotocaptureenabled.md) property’s value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isLivePhotoCaptureSupported: Bool](avcapturephotooutput/islivephotocapturesupported.md)
  A Boolean value that indicates whether the capture output currently supports Live Photo capture.
- [var isLivePhotoCaptureEnabled: Bool](avcapturephotooutput/islivephotocaptureenabled.md)
  A Boolean value that indicates whether to configure the capture pipeline for Live Photo capture.
- [var preservesLivePhotoCaptureSuspendedOnSessionStop: Bool](avcapturephotooutput/preserveslivephotocapturesuspendedonsessionstop.md)
  A Boolean value that indicates whether to preserve the suspended state of Live Photo capture when the session stops.
- [var isLivePhotoAutoTrimmingEnabled: Bool](avcapturephotooutput/islivephotoautotrimmingenabled.md)
  A Boolean value that indicates whether to automatically trim Live Photo movie captures to avoid excessive movement.
- [var availableLivePhotoVideoCodecTypes: [AVVideoCodecType]](avcapturephotooutput/availablelivephotovideocodectypes.md)
  An array of video codecs currently available for Live Photo movie captures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/islivephotocapturesuspended)*