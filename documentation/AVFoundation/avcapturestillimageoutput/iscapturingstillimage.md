# isCapturingStillImage

**Framework**: AVFoundation  
**Kind**: property

Indicates whether a still image is being captured.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 14.0+
- macOS 10.8+

## Declaration

```swift
var isCapturingStillImage: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when a still image is being captured, and [`false`](https://developer.apple.com/documentation/Swift/false) when no still image capture is underway.

This property supports key-value observing.

## See Also

- [func captureStillImageAsynchronously(from: AVCaptureConnection, completionHandler: (CMSampleBuffer?, (any Error)?) -> Void)](avcapturestillimageoutput/capturestillimageasynchronously(from:completionhandler:).md)
  Initiates a still image capture and returns immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/iscapturingstillimage)*