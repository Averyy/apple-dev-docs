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
- `settings`: An array of [`AVCaptureBracketedStillImageSettings`](avcapturebracketedstillimagesettings.md) objects. All the array items must be of the same [`AVCaptureBracketedStillImageSettings`](avcapturebracketedstillimagesettings.md) subclass, or an [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException) exception is thrown.
- `handler`: A user provided block that will be called asynchronously as each still image in the bracket is captured. The block has three parameters: - **sampleBuffer**: If the capture request is successful,  contains a valid CMSampleBuffer.
- **stillImageSettings**: Contains the [`AVCaptureBracketedStillImageSettings`](avcapturebracketedstillimagesettings.md) object corresponding to this still image.
- **error**: If the bracketed capture fails, `sampleBuffer` is `NULL` and error is non-`nil`. If the count of the `settings` parameter exceeds [`maxBracketedCaptureStillImageCount`](avcapturestillimageoutput/maxbracketedcapturestillimagecount.md), then `AVErrorMaximumStillImageCaptureRequestsExceeded` is returned. You should not assume that the completion handler will be called on a specific thread.

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