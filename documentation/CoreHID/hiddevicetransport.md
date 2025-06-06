# HIDDeviceTransport

**Framework**: Core HID  
**Kind**: enum

Common transport types that transmit data to or from a HID device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum HIDDeviceTransport
```

#### Overview

If a device declares an uncommon transport, the [`HIDDeviceTransport.unknown(_:)`](hiddevicetransport/unknown(_:).md) case is used with the associated raw string value.

## Topics

### Operators
- [static func == (HIDDeviceTransport, HIDDeviceTransport) -> Bool](hiddevicetransport/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [HIDDeviceTransport.aid](hiddevicetransport/aid.md)
- [HIDDeviceTransport.airPlay](hiddevicetransport/airplay.md)
- [HIDDeviceTransport.bluetooth](hiddevicetransport/bluetooth.md)
- [HIDDeviceTransport.bluetoothAACP](hiddevicetransport/bluetoothaacp.md)
- [HIDDeviceTransport.bluetoothLowEnergy](hiddevicetransport/bluetoothlowenergy.md)
- [HIDDeviceTransport.fifo](hiddevicetransport/fifo.md)
- [HIDDeviceTransport.i2c](hiddevicetransport/i2c.md)
- [HIDDeviceTransport.iap](hiddevicetransport/iap.md)
- [HIDDeviceTransport.serial](hiddevicetransport/serial.md)
- [HIDDeviceTransport.spi](hiddevicetransport/spi.md)
- [HIDDeviceTransport.spu](hiddevicetransport/spu.md)
- [HIDDeviceTransport.unknown(_:)](hiddevicetransport/unknown(_:).md)
- [HIDDeviceTransport.usb](hiddevicetransport/usb.md)
- [HIDDeviceTransport.virtual](hiddevicetransport/virtual.md)
### Default Implementations
- [Equatable Implementations](hiddevicetransport/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
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
- [enum HIDReportType](hidreporttype.md)
  Types for HID reports.
- [struct HIDReportID](hidreportid.md)
  A type to represent the report IDs of HID reports.
- [enum HIDUsage](hidusage.md)
  A type to represent HID usage pages.
- [enum HIDDeviceError](hiddeviceerror.md)
  Errors that the framework can throw.
- [enum HIDDeviceLocalizationCode](hiddevicelocalizationcode.md)
  The localization codes that some HID devices declare to specify conformance to a certain format or language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddevicetransport)*