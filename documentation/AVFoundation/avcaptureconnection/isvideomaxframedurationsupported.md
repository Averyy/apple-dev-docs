# isVideoMaxFrameDurationSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the connection supports a maximum frame duration.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.9+

## Declaration

```swift
var isVideoMaxFrameDurationSupported: Bool { get }
```

#### Discussion

The property indicates whether the connection honors the [`videoMaxFrameDuration`](avcaptureconnection/videomaxframeduration.md) property for a video connection.

## See Also

- [var isVideoMinFrameDurationSupported: Bool](avcaptureconnection/isvideominframedurationsupported.md)
  A Boolean value that indicates whether the connection supports a minimum frame duration.
- [var videoMinFrameDuration: CMTime](avcaptureconnection/videominframeduration.md)
  The smallest time interval the connection can apply between consecutive video frames.
- [var videoMaxFrameDuration: CMTime](avcaptureconnection/videomaxframeduration.md)
  The largest time interval the connection can apply between consecutive video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideomaxframedurationsupported)*