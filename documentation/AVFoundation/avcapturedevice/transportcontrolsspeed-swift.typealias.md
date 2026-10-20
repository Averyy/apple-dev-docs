# AVCaptureDevice.TransportControlsSpeed

**Framework**: AVFoundation  
**Kind**: typealias  
**Role**: Type Alias

A constant that specifies speed of transport controls.

**Availability**:
- macOS 10.7+

## Declaration

```swift
typealias TransportControlsSpeed = Float
```

```c
typedef float AVCaptureDeviceTransportControlsSpeed;
```

## See Also

### Controlling transport behavior
- [var transportControlsSupported: Bool](./transportcontrolssupported.md)
  A Boolean value that indicates whether the device supports transport control commands.
- [var transportControlsPlaybackMode: AVCaptureDevice.TransportControlsPlaybackMode](./transportcontrolsplaybackmode-swift.property.md)
  The current playback mode.
- [func setTransportControlsPlaybackMode(AVCaptureDevice.TransportControlsPlaybackMode, speed: AVCaptureDevice.TransportControlsSpeed)](./settransportcontrolsplaybackmode%28_,speed%29.md)
  Sets the transport control’s playback mode and speed.
- [AVCaptureDevice.TransportControlsPlaybackMode](./transportcontrolsplaybackmode-swift.enum.md)
  Constants that indicate the transport control’s current mode of playback, if it has one.
- [var transportControlsSpeed: AVCaptureDevice.TransportControlsSpeed](./transportcontrolsspeed-swift.property.md)
  The current playback speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/transportcontrolsspeed-swift.typealias)*