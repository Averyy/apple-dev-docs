# isLensStabilizationDuringBracketedCaptureSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the capture output supports lens stabilization across the duration of a bracketed capture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isLensStabilizationDuringBracketedCaptureSupported: Bool { get }
```

#### Discussion

You may set the [`isLensStabilizationDuringBracketedCaptureEnabled`](avcapturestillimageoutput/islensstabilizationduringbracketedcaptureenabled.md) property only if this property’s value is [`true`](https://developer.apple.com/documentation/Swift/true). This value may change as the session’s [`sessionPreset`](avcapturesession/sessionpreset.md) property or the input device’s [`activeFormat`](avcapturedevice/activeformat.md) property changes.

This property supports key-value observing.

## See Also

- [func captureStillImageBracketAsynchronously(from: AVCaptureConnection, withSettingsArray: [AVCaptureBracketedStillImageSettings], completionHandler: (CMSampleBuffer?, AVCaptureBracketedStillImageSettings?, (any Error)?) -> Void)](avcapturestillimageoutput/capturestillimagebracketasynchronously(from:withsettingsarray:completionhandler:).md)
  Captures a still image bracket.
- [var maxBracketedCaptureStillImageCount: Int](avcapturestillimageoutput/maxbracketedcapturestillimagecount.md)
  Specifies the maximum number of still images that may be taken in a single bracket.
- [func prepareToCaptureStillImageBracket(from: AVCaptureConnection, withSettingsArray: [AVCaptureBracketedStillImageSettings], completionHandler: (Bool, (any Error)?) -> Void)](avcapturestillimageoutput/preparetocapturestillimagebracket(from:withsettingsarray:completionhandler:).md)
  Allows the receiver to prepare resources in advance of capturing a still image bracket.
- [var isLensStabilizationDuringBracketedCaptureEnabled: Bool](avcapturestillimageoutput/islensstabilizationduringbracketedcaptureenabled.md)
  A Boolean value that specifies whether to stabilize the lens across the duration of a bracketed capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/islensstabilizationduringbracketedcapturesupported)*