# videoMaxFrameDuration

**Framework**: AVFoundation  
**Kind**: property

The largest time interval the connection can apply between consecutive video frames.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.9+

## Declaration

```swift
var videoMaxFrameDuration: CMTime { get set }
```

#### Discussion

When [`isVideoMaxFrameDurationSupported`](avcaptureconnection/isvideomaxframedurationsupported.md) is [`true`](https://developer.apple.com/documentation/swift/true), the value of the property configures the upper bound for the amount of time a video connection separates consecutive frames. The value is equivalent to the reciprocal of the minimum frame rate.

You can set an unlimited frame rate with [`zero`](https://developer.apple.com/documentation/CoreMedia/CMTime/zero) or [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid) (which is the default).

## See Also

- [var isVideoMinFrameDurationSupported: Bool](avcaptureconnection/isvideominframedurationsupported.md)
  A Boolean value that indicates whether the connection supports a minimum frame duration.
- [var videoMinFrameDuration: CMTime](avcaptureconnection/videominframeduration.md)
  The smallest time interval the connection can apply between consecutive video frames.
- [var isVideoMaxFrameDurationSupported: Bool](avcaptureconnection/isvideomaxframedurationsupported.md)
  A Boolean value that indicates whether the connection supports a maximum frame duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videomaxframeduration)*