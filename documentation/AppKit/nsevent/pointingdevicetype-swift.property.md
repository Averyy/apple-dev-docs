# pointingDeviceType

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The kind of pointing device associated with this event.

**Availability**:
- macOS

## Declaration

```swift
var pointingDeviceType: NSEvent.PointingDeviceType { get }
```

```objc
@property (readonly) NSPointingDeviceType pointingDeviceType;
```

#### Discussion

For example, the device could be a pen, eraser, or cursor pointing device. This property is valid for mouse events with subtype `NSTabletProximityEventSubtype` and for `NSTabletProximity` events. See `Getting Unicode Values` for descriptions of valid NSPointingDeviceType constants.

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
- [NSEvent.PointingDeviceType](./pointingdevicetype-swift.enum.md)
  The pointing-device types for tablet-proximity events or mouse events with a proximity event subtype.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/pointingdevicetype-swift.property)*