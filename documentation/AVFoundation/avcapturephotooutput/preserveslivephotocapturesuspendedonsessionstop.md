# preservesLivePhotoCaptureSuspendedOnSessionStop

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether to preserve the suspended state of Live Photo capture when the session stops.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
var preservesLivePhotoCaptureSuspendedOnSessionStop: Bool { get set }
```

#### Discussion

This value defaults to [`false`](https://developer.apple.com/documentation/swift/false), which means that Live Photo capture resumes when the session stops. Set the value to [`true`](https://developer.apple.com/documentation/swift/true) to save the state of the [`isLivePhotoCaptureSuspended`](avcapturephotooutput/islivephotocapturesuspended.md) property across session restarts.

## See Also

- [var isLivePhotoCaptureSupported: Bool](avcapturephotooutput/islivephotocapturesupported.md)
  A Boolean value that indicates whether the capture output currently supports Live Photo capture.
- [var isLivePhotoCaptureEnabled: Bool](avcapturephotooutput/islivephotocaptureenabled.md)
  A Boolean value that indicates whether to configure the capture pipeline for Live Photo capture.
- [var isLivePhotoCaptureSuspended: Bool](avcapturephotooutput/islivephotocapturesuspended.md)
  A Boolean value that indicates whether Live Photo capture is currently in a suspended state.
- [var isLivePhotoAutoTrimmingEnabled: Bool](avcapturephotooutput/islivephotoautotrimmingenabled.md)
  A Boolean value that indicates whether to automatically trim Live Photo movie captures to avoid excessive movement.
- [var availableLivePhotoVideoCodecTypes: [AVVideoCodecType]](avcapturephotooutput/availablelivephotovideocodectypes.md)
  An array of video codecs currently available for Live Photo movie captures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/preserveslivephotocapturesuspendedonsessionstop)*