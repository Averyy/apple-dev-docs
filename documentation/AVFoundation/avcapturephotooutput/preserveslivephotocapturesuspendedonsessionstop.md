# preservesLivePhotoCaptureSuspendedOnSessionStop

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) BOOL preservesLivePhotoCaptureSuspendedOnSessionStop;
```

#### Discussion

This value defaults to [`false`](../../Swift/false.md), which means that Live Photo capture resumes when the session stops. Set the value to [`true`](../../Swift/true.md) to save the state of the [`isLivePhotoCaptureSuspended`](./islivephotocapturesuspended.md) property across session restarts.

## See Also

### Configuring Live Photo capture
- [var isLivePhotoCaptureSupported: Bool](./islivephotocapturesupported.md)
  A Boolean value that indicates whether the capture output currently supports Live Photo capture.
- [var isLivePhotoCaptureEnabled: Bool](./islivephotocaptureenabled.md)
  A Boolean value that indicates whether to configure the capture pipeline for Live Photo capture.
- [var isLivePhotoCaptureSuspended: Bool](./islivephotocapturesuspended.md)
  A Boolean value that indicates whether Live Photo capture is currently in a suspended state.
- [var isLivePhotoAutoTrimmingEnabled: Bool](./islivephotoautotrimmingenabled.md)
  A Boolean value that indicates whether to automatically trim Live Photo movie captures to avoid excessive movement.
- [var availableLivePhotoVideoCodecTypes: [AVVideoCodecType]](./availablelivephotovideocodectypes.md)
  An array of video codecs currently available for Live Photo movie captures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/preserveslivephotocapturesuspendedonsessionstop)*