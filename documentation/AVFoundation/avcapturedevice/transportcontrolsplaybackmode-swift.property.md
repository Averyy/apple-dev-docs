# transportControlsPlaybackMode

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The current playback mode.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var transportControlsPlaybackMode: AVCaptureDevice.TransportControlsPlaybackMode { get }
```

```objc
@property (nonatomic, readonly) AVCaptureDeviceTransportControlsPlaybackMode transportControlsPlaybackMode;
```

## Discussion

For devices that support transport control, query this property to discover the current playback mode.

## See Also

### Controlling transport behavior
- [var transportControlsSupported: Bool](./transportcontrolssupported.md)
  A Boolean value that indicates whether the device supports transport control commands.
- [func setTransportControlsPlaybackMode(AVCaptureDevice.TransportControlsPlaybackMode, speed: AVCaptureDevice.TransportControlsSpeed)](./settransportcontrolsplaybackmode%28_,speed%29.md)
  Sets the transport control’s playback mode and speed.
- [AVCaptureDevice.TransportControlsPlaybackMode](./transportcontrolsplaybackmode-swift.enum.md)
  Constants that indicate the transport control’s current mode of playback, if it has one.
- [var transportControlsSpeed: AVCaptureDevice.TransportControlsSpeed](./transportcontrolsspeed-swift.property.md)
  The current playback speed.
- [AVCaptureDevice.TransportControlsSpeed](./transportcontrolsspeed-swift.typealias.md)
  A constant that specifies speed of transport controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/transportcontrolsplaybackmode-swift.property)*