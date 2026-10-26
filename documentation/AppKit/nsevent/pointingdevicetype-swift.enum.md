# NSEvent.PointingDeviceType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The pointing-device types for tablet-proximity events or mouse events with a proximity event subtype.

**Availability**:
- macOS

## Declaration

```swift
enum PointingDeviceType
```

```c
enum NSPointingDeviceType : NSUInteger;
```

#### Overview

The [`pointingDeviceType`](./pointingdevicetype-swift.property.md) property returns one of these constants.

## Topics

### Enumeration Cases
- [NSEvent.PointingDeviceType.cursor](./pointingdevicetype-swift.enum/cursor.md)
  Represents a cursor pointing device.
- [NSEvent.PointingDeviceType.eraser](./pointingdevicetype-swift.enum/eraser.md)
  Represents the eraser end of a stylus-like pointing device.
- [NSEvent.PointingDeviceType.pen](./pointingdevicetype-swift.enum/pen.md)
  Represents the tip end of a stylus-like pointing device.
- [NSEvent.PointingDeviceType.unknown](./pointingdevicetype-swift.enum/unknown.md)
  Represents an unknown type of pointing device.
### Initializers
- [init?(rawValue: UInt)](./pointingdevicetype-swift.enum/init%28rawvalue%29.md)
### Deprecated
- [NSCursorPointingDevice](../nscursorpointingdevice.md)
  Represents a cursor (or puck-like) pointing device.
- [NSEraserPointingDevice](../nseraserpointingdevice.md)
  Represents the eraser end of a stylus-like pointing device.
- [NSPenPointingDevice](../nspenpointingdevice.md)
  Represents the tip end of a stylus-like pointing device.
- [NSUnknownPointingDevice](../nsunknownpointingdevice.md)
  Represents an unknown type of pointing device.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting tablet proximity information
- [var capabilityMask: Int](./capabilitymask.md)
  A mask that indicates the capabilities of the tablet device that generated this event.
- [var deviceID: Int](./deviceid.md)
  A special identifier the system matches against tablet-pointer and tablet-proximity events.
- [var isEnteringProximity: Bool](./isenteringproximity.md)
  A Boolean value that indicates whether a pointing device is entering or leaving the proximity of its tablet.
- [var pointingDeviceID: Int](./pointingdeviceid.md)
  The index of the pointing device currently in proximity with the tablet.
- [var pointingDeviceSerialNumber: Int](./pointingdeviceserialnumber.md)
  The vendor-assigned serial number of a pointing device.
- [var pointingDeviceType: NSEvent.PointingDeviceType](./pointingdevicetype-swift.property.md)
  The kind of pointing device associated with this event.
- [var systemTabletID: Int](./systemtabletid.md)
  The index of the tablet device connected to the system.
- [var tabletID: Int](./tabletid.md)
  The USB model identifier of the tablet device associated with this event.
- [var uniqueID: UInt64](./uniqueid.md)
  The unique identifier of the pointing device that generated this event.
- [var vendorID: Int](./vendorid.md)
  The vendor identifier of the tablet associated with the event.
- [var vendorPointingDeviceType: Int](./vendorpointingdevicetype.md)
  A coded bit field whose set bits indicate the type of pointing device (within a vendor selection) associated with the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/pointingdevicetype-swift.enum)*