# isVideoMinFrameDurationSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the connection supports a minimum frame duration.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.7+

## Declaration

```swift
var isVideoMinFrameDurationSupported: Bool { get }
```

#### Discussion

The property indicates whether the connection honors the [`videoMinFrameDuration`](avcaptureconnection/videominframeduration.md) property for a video connection.

## See Also

- [var videoMinFrameDuration: CMTime](avcaptureconnection/videominframeduration.md)
  The smallest time interval the connection can apply between consecutive video frames.
- [var isVideoMaxFrameDurationSupported: Bool](avcaptureconnection/isvideomaxframedurationsupported.md)
  A Boolean value that indicates whether the connection supports a maximum frame duration.
- [var videoMaxFrameDuration: CMTime](avcaptureconnection/videomaxframeduration.md)
  The largest time interval the connection can apply between consecutive video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideominframedurationsupported)*