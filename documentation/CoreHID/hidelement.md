# HIDElement

**Framework**: Core HID  
**Kind**: struct

A representation of an item from a report descriptor for a HID device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct HIDElement
```

## Mentions

- [Communicating with human interface devices](communicatingwithhiddevices.md)

#### Overview

A [`HIDElement`](hidelement.md) is an abstraction for the data in a HID report, and represents one item of data that could be sent or received in a report for a specific device. For example, for a mouse with a report descriptor that declares a report with 1 byte of data for each an X and a Y coordinate, there would be an element for the data associated with the X coordinate. If this element was monitored by a [`HIDDeviceClient`](hiddeviceclient.md), when an input report was received with an update to the X coordinate, a notification with the updated data would be sent to [`HIDDeviceClient.Notification.elementUpdates(values:)`](hiddeviceclient/notification/elementupdates(values:).md).

Elements are only received by requesting the elements for a specific device through a client’s [`elements`](hiddeviceclient/elements.md) property.

See the HID specification for more details: [`https://www.usb.org/hid`](https://developer.apple.comhttps://www.usb.org/hid).

## Topics

### Structures
- [HIDElement.Value](hidelement/value.md)
  Data associated with a HID element.
### Instance Properties
- [var client: HIDDeviceClient](hidelement/client.md)
  The client for the device with which this element is associated.
- [var logicalMaximum: Int64?](hidelement/logicalmaximum.md)
  The logical maximum for this element’s data.
- [var logicalMinimum: Int64?](hidelement/logicalminimum.md)
  The logical minimum for this element’s data.
- [var parentCollection: HIDElementCollection](hidelement/parentcollection.md)
  The [`HIDElementCollection`](hidelementcollection.md) that contains this element.
- [var physicalMaximum: Int64?](hidelement/physicalmaximum.md)
  The physical maximum for this element’s data.
- [var physicalMinimum: Int64?](hidelement/physicalminimum.md)
  The physical minimum for this element’s data.
- [var reportID: HIDReportID?](hidelement/reportid.md)
  The report ID for the report that contains this element.
- [var reportSize: UInt32](hidelement/reportsize.md)
  The size in bits of the data for this element.
- [var type: HIDReportType](hidelement/type.md)
  The type of this element.
- [var unit: UInt32?](hidelement/unit.md)
  The HID specification compliant unit code for this element.
- [var unitExponent: Int8?](hidelement/unitexponent.md)
  The calculated exponent for this element.
- [var usage: HIDUsage](hidelement/usage.md)
  The HID specification compliant usage for this element.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Communicating with human interface devices](communicatingwithhiddevices.md)
  Interact with and obtain data from devices such as keyboards and mice.
- [actor HIDDeviceClient](hiddeviceclient.md)
  A client of a physical or virtual HID compatible peripheral.
- [struct HIDElementCollection](hidelementcollection.md)
  A collection of items from a report descriptor for a HID device.
- [HIDElement.Value](hidelement/value.md)
  Data associated with a HID element.
- [protocol HIDElementUpdate](hidelementupdate.md)
  A base protocol for element update types.
- [enum HIDReportType](hidreporttype.md)
  Types for HID reports.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement)*