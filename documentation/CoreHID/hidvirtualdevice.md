# HIDVirtualDevice

**Framework**: Core HID  
**Kind**: class

A virtual service to emulate a HID device connected to the system.

**Availability**:
- macOS 15.0+

## Declaration

```swift
actor HIDVirtualDevice
```

## Mentions

- [Creating virtual devices](creatingvirtualdevices.md)

#### Overview

A HID device is a computer peripheral intended to provide direction to the system from human input. The specification is a broad, industry-wide standard maintained by the [`USB Implementers Forum`](https://developer.apple.comhttps://www.usb.org/hid).

A `HIDVirtualDevice` is an object that emulates a HID device connected to the system, without the need for a physical device. Such a tool can be used by an app to emulate a keyboard and dispatch HID reports to the system using [`dispatchInputReport(data:timestamp:)`](hidvirtualdevice/dispatchinputreport(data:timestamp:).md) that signify key strokes, and could be received by a [`HIDDeviceClient`](hiddeviceclient.md)listening for such activity in other apps. The virtual device can also receive requests from the system using its [`HIDVirtualDeviceDelegate`](hidvirtualdevicedelegate.md).

## Topics

### Create a HID virtual device
- [init?(properties: HIDVirtualDevice.Properties)](hidvirtualdevice/init(properties:).md)
  Creates a virtual HID device.
- [let deviceReference: HIDDeviceClient.DeviceReference](hidvirtualdevice/devicereference.md)
  The reference to the virtual HID device.
- [func activate(delegate: any HIDVirtualDeviceDelegate)](hidvirtualdevice/activate(delegate:).md)
  Activate a newly created virtual device to begin receiving notifications and enable functionality.
### Dispatch input reports
- [func dispatchInputReport(data: Data, timestamp: SuspendingClock.Instant) async throws](hidvirtualdevice/dispatchinputreport(data:timestamp:).md)
  Dispatch an input report to the system.
### Structures
- [HIDVirtualDevice.Properties](hidvirtualdevice/properties.md)
  The properties for a virtual HID device.
### Instance Properties
- [var unownedExecutor: UnownedSerialExecutor](hidvirtualdevice/unownedexecutor.md)
  Retrieve the executor for this actor as an optimized, unowned reference.
### Default Implementations
- [Actor Implementations](hidvirtualdevice/actor-implementations.md)
- [CustomStringConvertible Implementations](hidvirtualdevice/customstringconvertible-implementations.md)
- [Equatable Implementations](hidvirtualdevice/equatable-implementations.md)
- [Hashable Implementations](hidvirtualdevice/hashable-implementations.md)

## Relationships

### Conforms To
- [Actor](../Swift/Actor.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Creating virtual devices](creatingvirtualdevices.md)
  Use and interact with a virtual human interface device for testing and development.
- [protocol HIDVirtualDeviceDelegate](hidvirtualdevicedelegate.md)
  The delegate to receive notifications for a virtual HID device.
- [HIDVirtualDevice.Properties](hidvirtualdevice/properties.md)
  The properties for a virtual HID device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidvirtualdevice)*