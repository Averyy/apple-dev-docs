# isLivePhotoCaptureSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the capture output currently supports Live Photo capture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isLivePhotoCaptureSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isLivePhotoCaptureSupported) BOOL livePhotoCaptureSupported;
```

#### Discussion

Live Photo captures both a still image and a short movie centered on the moment of capture, and the system presents them together in user interfaces such as the Photos app.

Not all devices and capture formats support Live Photo capture. This property’s value can change if the [`sessionPreset`](../avcapturesession/sessionpreset.md) property of the current capture session or the [`activeFormat`](../avcapturedevice/activeformat.md) property of the underlying capture device changes.

When this value changes to [`false`](../../Swift/false.md), the [`isLivePhotoCaptureEnabled`](./islivephotocaptureenabled.md) property’s value also changes to [`false`](../../Swift/false.md). If you previously opted in for Live Photo capture and then change configurations, you may need to set [`isLivePhotoCaptureEnabled`](./islivephotocaptureenabled.md) to [`true`](../../Swift/true.md) again.

## See Also

### Configuring Live Photo capture
- [var isLivePhotoCaptureEnabled: Bool](./islivephotocaptureenabled.md)
  A Boolean value that indicates whether to configure the capture pipeline for Live Photo capture.
- [var isLivePhotoCaptureSuspended: Bool](./islivephotocapturesuspended.md)
  A Boolean value that indicates whether Live Photo capture is currently in a suspended state.
- [var preservesLivePhotoCaptureSuspendedOnSessionStop: Bool](./preserveslivephotocapturesuspendedonsessionstop.md)
  A Boolean value that indicates whether to preserve the suspended state of Live Photo capture when the session stops.
- [var isLivePhotoAutoTrimmingEnabled: Bool](./islivephotoautotrimmingenabled.md)
  A Boolean value that indicates whether to automatically trim Live Photo movie captures to avoid excessive movement.
- [var availableLivePhotoVideoCodecTypes: [AVVideoCodecType]](./availablelivephotovideocodectypes.md)
  An array of video codecs currently available for Live Photo movie captures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/islivephotocapturesupported)*