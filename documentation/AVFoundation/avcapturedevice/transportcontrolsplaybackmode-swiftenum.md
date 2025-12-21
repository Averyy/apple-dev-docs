# AVCaptureDevice.TransportControlsPlaybackMode

**Framework**: AVFoundation  
**Kind**: enum

Constants that indicate the transport control’s current mode of playback, if it has one.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum TransportControlsPlaybackMode
```

## Topics

### Playback modes
- [AVCaptureDevice.TransportControlsPlaybackMode.notPlaying](avcapturedevice/transportcontrolsplaybackmode-swift.enum/notplaying.md)
  A value that indicates that the tape transport isn’t threaded through the play head.
- [AVCaptureDevice.TransportControlsPlaybackMode.playing](avcapturedevice/transportcontrolsplaybackmode-swift.enum/playing.md)
  A value that indicates that the tape transport is threaded through the play head.
### Initializers
- [init?(rawValue: Int)](avcapturedevice/transportcontrolsplaybackmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var transportControlsSupported: Bool](avcapturedevice/transportcontrolssupported.md)
  A Boolean value that indicates whether the device supports transport control commands.
- [var transportControlsPlaybackMode: AVCaptureDevice.TransportControlsPlaybackMode](avcapturedevice/transportcontrolsplaybackmode-swift.property.md)
  The current playback mode.
- [func setTransportControlsPlaybackMode(AVCaptureDevice.TransportControlsPlaybackMode, speed: AVCaptureDevice.TransportControlsSpeed)](avcapturedevice/settransportcontrolsplaybackmode(_:speed:).md)
  Sets the transport control’s playback mode and speed.
- [var transportControlsSpeed: AVCaptureDevice.TransportControlsSpeed](avcapturedevice/transportcontrolsspeed-swift.property.md)
  The current playback speed.
- [AVCaptureDevice.TransportControlsSpeed](avcapturedevice/transportcontrolsspeed-swift.typealias.md)
  A constant that specifies speed of transport controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/transportcontrolsplaybackmode-swift.enum)*