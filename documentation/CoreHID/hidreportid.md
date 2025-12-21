# HIDReportID

**Framework**: Core HID  
**Kind**: struct

A type to represent the report IDs of HID reports.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct HIDReportID
```

## Mentions

- [Communicating with human interface devices](communicatingwithhiddevices.md)

#### Overview

Report IDs are defined to be 1 byte in the HID specification, and can help identify the reports received from or sent to a device. Report IDs are optional. If a descriptor only has one report, a report ID is unnecessary. A report ID of 0 is invalid.

For more details, see [`Human Interface Devices (HID) Specifications and Tools`](https://developer.apple.comhttps://www.usb.org/hid).

## Topics

### Initializers
- [init?(rawValue: UInt8)](hidreportid/init(rawvalue:).md)
  Creates a HID report ID.
### Instance Properties
- [var rawValue: HIDReportID.RawValue](hidreportid/rawvalue.md)
  The raw value of the report ID.
### Type Properties
- [static let allReports: ClosedRange<HIDReportID>](hidreportid/allreports.md)
  A convenient definition that represents every possible report ID.

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Communicating with human interface devices](communicatingwithhiddevices.md)
  Interact with and obtain data from devices such as keyboards and mice.
- [actor HIDDeviceClient](hiddeviceclient.md)
  A client of a physical or virtual HID compatible peripheral.
- [struct HIDElement](hidelement.md)
  A representation of an item from a report descriptor for a HID device.
- [struct HIDElementCollection](hidelementcollection.md)
  A collection of items from a report descriptor for a HID device.
- [HIDElement.Value](hidelement/value.md)
  Data associated with a HID element.
- [protocol HIDElementUpdate](hidelementupdate.md)
  A base protocol for element update types.
- [enum HIDReportType](hidreporttype.md)
  Types for HID reports.
- [enum HIDUsage](hidusage.md)
  A type to represent HID usage pages.
- [enum HIDDeviceError](hiddeviceerror.md)
  Errors that the framework can throw.
- [enum HIDDeviceTransport](hiddevicetransport.md)
  Common transport types that transmit data to or from a HID device.
- [enum HIDDeviceLocalizationCode](hiddevicelocalizationcode.md)
  The localization codes that some HID devices declare to specify conformance to a certain format or language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidreportid)*