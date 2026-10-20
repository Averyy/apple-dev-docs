# videoMinFrameDuration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The smallest time interval the connection can apply between consecutive video frames.

**Availability**:
- Mac Catalyst 14.0+ - Deprecated in 14.0
- macOS 10.7+

> **Deprecated**: Use AVCaptureDevice's activeVideoMinFrameDuration instead.

## Declaration

```swift
var videoMinFrameDuration: CMTime { get set }
```

```objc
@property (nonatomic) CMTime videoMinFrameDuration;
```

#### Discussion

When [`isVideoMinFrameDurationSupported`](./isvideominframedurationsupported.md) is [`true`](../../Swift/true.md), the value of the property configures the lower bound for the amount of time a video connection separates consecutive frames. The value is equivalent to the reciprocal of the minimum frame rate.

You can set an unlimited frame rate with [`zero`](../../CoreMedia/cmtime/zero.md) or [`invalid`](../../CoreMedia/cmtime/invalid.md) (which is the default).

## See Also

### Configuring a video’s frame rate
- [var isVideoMinFrameDurationSupported: Bool](./isvideominframedurationsupported.md)
  A Boolean value that indicates whether the connection supports a minimum frame duration.
- [var isVideoMaxFrameDurationSupported: Bool](./isvideomaxframedurationsupported.md)
  A Boolean value that indicates whether the connection supports a maximum frame duration.
- [var videoMaxFrameDuration: CMTime](./videomaxframeduration.md)
  The largest time interval the connection can apply between consecutive video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videominframeduration)*