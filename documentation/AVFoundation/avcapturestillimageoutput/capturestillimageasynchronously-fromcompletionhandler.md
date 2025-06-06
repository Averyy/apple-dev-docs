# captureStillImageAsynchronously(from:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Initiates a still image capture and returns immediately.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func captureStillImageAsynchronously(from connection: AVCaptureConnection, completionHandler handler: @escaping (CMSampleBuffer?, (any Error)?) -> Void)
```

#### Discussion

This method returns immediately after it is invoked, later calling the provided completion handler block when image data is ready. If the request could not be completed, the error parameter will contain an `NSError` object describing the failure.

You should not assume that the completion handler will be called on a specific thread.

## Parameters

- `connection`: The connection from which to capture the image.
- `handler`: The buffer attachments may contain metadata appropriate to the image data format. For example, a buffer containing JPEG data may carry a   as an attachment. See ImageIO/CGImageProperties.h for a list of keys and value types.

## See Also

- [var isCapturingStillImage: Bool](avcapturestillimageoutput/iscapturingstillimage.md)
  Indicates whether a still image is being captured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/capturestillimageasynchronously(from:completionhandler:))*