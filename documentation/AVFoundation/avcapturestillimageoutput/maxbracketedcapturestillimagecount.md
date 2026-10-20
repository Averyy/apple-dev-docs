# maxBracketedCaptureStillImageCount

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Specifies the maximum number of still images that may be taken in a single bracket.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVCapturePhotoOutput maxBracketedCapturePhotoCount instead.

## Declaration

```swift
var maxBracketedCaptureStillImageCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger maxBracketedCaptureStillImageCount;
```

#### Discussion

AVCaptureStillImageOutput can only satisfy a limited number of image requests in a single bracket without exhausting system resources.

The maximum number of still images that may be taken in a single bracket depends on the size of the images being captured, and consequently may vary with AVCaptureSession -sessionPreset and AVCaptureDevice -activeFormat values.

## See Also

### Related Documentation
- [func captureStillImageAsynchronously(from: AVCaptureConnection, completionHandler: (CMSampleBuffer?, (any Error)?) -> Void)](./capturestillimageasynchronously%28from,completionhandler%29.md)
  Initiates a still image capture and returns immediately.
### Still image bracketed capture
- [func captureStillImageBracketAsynchronously(from: AVCaptureConnection, withSettingsArray: [AVCaptureBracketedStillImageSettings], completionHandler: (CMSampleBuffer?, AVCaptureBracketedStillImageSettings?, (any Error)?) -> Void)](./capturestillimagebracketasynchronously%28from,withsettingsarray,completionhandler%29.md)
  Captures a still image bracket.
- [func prepareToCaptureStillImageBracket(from: AVCaptureConnection, withSettingsArray: [AVCaptureBracketedStillImageSettings], completionHandler: (Bool, (any Error)?) -> Void)](./preparetocapturestillimagebracket%28from,withsettingsarray,completionhandler%29.md)
  Allows the receiver to prepare resources in advance of capturing a still image bracket.
- [var isLensStabilizationDuringBracketedCaptureSupported: Bool](./islensstabilizationduringbracketedcapturesupported.md)
  A Boolean value that indicates whether the capture output supports lens stabilization across the duration of a bracketed capture.
- [var isLensStabilizationDuringBracketedCaptureEnabled: Bool](./islensstabilizationduringbracketedcaptureenabled.md)
  A Boolean value that specifies whether to stabilize the lens across the duration of a bracketed capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/maxbracketedcapturestillimagecount)*