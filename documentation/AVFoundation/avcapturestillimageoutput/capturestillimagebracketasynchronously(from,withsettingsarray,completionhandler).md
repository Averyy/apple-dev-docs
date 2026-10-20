# captureStillImageBracketAsynchronously(from:withSettingsArray:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Captures a still image bracket.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVCapturePhotoOutput capturePhotoWithSettings:delegate: instead.

## Declaration

```swift
func captureStillImageBracketAsynchronously(from connection: AVCaptureConnection, withSettingsArray settings: [AVCaptureBracketedStillImageSettings], completionHandler handler: @escaping (CMSampleBuffer?, AVCaptureBracketedStillImageSettings?, (any Error)?) -> Void)
```

```objc
- (void) captureStillImageBracketAsynchronouslyFromConnection:(AVCaptureConnection *) connection withSettingsArray:(NSArray<__kindof AVCaptureBracketedStillImageSettings *> *) settings completionHandler:(void (^)(CMSampleBufferRef sampleBuffer, AVCaptureBracketedStillImageSettings *stillImageSettings, NSError *error)) handler;
```

#### Discussion

If you have not invoked [`prepareToCaptureStillImageBracket(from:withSettingsArray:completionHandler:)`](./preparetocapturestillimagebracket%28from,withsettingsarray,completionhandler%29.md) for this still image bracket request, the bracket may not be taken immediately, as the receiver may internally need to prepare resources.

## Parameters

- `connection`: The connection through which the still image bracket should be captured.
- `settings`: An array of [`AVCaptureBracketedStillImageSettings`](../avcapturebracketedstillimagesettings.md) objects. All the array items must be of the same [`AVCaptureBracketedStillImageSettings`](../avcapturebracketedstillimagesettings.md) subclass, or an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) exception is thrown.
- `handler`: A user provided block that will be called asynchronously as each still image in the bracket is captured.

  The block has three parameters:

  - **sampleBuffer**: If the capture request is successful,  contains a valid CMSampleBuffer.
  - **stillImageSettings**: Contains the [`AVCaptureBracketedStillImageSettings`](../avcapturebracketedstillimagesettings.md) object corresponding to this still image.
  - **error**: If the bracketed capture fails, `sampleBuffer` is `NULL` and error is non-`nil`.

  If the count of the `settings` parameter exceeds [`maxBracketedCaptureStillImageCount`](./maxbracketedcapturestillimagecount.md), then `AVErrorMaximumStillImageCaptureRequestsExceeded` is returned.

  You should not assume that the completion handler will be called on a specific thread.

## See Also

### Related Documentation
- [func captureStillImageAsynchronously(from: AVCaptureConnection, completionHandler: (CMSampleBuffer?, (any Error)?) -> Void)](./capturestillimageasynchronously%28from,completionhandler%29.md)
  Initiates a still image capture and returns immediately.
### Still image bracketed capture
- [var maxBracketedCaptureStillImageCount: Int](./maxbracketedcapturestillimagecount.md)
  Specifies the maximum number of still images that may be taken in a single bracket.
- [func prepareToCaptureStillImageBracket(from: AVCaptureConnection, withSettingsArray: [AVCaptureBracketedStillImageSettings], completionHandler: (Bool, (any Error)?) -> Void)](./preparetocapturestillimagebracket%28from,withsettingsarray,completionhandler%29.md)
  Allows the receiver to prepare resources in advance of capturing a still image bracket.
- [var isLensStabilizationDuringBracketedCaptureSupported: Bool](./islensstabilizationduringbracketedcapturesupported.md)
  A Boolean value that indicates whether the capture output supports lens stabilization across the duration of a bracketed capture.
- [var isLensStabilizationDuringBracketedCaptureEnabled: Bool](./islensstabilizationduringbracketedcaptureenabled.md)
  A Boolean value that specifies whether to stabilize the lens across the duration of a bracketed capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/capturestillimagebracketasynchronously(from:withsettingsarray:completionhandler:))*