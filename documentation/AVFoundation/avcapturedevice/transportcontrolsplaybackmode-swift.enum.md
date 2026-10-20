# AVCaptureDevice.TransportControlsPlaybackMode

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the transport control’s current mode of playback, if it has one.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum TransportControlsPlaybackMode
```

```c
enum AVCaptureDeviceTransportControlsPlaybackMode : NSInteger;
```

## Topics

### Playback modes
- [AVCaptureDevice.TransportControlsPlaybackMode.notPlaying](./transportcontrolsplaybackmode-swift.enum/notplaying.md)
  A value that indicates that the tape transport isn’t threaded through the play head.
- [AVCaptureDevice.TransportControlsPlaybackMode.playing](./transportcontrolsplaybackmode-swift.enum/playing.md)
  A value that indicates that the tape transport is threaded through the play head.
### Initializers
- [init?(rawValue: Int)](./transportcontrolsplaybackmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Controlling transport behavior
- [var transportControlsSupported: Bool](./transportcontrolssupported.md)
  A Boolean value that indicates whether the device supports transport control commands.
- [var transportControlsPlaybackMode: AVCaptureDevice.TransportControlsPlaybackMode](./transportcontrolsplaybackmode-swift.property.md)
  The current playback mode.
- [func setTransportControlsPlaybackMode(AVCaptureDevice.TransportControlsPlaybackMode, speed: AVCaptureDevice.TransportControlsSpeed)](./settransportcontrolsplaybackmode%28_,speed%29.md)
  Sets the transport control’s playback mode and speed.
- [var transportControlsSpeed: AVCaptureDevice.TransportControlsSpeed](./transportcontrolsspeed-swift.property.md)
  The current playback speed.
- [AVCaptureDevice.TransportControlsSpeed](./transportcontrolsspeed-swift.typealias.md)
  A constant that specifies speed of transport controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/transportcontrolsplaybackmode-swift.enum)*