# HIDElementUpdate

**Framework**: Core HID  
**Kind**: protocol

A base protocol for element update types.

**Availability**:
- macOS 15.0+

## Declaration

```swift
protocol HIDElementUpdate : Hashable, Sendable
```

#### Overview

Not intended to be used directly, see [`HIDDeviceClient.ProvideElementUpdate`](hiddeviceclient/provideelementupdate.md) and [`HIDDeviceClient.RequestElementUpdate`](hiddeviceclient/requestelementupdate.md).

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [HIDDeviceClient.ProvideElementUpdate](hiddeviceclient/provideelementupdate.md)
- [HIDDeviceClient.RequestElementUpdate](hiddeviceclient/requestelementupdate.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelementupdate)*