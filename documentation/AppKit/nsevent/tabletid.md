# tabletID

**Framework**: AppKit  
**Kind**: property

The USB model identifier of the tablet device associated with this event.

**Availability**:
- macOS ?+

## Declaration

```swift
var tabletID: Int { get }
```

#### Discussion

This property is valid for mouse events with subtype `NSTabletProximityEventSubtype` and for `NSTabletProximity` events.

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
- [NSEvent.PointingDeviceType](nsevent/pointingdevicetype-swift.enum.md)
  The pointing-device types for tablet-proximity events or mouse events with a proximity event subtype.
- [var systemTabletID: Int](nsevent/systemtabletid.md)
  The index of the tablet device connected to the system.
- [var uniqueID: UInt64](nsevent/uniqueid.md)
  The unique identifier of the pointing device that generated this event.
- [var vendorID: Int](nsevent/vendorid.md)
  The vendor identifier of the tablet associated with the event.
- [var vendorPointingDeviceType: Int](nsevent/vendorpointingdevicetype.md)
  A coded bit field whose set bits indicate the type of pointing device (within a vendor selection) associated with the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/tabletid)*