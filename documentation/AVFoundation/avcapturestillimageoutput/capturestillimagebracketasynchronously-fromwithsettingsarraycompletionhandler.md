# captureStillImageBracketAsynchronously(from:withSettingsArray:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Captures a still image bracket.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func captureStillImageBracketAsynchronously(from connection: AVCaptureConnection, withSettingsArray settings: [AVCaptureBracketedStillImageSettings], completionHandler handler: @escaping (CMSampleBuffer?, AVCaptureBracketedStillImageSettings?, (any Error)?) -> Void)
```

#### Discussion

If you have not invoked [`prepareToCaptureStillImageBracket(from:withSettingsArray:completionHandler:)`](avcapturestillimageoutput/preparetocapturestillimagebracket(from:withsettingsarray:completionhandler:).md) for this still image bracket request, the bracket may not be taken immediately, as the receiver may internally need to prepare resources.

## Parameters

- `connection`: The connection through which the still image bracket should be captured.
- `settings`: An array of   objects. All the array items must be of the same   subclass, or an   exception is thrown.
- `handler`: You should not assume that the completion handler will be called on a specific thread.

## See Also

- [func captureStillImageAsynchronously(from: AVCaptureConnection, completionHandler: (CMSampleBuffer?, (any Error)?) -> Void)](avcapturestillimageoutput/capturestillimageasynchronously(from:completionhandler:).md)
  Initiates a still image capture and returns immediately.
- [var maxBracketedCaptureStillImageCount: Int](avcapturestillimageoutput/maxbracketedcapturestillimagecount.md)
  Specifies the maximum number of still images that may be taken in a single bracket.
- [func prepareToCaptureStillImageBracket(from: AVCaptureConnection, withSettingsArray: [AVCaptureBracketedStillImageSettings], completionHandler: (Bool, (any Error)?) -> Void)](avcapturestillimageoutput/preparetocapturestillimagebracket(from:withsettingsarray:completionhandler:).md)
  Allows the receiver to prepare resources in advance of capturing a still image bracket.
- [var isLensStabilizationDuringBracketedCaptureSupported: Bool](avcapturestillimageoutput/islensstabilizationduringbracketedcapturesupported.md)
  A Boolean value that indicates whether the capture output supports lens stabilization across the duration of a bracketed capture.
- [var isLensStabilizationDuringBracketedCaptureEnabled: Bool](avcapturestillimageoutput/islensstabilizationduringbracketedcaptureenabled.md)
  A Boolean value that specifies whether to stabilize the lens across the duration of a bracketed capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/capturestillimagebracketasynchronously(from:withsettingsarray:completionhandler:))*