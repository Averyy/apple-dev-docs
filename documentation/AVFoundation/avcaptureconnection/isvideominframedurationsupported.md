# isVideoMinFrameDurationSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the connection supports a minimum frame duration.

**Availability**:
- Mac Catalyst 14.0+ - Deprecated in 14.0
- macOS 10.7+

> **Deprecated**: Use AVCaptureDevice's activeFormat.videoSupportedFrameRateRanges instead.

## Declaration

```swift
var isVideoMinFrameDurationSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isVideoMinFrameDurationSupported) BOOL supportsVideoMinFrameDuration;
```

#### Discussion

The property indicates whether the connection honors the [`videoMinFrameDuration`](./videominframeduration.md) property for a video connection.

## See Also

### Configuring a video’s frame rate
- [var videoMinFrameDuration: CMTime](./videominframeduration.md)
  The smallest time interval the connection can apply between consecutive video frames.
- [var isVideoMaxFrameDurationSupported: Bool](./isvideomaxframedurationsupported.md)
  A Boolean value that indicates whether the connection supports a maximum frame duration.
- [var videoMaxFrameDuration: CMTime](./videomaxframeduration.md)
  The largest time interval the connection can apply between consecutive video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideominframedurationsupported)*