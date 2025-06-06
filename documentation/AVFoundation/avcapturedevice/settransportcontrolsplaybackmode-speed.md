# setTransportControlsPlaybackMode(_:speed:)

**Framework**: AVFoundation  
**Kind**: method

Sets the transport control’s playback mode and speed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func setTransportControlsPlaybackMode(_ mode: AVCaptureDevice.TransportControlsPlaybackMode, speed: AVCaptureDevice.TransportControlsSpeed)
```

#### Discussion

Before changing the value of this property, you must call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) to acquire exclusive access to the device’s configuration properties. Otherwise, calling this method raises an exception. When you’re finished configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock and allow other devices to configure the settings.

## Parameters

- `mode`: A playback mode constant that indicates whether to put the deck should into play mode.
- `speed`: The speed at which to wind or play the tape.

## See Also

- [var transportControlsSupported: Bool](avcapturedevice/transportcontrolssupported.md)
  A Boolean value that indicates whether the device supports transport control commands.
- [var transportControlsPlaybackMode: AVCaptureDevice.TransportControlsPlaybackMode](avcapturedevice/transportcontrolsplaybackmode-swift.property.md)
  The current playback mode.
- [AVCaptureDevice.TransportControlsPlaybackMode](avcapturedevice/transportcontrolsplaybackmode-swift.enum.md)
  Constants that indicate the transport control’s current mode of playback, if it has one.
- [var transportControlsSpeed: AVCaptureDevice.TransportControlsSpeed](avcapturedevice/transportcontrolsspeed-swift.property.md)
  The current playback speed.
- [AVCaptureDevice.TransportControlsSpeed](avcapturedevice/transportcontrolsspeed-swift.typealias.md)
  A constant that specifies speed of transport controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/settransportcontrolsplaybackmode(_:speed:))*