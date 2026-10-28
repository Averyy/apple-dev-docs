# isCapturingStillImage

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Indicates whether a still image is being captured.

**Availability**:
- iOS 5.0+ - Deprecated in 10.0
- iPadOS 5.0+ - Deprecated in 10.0
- Mac Catalyst 14.0+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.15

## Declaration

```swift
var isCapturingStillImage: Bool { get }
```

```objc
@property (readonly, getter=isCapturingStillImage) BOOL capturingStillImage;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when a still image is being captured, and [`false`](../../Swift/false.md) when no still image capture is underway.

This property supports key-value observing.

## See Also

### Capturing an image
- [func captureStillImageAsynchronously(from: AVCaptureConnection, completionHandler: (CMSampleBuffer?, (any Error)?) -> Void)](./capturestillimageasynchronously%28from,completionhandler%29.md)
  Initiates a still image capture and returns immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/iscapturingstillimage)*