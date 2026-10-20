# AVCaptureInput.Port

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVCaptureInputPort : NSObject
```

#### Overview

Instances of [`AVCaptureInput`](../avcaptureinput.md) have one or more input ports, one for each data stream they can produce. For example, an [`AVCaptureDeviceInput`](../avcapturedeviceinput.md) object presenting one video data stream has one port.

## Topics

### Inspecting an input port
- [var isEnabled: Bool](./port/isenabled.md)
  A Boolean value that indicates whether the port is in an enabled state.
- [var mediaType: AVMediaType](./port/mediatype.md)
  The media type of the port.
- [var formatDescription: CMFormatDescription?](./port/formatdescription.md)
  A description of the port format.
- [var sourceDeviceType: AVCaptureDevice.DeviceType?](./port/sourcedevicetype.md)
  The device type of the source camera that provides data to the port.
- [var sourceDevicePosition: AVCaptureDevice.Position](./port/sourcedeviceposition.md)
  The position of the source device providing input through this port.
- [var clock: CMClock?](./port/clock.md)
  An object that represents the capture device’s clock.
### Observing format changes
- [class let formatDescriptionDidChangeNotification: NSNotification.Name](./port/formatdescriptiondidchangenotification.md)
  A notification the system posts when the capture input port’s format description changes.
### Accessing the input
- [var input: AVCaptureInput](./port/input.md)
  The input object that owns the port.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Accessing ports
- [var ports: [AVCaptureInput.Port]](./ports.md)
  The ports available on a capture input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureinput/port)*