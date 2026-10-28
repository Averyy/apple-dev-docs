# isLensStabilizationDuringBracketedCaptureEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether to stabilize the lens across the duration of a bracketed capture.

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVCapturePhotoOutput with AVCapturePhotoBracketSettings instead.

## Declaration

```swift
var isLensStabilizationDuringBracketedCaptureEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isLensStabilizationDuringBracketedCaptureEnabled) BOOL lensStabilizationDuringBracketedCaptureEnabled;
```

## Discussion

Applying lens stabilization to bracketed capture attempts to keep the lens steady for the entire duration of the bracket, resulting in more consistent images across the bracket. When lens stabilization is enabled, bracketed still image captures incur additional latency. Lens stabilization is more effective with longer-exposure captures, and offers limited or no benefit for exposure durations shorter than 1/30 of a second. It is possible that during the bracket, the lens stabilization module may run out of correction range and therefore will not be active for every frame in the bracket. Each emitted sample buffer from the bracket has an attachment of `kCMSampleBufferAttachmentKey_StillImageLensStabilizationInfo` indicating additional information about stabilization applied to the buffer.

This property’s default value is [`false`](../../Swift/false.md). You may set this property’s value to [`true`](../../Swift/true.md) only if the [`isLensStabilizationDuringBracketedCaptureSupported`](./islensstabilizationduringbracketedcapturesupported.md) value is [`true`](../../Swift/true.md). Otherwise, setting this property raises an exception ([`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md)). If the [`isLensStabilizationDuringBracketedCaptureSupported`](./islensstabilizationduringbracketedcapturesupported.md) property’s value changes to [`false`](../../Swift/false.md), this property’s value also becomes [`false`](../../Swift/false.md).

This property supports key-value observing.

## See Also

### Still image bracketed capture
- [func captureStillImageBracketAsynchronously(from: AVCaptureConnection, withSettingsArray: [AVCaptureBracketedStillImageSettings], completionHandler: (CMSampleBuffer?, AVCaptureBracketedStillImageSettings?, (any Error)?) -> Void)](./capturestillimagebracketasynchronously%28from,withsettingsarray,completionhandler%29.md)
  Captures a still image bracket.
- [var maxBracketedCaptureStillImageCount: Int](./maxbracketedcapturestillimagecount.md)
  Specifies the maximum number of still images that may be taken in a single bracket.
- [func prepareToCaptureStillImageBracket(from: AVCaptureConnection, withSettingsArray: [AVCaptureBracketedStillImageSettings], completionHandler: (Bool, (any Error)?) -> Void)](./preparetocapturestillimagebracket%28from,withsettingsarray,completionhandler%29.md)
  Allows the receiver to prepare resources in advance of capturing a still image bracket.
- [var isLensStabilizationDuringBracketedCaptureSupported: Bool](./islensstabilizationduringbracketedcapturesupported.md)
  A Boolean value that indicates whether the capture output supports lens stabilization across the duration of a bracketed capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/islensstabilizationduringbracketedcaptureenabled)*