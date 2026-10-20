# videoMaxFrameDuration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The largest time interval the connection can apply between consecutive video frames.

**Availability**:
- Mac Catalyst 14.0+ - Deprecated in 14.0
- macOS 10.9+

> **Deprecated**: Use AVCaptureDevice's activeVideoMaxFrameDuration instead.

## Declaration

```swift
var videoMaxFrameDuration: CMTime { get set }
```

```objc
@property (nonatomic) CMTime videoMaxFrameDuration;
```

#### Discussion

When [`isVideoMaxFrameDurationSupported`](./isvideomaxframedurationsupported.md) is [`true`](../../Swift/true.md), the value of the property configures the upper bound for the amount of time a video connection separates consecutive frames. The value is equivalent to the reciprocal of the minimum frame rate.

You can set an unlimited frame rate with [`zero`](../../CoreMedia/cmtime/zero.md) or [`invalid`](../../CoreMedia/cmtime/invalid.md) (which is the default).

## See Also

### Configuring a video’s frame rate
- [var isVideoMinFrameDurationSupported: Bool](./isvideominframedurationsupported.md)
  A Boolean value that indicates whether the connection supports a minimum frame duration.
- [var videoMinFrameDuration: CMTime](./videominframeduration.md)
  The smallest time interval the connection can apply between consecutive video frames.
- [var isVideoMaxFrameDurationSupported: Bool](./isvideomaxframedurationsupported.md)
  A Boolean value that indicates whether the connection supports a maximum frame duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videomaxframeduration)*