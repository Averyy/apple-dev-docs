# prepareToCaptureStillImageBracket(from:withSettingsArray:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Allows the receiver to prepare resources in advance of capturing a still image bracket.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVCapturePhotoOutput setPreparedPhotoSettingsArray:completionHandler: instead.

## Declaration

```swift
func prepareToCaptureStillImageBracket(from connection: AVCaptureConnection, withSettingsArray settings: [AVCaptureBracketedStillImageSettings], completionHandler handler: @escaping (Bool, (any Error)?) -> Void)
```

```objc
- (void) prepareToCaptureStillImageBracketFromConnection:(AVCaptureConnection *) connection withSettingsArray:(NSArray<__kindof AVCaptureBracketedStillImageSettings *> *) settings completionHandler:(void (^)(BOOL prepared, NSError *error)) handler;
```

## Discussion

Before taking a still image bracket, additional resources may need to be allocated. By calling this method first, you are able to know when the receiver is ready to capture the bracket with the specified settings array.

## Parameters

- `connection`: The connection through which the still image bracket should be captured.
- `settings`: An array of [`AVCaptureBracketedStillImageSettings`](../avcapturebracketedstillimagesettings.md) objects. All the array items must be of the same [`AVCaptureBracketedStillImageSettings`](../avcapturebracketedstillimagesettings.md) subclass, or an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) exception is thrown.
- `handler`: A user provided block that will be called asynchronously once resources have successfully been allocated for the specified bracketed capture operation.

  The block has two parameters:

  - **prepared**: If sufficient resources could not be allocated, this parameter is [`false`](../../Swift/false.md), and the `error` parameter contains a non-`nil` error value.
  - **error**: The value is non-`nil` if an error is encountered.

  If the count of the `settings` parameter exceeds [`maxBracketedCaptureStillImageCount`](./maxbracketedcapturestillimagecount.md), then `AVErrorMaximumStillImageCaptureRequestsExceeded` is returned.

  You should not assume that the completion handler will be called on a specific thread.

## See Also

### Related Documentation
- [func captureStillImageAsynchronously(from: AVCaptureConnection, completionHandler: (CMSampleBuffer?, (any Error)?) -> Void)](./capturestillimageasynchronously%28from,completionhandler%29.md)
  Initiates a still image capture and returns immediately.
### Still image bracketed capture
- [func captureStillImageBracketAsynchronously(from: AVCaptureConnection, withSettingsArray: [AVCaptureBracketedStillImageSettings], completionHandler: (CMSampleBuffer?, AVCaptureBracketedStillImageSettings?, (any Error)?) -> Void)](./capturestillimagebracketasynchronously%28from,withsettingsarray,completionhandler%29.md)
  Captures a still image bracket.
- [var maxBracketedCaptureStillImageCount: Int](./maxbracketedcapturestillimagecount.md)
  Specifies the maximum number of still images that may be taken in a single bracket.
- [var isLensStabilizationDuringBracketedCaptureSupported: Bool](./islensstabilizationduringbracketedcapturesupported.md)
  A Boolean value that indicates whether the capture output supports lens stabilization across the duration of a bracketed capture.
- [var isLensStabilizationDuringBracketedCaptureEnabled: Bool](./islensstabilizationduringbracketedcaptureenabled.md)
  A Boolean value that specifies whether to stabilize the lens across the duration of a bracketed capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/preparetocapturestillimagebracket(from:withsettingsarray:completionhandler:))*