# HIDReportType

**Framework**: Core HID  
**Kind**: enum

Types for HID reports.

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum HIDReportType
```

#### Overview

For more details, see [`Human Interface Devices (HID) Specifications and Tools`](https://developer.apple.comhttps://www.usb.org/hid).

## Topics

### Operators
- [static func == (HIDReportType, HIDReportType) -> Bool](hidreporttype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [HIDReportType.feature](hidreporttype/feature.md)
  A feature report is bidirectional configuration data, typically used to alter device or software functionality.
- [HIDReportType.input](hidreporttype/input.md)
  An input report is data dispatched from the device to the system, typically sent in response to human interaction with one of the device controls.
- [HIDReportType.output](hidreporttype/output.md)
  An output report is data sent from the system to the device, typically used to set a device control.
### Instance Properties
- [var hashValue: Int](hidreporttype/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](hidreporttype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](hidreporttype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

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
- [struct HIDReportID](hidreportid.md)
  A type to represent the report IDs of HID reports.
- [enum HIDUsage](hidusage.md)
  A type to represent HID usage pages.
- [enum HIDDeviceError](hiddeviceerror.md)
  Errors that the framework can throw.
- [enum HIDDeviceTransport](hiddevicetransport.md)
  Common transport types that transmit data to or from a HID device.
- [enum HIDDeviceLocalizationCode](hiddevicelocalizationcode.md)
  The localization codes that some HID devices declare to specify conformance to a certain format or language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidreporttype)*