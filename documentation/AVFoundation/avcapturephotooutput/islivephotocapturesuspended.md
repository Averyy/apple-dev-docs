# isLivePhotoCaptureSuspended

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, getter=isLivePhotoCaptureSuspended) BOOL livePhotoCaptureSuspended;
```

#### Discussion

By default, this property’s value is [`false`](../../Swift/false.md). Set this value to [`true`](../../Swift/true.md) to stop any current Live Photo movie captures in progress. Doing this prevents recording additional actions in the Live Photo movie. For example, if you want to capture a still photo that makes a shutter sound, you can prevent recording that action.

When you change this value to [`true`](../../Swift/true.md), the system trims any Live Photo movie captures in progress to the current time. Likewise, when you change this value from [`true`](../../Swift/true.md) to [`false`](../../Swift/false.md), subsequent Live Photo movie captures won’t contain any earlier recordings.

By default, this property resets to [`false`](../../Swift/false.md) when the [`AVCaptureSession`](../avcapturesession.md) stops. You can prevent this behavior by setting [`preservesLivePhotoCaptureSuspendedOnSessionStop`](./preserveslivephotocapturesuspendedonsessionstop.md) to [`true`](../../Swift/true.md) before stopping the session.

> ❗ **Important**:  Setting this property to [`true`](../../Swift/true.md) throws an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) if the [`isLivePhotoCaptureEnabled`](./islivephotocaptureenabled.md) property’s value is [`false`](../../Swift/false.md).

## See Also

### Configuring Live Photo capture
- [var isLivePhotoCaptureSupported: Bool](./islivephotocapturesupported.md)
  A Boolean value that indicates whether the capture output currently supports Live Photo capture.
- [var isLivePhotoCaptureEnabled: Bool](./islivephotocaptureenabled.md)
  A Boolean value that indicates whether to configure the capture pipeline for Live Photo capture.
- [var preservesLivePhotoCaptureSuspendedOnSessionStop: Bool](./preserveslivephotocapturesuspendedonsessionstop.md)
  A Boolean value that indicates whether to preserve the suspended state of Live Photo capture when the session stops.
- [var isLivePhotoAutoTrimmingEnabled: Bool](./islivephotoautotrimmingenabled.md)
  A Boolean value that indicates whether to automatically trim Live Photo movie captures to avoid excessive movement.
- [var availableLivePhotoVideoCodecTypes: [AVVideoCodecType]](./availablelivephotovideocodectypes.md)
  An array of video codecs currently available for Live Photo movie captures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/islivephotocapturesuspended)*