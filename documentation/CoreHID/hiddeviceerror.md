# HIDDeviceError

**Framework**: Core HID  
**Kind**: enum

Errors that the framework can throw.

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum HIDDeviceError
```

## Topics

### Enumeration Cases
- [HIDDeviceError.aborted](hiddeviceerror/aborted.md)
  The request was aborted.
- [HIDDeviceError.badArgument](hiddeviceerror/badargument.md)
  The request contains an inappropriate argument.
- [HIDDeviceError.busy](hiddeviceerror/busy.md)
  The device is busy.
- [HIDDeviceError.deviceError](hiddeviceerror/deviceerror.md)
  There was an error with the device that couldn’t be further determined.
- [HIDDeviceError.exclusiveAccess](hiddeviceerror/exclusiveaccess.md)
  Another client posesses exclusive access to this device.
- [HIDDeviceError.ioError](hiddeviceerror/ioerror.md)
  An input/output error occurred between the host and the device.
- [HIDDeviceError.messageTooLarge](hiddeviceerror/messagetoolarge.md)
  The data provided to a function was too large for the device to handle.
- [HIDDeviceError.noPower](hiddeviceerror/nopower.md)
  The device isn’t powered.
- [HIDDeviceError.noResources](hiddeviceerror/noresources.md)
  The device doesn’t have the resources required to handle this request.
- [HIDDeviceError.notPermitted](hiddeviceerror/notpermitted.md)
  The client isn’t permitted to make this request with the provided arguments.
- [HIDDeviceError.notPrivileged](hiddeviceerror/notprivileged.md)
  The client doesn’t have the privileges required to make this request.
- [HIDDeviceError.notReady](hiddeviceerror/notready.md)
  The device isn’t ready for this request.
- [HIDDeviceError.notResponding](hiddeviceerror/notresponding.md)
  The device isn’t responding.
- [HIDDeviceError.timeout](hiddeviceerror/timeout.md)
  The request timed out.
- [HIDDeviceError.unknown(_:)](hiddeviceerror/unknown(_:).md)
  A catch-all for uncommon errors.
- [HIDDeviceError.unsupported](hiddeviceerror/unsupported.md)
  The request with the provided arguments isn’t supported.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
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
- [struct HIDReportID](hidreportid.md)
  A type to represent the report IDs of HID reports.
- [enum HIDUsage](hidusage.md)
  A type to represent HID usage pages.
- [enum HIDDeviceTransport](hiddevicetransport.md)
  Common transport types that transmit data to or from a HID device.
- [enum HIDDeviceLocalizationCode](hiddevicelocalizationcode.md)
  The localization codes that some HID devices declare to specify conformance to a certain format or language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceerror)*