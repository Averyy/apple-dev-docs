# macOS Capture Features

**Framework**: AVFoundation

Control the transport behavior and input sources of capture hardware in macOS.

## Topics

### Controlling Transport Behavior
- [var transportControlsSupported: Bool](avcapturedevice/transportcontrolssupported.md)
  A Boolean value that indicates whether the device supports transport control commands.
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
### Configuring Input Sources
- [var inputSources: [AVCaptureDevice.InputSource]](avcapturedevice/inputsources.md)
  An array of input sources that the device supports.
- [var activeInputSource: AVCaptureDevice.InputSource?](avcapturedevice/activeinputsource.md)
  The currently active input source of the device.
- [AVCaptureDevice.InputSource](avcapturedevice/inputsource.md)
  A distinct input source on a capture device.
### Accessing Linked Devices
- [var linkedDevices: [AVCaptureDevice]](avcapturedevice/linkeddevices.md)
  An array of capture devices that are physically linked to a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/macos-capture-features)*