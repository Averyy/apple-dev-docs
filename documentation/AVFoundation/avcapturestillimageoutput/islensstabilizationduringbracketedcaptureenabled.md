# isLensStabilizationDuringBracketedCaptureEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that specifies whether to stabilize the lens across the duration of a bracketed capture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isLensStabilizationDuringBracketedCaptureEnabled: Bool { get set }
```

#### Discussion

Applying lens stabilization to bracketed capture attempts to keep the lens steady for the entire duration of the bracket, resulting in more consistent images across the bracket. When lens stabilization is enabled, bracketed still image captures incur additional latency. Lens stabilization is more effective with longer-exposure captures, and offers limited or no benefit for exposure durations shorter than 1/30 of a second. It is possible that during the bracket, the lens stabilization module may run out of correction range and therefore will not be active for every frame in the bracket. Each emitted sample buffer from the bracket has an attachment of `kCMSampleBufferAttachmentKey_StillImageLensStabilizationInfo` indicating additional information about stabilization applied to the buffer.

This property’s default value is [`false`](https://developer.apple.com/documentation/swift/false). You may set this property’s value to [`true`](https://developer.apple.com/documentation/swift/true) only if the [`isLensStabilizationDuringBracketedCaptureSupported`](avcapturestillimageoutput/islensstabilizationduringbracketedcapturesupported.md) value is [`true`](https://developer.apple.com/documentation/swift/true). Otherwise, setting this property raises an exception ([`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException)). If the [`isLensStabilizationDuringBracketedCaptureSupported`](avcapturestillimageoutput/islensstabilizationduringbracketedcapturesupported.md) property’s value changes to [`false`](https://developer.apple.com/documentation/swift/false), this property’s value also becomes [`false`](https://developer.apple.com/documentation/swift/false).

This property supports key-value observing.

## See Also

- [func captureStillImageBracketAsynchronously(from: AVCaptureConnection, withSettingsArray: [AVCaptureBracketedStillImageSettings], completionHandler: (CMSampleBuffer?, AVCaptureBracketedStillImageSettings?, (any Error)?) -> Void)](avcapturestillimageoutput/capturestillimagebracketasynchronously(from:withsettingsarray:completionhandler:).md)
  Captures a still image bracket.
- [var maxBracketedCaptureStillImageCount: Int](avcapturestillimageoutput/maxbracketedcapturestillimagecount.md)
  Specifies the maximum number of still images that may be taken in a single bracket.
- [func prepareToCaptureStillImageBracket(from: AVCaptureConnection, withSettingsArray: [AVCaptureBracketedStillImageSettings], completionHandler: (Bool, (any Error)?) -> Void)](avcapturestillimageoutput/preparetocapturestillimagebracket(from:withsettingsarray:completionhandler:).md)
  Allows the receiver to prepare resources in advance of capturing a still image bracket.
- [var isLensStabilizationDuringBracketedCaptureSupported: Bool](avcapturestillimageoutput/islensstabilizationduringbracketedcapturesupported.md)
  A Boolean value that indicates whether the capture output supports lens stabilization across the duration of a bracketed capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/islensstabilizationduringbracketedcaptureenabled)*