# isLensStabilizationDuringBracketedCaptureSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the capture output supports lens stabilization across the duration of a bracketed capture.

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVCapturePhotoOutput lensStabilizationDuringBracketedCaptureSupported instead.

## Declaration

```swift
var isLensStabilizationDuringBracketedCaptureSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isLensStabilizationDuringBracketedCaptureSupported) BOOL lensStabilizationDuringBracketedCaptureSupported;
```

## Discussion

You may set the [`isLensStabilizationDuringBracketedCaptureEnabled`](./islensstabilizationduringbracketedcaptureenabled.md) property only if this property’s value is [`true`](../../Swift/true.md). This value may change as the session’s [`sessionPreset`](../avcapturesession/sessionpreset.md) property or the input device’s [`activeFormat`](../avcapturedevice/activeformat.md) property changes.

This property supports key-value observing.

## See Also

### Still image bracketed capture
- [func captureStillImageBracketAsynchronously(from: AVCaptureConnection, withSettingsArray: [AVCaptureBracketedStillImageSettings], completionHandler: (CMSampleBuffer?, AVCaptureBracketedStillImageSettings?, (any Error)?) -> Void)](./capturestillimagebracketasynchronously%28from,withsettingsarray,completionhandler%29.md)
  Captures a still image bracket.
- [var maxBracketedCaptureStillImageCount: Int](./maxbracketedcapturestillimagecount.md)
  Specifies the maximum number of still images that may be taken in a single bracket.
- [func prepareToCaptureStillImageBracket(from: AVCaptureConnection, withSettingsArray: [AVCaptureBracketedStillImageSettings], completionHandler: (Bool, (any Error)?) -> Void)](./preparetocapturestillimagebracket%28from,withsettingsarray,completionhandler%29.md)
  Allows the receiver to prepare resources in advance of capturing a still image bracket.
- [var isLensStabilizationDuringBracketedCaptureEnabled: Bool](./islensstabilizationduringbracketedcaptureenabled.md)
  A Boolean value that specifies whether to stabilize the lens across the duration of a bracketed capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/islensstabilizationduringbracketedcapturesupported)*