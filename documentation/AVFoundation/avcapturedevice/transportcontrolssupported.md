# transportControlsSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the device supports transport control commands.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var transportControlsSupported: Bool { get }
```

#### Discussion

For devices with transport controls, such as AVC tape-based camcorders or pro capture devices with RS422 deck control, the value of this property is [`true`](https://developer.apple.com/documentation/swift/true). If transport controls aren’t supported, none of the associated transport control methods and properties are available to the device.

This property is key-value observable.

## See Also

- [var transportControlsPlaybackMode: AVCaptureDevice.TransportControlsPlaybackMode](avcapturedevice/transportcontrolsplaybackmode-swift.property.md)
  The current playback mode.
- [func setTransportControlsPlaybackMode(AVCaptureDevice.TransportControlsPlaybackMode, speed: AVCaptureDevice.TransportControlsSpeed)](avcapturedevice/settransportcontrolsplaybackmode(_:speed:).md)
  Sets the transport control’s playback mode and speed.
- [AVCaptureDevice.TransportControlsPlaybackMode](avcapturedevice/transportcontrolsplaybackmode-swift.enum.md)
  Constants that indicate the transport control’s current mode of playback, if it has one.
- [var transportControlsSpeed: AVCaptureDevice.TransportControlsSpeed](avcapturedevice/transportcontrolsspeed-swift.property.md)
  The current playback speed.
- [AVCaptureDevice.TransportControlsSpeed](avcapturedevice/transportcontrolsspeed-swift.typealias.md)
  A constant that specifies speed of transport controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/transportcontrolssupported)*