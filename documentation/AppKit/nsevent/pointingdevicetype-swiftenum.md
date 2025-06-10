# NSEvent.PointingDeviceType

**Framework**: AppKit  
**Kind**: enum

The pointing-device types for tablet-proximity events or mouse events with a proximity event subtype.

**Availability**:
- macOS ?+

## Declaration

```swift
enum PointingDeviceType
```

#### Overview

The [`pointingDeviceType`](nsevent/pointingdevicetype-swift.property.md) property returns one of these constants.

## Topics

### Enumeration Cases
- [NSEvent.PointingDeviceType.cursor](nsevent/pointingdevicetype-swift.enum/cursor.md)
  Represents a cursor pointing device.
- [NSEvent.PointingDeviceType.eraser](nsevent/pointingdevicetype-swift.enum/eraser.md)
  Represents the eraser end of a stylus-like pointing device.
- [NSEvent.PointingDeviceType.pen](nsevent/pointingdevicetype-swift.enum/pen.md)
  Represents the tip end of a stylus-like pointing device.
- [NSEvent.PointingDeviceType.unknown](nsevent/pointingdevicetype-swift.enum/unknown.md)
  Represents an unknown type of pointing device.
### Initializers
- [init?(rawValue: UInt)](nsevent/pointingdevicetype-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var capabilityMask: Int](nsevent/capabilitymask.md)
  A mask that indicates the capabilities of the tablet device that generated this event.
- [var deviceID: Int](nsevent/deviceid.md)
  A special identifier the system matches against tablet-pointer and tablet-proximity events.
- [var isEnteringProximity: Bool](nsevent/isenteringproximity.md)
  A Boolean value that indicates whether a pointing device is entering or leaving the proximity of its tablet.
- [var pointingDeviceID: Int](nsevent/pointingdeviceid.md)
  The index of the pointing device currently in proximity with the tablet.
- [var pointingDeviceSerialNumber: Int](nsevent/pointingdeviceserialnumber.md)
  The vendor-assigned serial number of a pointing device.
- [var pointingDeviceType: NSEvent.PointingDeviceType](nsevent/pointingdevicetype-swift.property.md)
  The kind of pointing device associated with this event.
- [var systemTabletID: Int](nsevent/systemtabletid.md)
  The index of the tablet device connected to the system.
- [var tabletID: Int](nsevent/tabletid.md)
  The USB model identifier of the tablet device associated with this event.
- [var uniqueID: UInt64](nsevent/uniqueid.md)
  The unique identifier of the pointing device that generated this event.
- [var vendorID: Int](nsevent/vendorid.md)
  The vendor identifier of the tablet associated with the event.
- [var vendorPointingDeviceType: Int](nsevent/vendorpointingdevicetype.md)
  A coded bit field whose set bits indicate the type of pointing device (within a vendor selection) associated with the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/pointingdevicetype-swift.enum)*