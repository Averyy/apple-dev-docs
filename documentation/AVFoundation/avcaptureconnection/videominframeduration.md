# videoMinFrameDuration

**Framework**: AVFoundation  
**Kind**: property

The smallest time interval the connection can apply between consecutive video frames.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.7+

## Declaration

```swift
var videoMinFrameDuration: CMTime { get set }
```

#### Discussion

When [`isVideoMinFrameDurationSupported`](avcaptureconnection/isvideominframedurationsupported.md) is [`true`](https://developer.apple.com/documentation/Swift/true), the value of the property configures the lower bound for the amount of time a video connection separates consecutive frames. The value is equivalent to the reciprocal of the minimum frame rate.

You can set an unlimited frame rate with [`zero`](https://developer.apple.com/documentation/CoreMedia/CMTime/zero) or [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTime/invalid) (which is the default).

## See Also

- [var isVideoMinFrameDurationSupported: Bool](avcaptureconnection/isvideominframedurationsupported.md)
  A Boolean value that indicates whether the connection supports a minimum frame duration.
- [var isVideoMaxFrameDurationSupported: Bool](avcaptureconnection/isvideomaxframedurationsupported.md)
  A Boolean value that indicates whether the connection supports a maximum frame duration.
- [var videoMaxFrameDuration: CMTime](avcaptureconnection/videomaxframeduration.md)
  The largest time interval the connection can apply between consecutive video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videominframeduration)*