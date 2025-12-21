# AVCaptureInput.Port

**Framework**: AVFoundation  
**Kind**: class

An object that represents a stream of data that a capture input provides.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
class Port
```

#### Overview

Instances of [`AVCaptureInput`](avcaptureinput.md) have one or more input ports, one for each data stream they can produce. For example, an [`AVCaptureDeviceInput`](avcapturedeviceinput.md) object presenting one video data stream has one port.

## Topics

### Inspecting an input port
- [var isEnabled: Bool](avcaptureinput/port/isenabled.md)
  A Boolean value that indicates whether the port is in an enabled state.
- [var mediaType: AVMediaType](avcaptureinput/port/mediatype.md)
  The media type of the port.
- [var formatDescription: CMFormatDescription?](avcaptureinput/port/formatdescription.md)
  A description of the port format.
- [var sourceDeviceType: AVCaptureDevice.DeviceType?](avcaptureinput/port/sourcedevicetype.md)
  The device type of the source camera that provides data to the port.
- [var sourceDevicePosition: AVCaptureDevice.Position](avcaptureinput/port/sourcedeviceposition.md)
  The position of the source device providing input through this port.
- [var clock: CMClock?](avcaptureinput/port/clock.md)
  An object that represents the capture device’s clock.
### Observing format changes
- [class let formatDescriptionDidChangeNotification: NSNotification.Name](avcaptureinput/port/formatdescriptiondidchangenotification.md)
  A notification the system posts when the capture input port’s format description changes.
### Accessing the input
- [var input: AVCaptureInput](avcaptureinput/port/input.md)
  The input object that owns the port.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var ports: [AVCaptureInput.Port]](avcaptureinput/ports.md)
  The ports available on a capture input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureinput/port)*