# HIDVirtualDeviceDelegate

**Framework**: Core HID  
**Kind**: protocol

The delegate to receive notifications for a virtual HID device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
protocol HIDVirtualDeviceDelegate : Sendable
```

## Mentions

- [Creating virtual devices](creatingvirtualdevices.md)

#### Overview

A delegate must be created and provided to [`activate(delegate:)`](hidvirtualdevice/activate(delegate:).md) during activation of a virtual HID device. This delegate receives notifications intended for the device, such as a get report request from a client. One delegate can be used for many devices.

## Topics

### Receive notifications for a device
- [func hidVirtualDevice(HIDVirtualDevice, receivedSetReportRequestOfType: HIDReportType, id: HIDReportID?, data: Data) async throws](hidvirtualdevicedelegate/hidvirtualdevice(_:receivedsetreportrequestoftype:id:data:).md)
  A notification that a set report request has been received from the system.
- [func hidVirtualDevice(HIDVirtualDevice, receivedGetReportRequestOfType: HIDReportType, id: HIDReportID?, maxSize: Int) async throws -> Data](hidvirtualdevicedelegate/hidvirtualdevice(_:receivedgetreportrequestoftype:id:maxsize:).md)
  A notification that a get report request has been received from the system.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Creating virtual devices](creatingvirtualdevices.md)
  Use and interact with a virtual human interface device for testing and development.
- [actor HIDVirtualDevice](hidvirtualdevice.md)
  A virtual service to emulate a HID device connected to the system.
- [HIDVirtualDevice.Properties](hidvirtualdevice/properties.md)
  The properties for a virtual HID device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidvirtualdevicedelegate)*