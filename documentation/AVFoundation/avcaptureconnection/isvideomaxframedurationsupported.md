# isVideoMaxFrameDurationSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the connection supports a maximum frame duration.

**Availability**:
- Mac Catalyst 14.0+ - Deprecated in 14.0
- macOS 10.9+

> **Deprecated**: Use AVCaptureDevice's activeFormat.videoSupportedFrameRateRanges instead.

## Declaration

```swift
var isVideoMaxFrameDurationSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isVideoMaxFrameDurationSupported) BOOL supportsVideoMaxFrameDuration;
```

## Discussion

The property indicates whether the connection honors the [`videoMaxFrameDuration`](./videomaxframeduration.md) property for a video connection.

## See Also

### Configuring a video’s frame rate
- [var isVideoMinFrameDurationSupported: Bool](./isvideominframedurationsupported.md)
  A Boolean value that indicates whether the connection supports a minimum frame duration.
- [var videoMinFrameDuration: CMTime](./videominframeduration.md)
  The smallest time interval the connection can apply between consecutive video frames.
- [var videoMaxFrameDuration: CMTime](./videomaxframeduration.md)
  The largest time interval the connection can apply between consecutive video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideomaxframedurationsupported)*