# isLivePhotoCaptureEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to configure the capture pipeline for Live Photo capture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isLivePhotoCaptureEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isLivePhotoCaptureEnabled) BOOL livePhotoCaptureEnabled;
```

## Discussion

This value defaults to [`false`](../../Swift/false.md). Changing this value while your session is running requires a lengthy reconfiguration of the capture render pipeline. If you intend to take any Live Photo captures, set this value to [`true`](../../Swift/true.md) before calling [`AVCaptureSession`](../avcapturesession.md) [`startRunning()`](../avcapturesession/startrunning%28%29.md). If you change this property while the session is running, in-progress Live Photo captures end immediately, unfulfilled photo requests cancel, and the video preview temporarily freezes.

You must enable this option before initiating a photo capture with the [`livePhotoMovieFileURL`](../avcapturephotosettings/livephotomoviefileurl.md) property of your photo settings object set to non-`nil`. However, after you’ve enabled this option, you can issue photo capture requests for both Live Photo captures and still photos.

## See Also

### Configuring Live Photo capture
- [var isLivePhotoCaptureSupported: Bool](./islivephotocapturesupported.md)
  A Boolean value that indicates whether the capture output currently supports Live Photo capture.
- [var isLivePhotoCaptureSuspended: Bool](./islivephotocapturesuspended.md)
  A Boolean value that indicates whether Live Photo capture is currently in a suspended state.
- [var preservesLivePhotoCaptureSuspendedOnSessionStop: Bool](./preserveslivephotocapturesuspendedonsessionstop.md)
  A Boolean value that indicates whether to preserve the suspended state of Live Photo capture when the session stops.
- [var isLivePhotoAutoTrimmingEnabled: Bool](./islivephotoautotrimmingenabled.md)
  A Boolean value that indicates whether to automatically trim Live Photo movie captures to avoid excessive movement.
- [var availableLivePhotoVideoCodecTypes: [AVVideoCodecType]](./availablelivephotovideocodectypes.md)
  An array of video codecs currently available for Live Photo movie captures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/islivephotocaptureenabled)*