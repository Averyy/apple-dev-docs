# transportControlsSpeed

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The current playback speed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var transportControlsSpeed: AVCaptureDevice.TransportControlsSpeed { get }
```

```objc
@property (nonatomic, readonly) AVCaptureDeviceTransportControlsSpeed transportControlsSpeed;
```

## Discussion

For devices that support transport control, the value of this property indicates the current playback speed of the deck. The following table gives examples of the meaning of values:

| Value | Meaning |
| --- | --- |
| 0.0 | Stopped |
| 1.0 | Forward at normal speed. |
| -1.0 | Reverse at normal speed. |
| 2.0 | Forward at 2x normal speed. |

This property is key-value observable.

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
- [AVCaptureDevice.TransportControlsSpeed](./transportcontrolsspeed-swift.typealias.md)
  A constant that specifies speed of transport controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/transportcontrolsspeed-swift.property)*