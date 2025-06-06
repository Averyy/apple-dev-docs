# HIDDeviceClient

**Framework**: Core HID  
**Kind**: class

A client of a physical or virtual HID compatible peripheral.

**Availability**:
- macOS 15.0+

## Declaration

```swift
actor HIDDeviceClient
```

## Mentions

- [Creating virtual devices](creatingvirtualdevices.md)
- [Communicating with human interface devices](communicatingwithhiddevices.md)

#### Overview

A human interface device (HID) is a computer peripheral intended to provide direction to the system from human input. The specification is a broad, industry-wide standard, maintained by the USB Implementers Forum. For more details, see [`Human Interface Devices (HID) Specifications and Tools`](https://developer.apple.comhttps://www.usb.org/hid).

A [`HIDDeviceClient`](hiddeviceclient.md) is a connection to one HID device on the system. It’s created using a [`HIDDeviceClient.DeviceReference`](hiddeviceclient/devicereference-swift.struct.md), received from a [`HIDDeviceManager`](hiddevicemanager.md). A [`HIDDeviceClient.DeviceReference`](hiddeviceclient/devicereference-swift.struct.md) is a simple reference to a specific HID device. The HID peripheral can be a USB device like a wired mouse, a Bluetooth device like a wireless keyboard, an onboard sensor like an accelerometer, or even a software based, virtual peripheral created using [`HIDVirtualDevice`](hidvirtualdevice.md).

A [`HIDDeviceClient`](hiddeviceclient.md) receives device notifications, such as input HID reports that are dispatched from the device in response to human input (like a keyboard key press) in [`monitorNotifications(reportIDsToMonitor:elementsToMonitor:)`](hiddeviceclient/monitornotifications(reportidstomonitor:elementstomonitor:).md). It sends get and set reports to the device to retrieve information or configure device functionality using [`dispatchSetReportRequest(type:id:data:timeout:)`](hiddeviceclient/dispatchsetreportrequest(type:id:data:timeout:).md). [`dispatchGetReportRequest(type:id:timeout:)`](hiddeviceclient/dispatchgetreportrequest(type:id:timeout:).md). It monitors or updates specific pieces of the HID report using [`HIDElement`](hidelement.md).

## Topics

### Create a device client
- [init?(deviceReference: HIDDeviceClient.DeviceReference)](hiddeviceclient/init(devicereference:).md)
  Creates a client for a HID device.
- [HIDDeviceClient.DeviceReference](hiddeviceclient/devicereference-swift.struct.md)
  A reference to a HID device on the system.
- [let deviceReference: HIDDeviceClient.DeviceReference](hiddeviceclient/devicereference-swift.property.md)
  The reference to the HID device used to create the  HID client device.
### Get device information
- [var descriptor: Data](hiddeviceclient/descriptor.md)
  The HID specification compliant report descriptor for the associated HID device.
- [var deviceUsages: [HIDUsage]](hiddeviceclient/deviceusages.md)
  A convenient list of all the usages that the device supports.
- [var isBuiltIn: Bool](hiddeviceclient/isbuiltin.md)
  A Boolean value that determines whether the device is built-in to the system or an external peripheral.
- [var localizationCode: HIDDeviceLocalizationCode](hiddeviceclient/localizationcode.md)
  A location code that specifies the HID compliant localization code, if there is one.
- [var locationID: UInt64?](hiddeviceclient/locationid.md)
  The location ID for the device, if there is one.
- [var manufacturer: String?](hiddeviceclient/manufacturer.md)
  The manufacturer of the device, if known.
- [var modelNumber: String?](hiddeviceclient/modelnumber.md)
  The model number for the device, if known.
- [let primaryUsage: HIDUsage](hiddeviceclient/primaryusage.md)
  The HID specification compliant usage for the device.
- [var product: String?](hiddeviceclient/product.md)
  The product name for the device, if known.
- [let productID: UInt32](hiddeviceclient/productid.md)
  The product ID for the device.
- [var serialNumber: String?](hiddeviceclient/serialnumber.md)
  The serial number of the device, if known.
- [var transport: HIDDeviceTransport?](hiddeviceclient/transport.md)
  The data transport for the device.
- [var uniqueID: String?](hiddeviceclient/uniqueid.md)
  A unique ID for the device, if there is one.
- [let vendorID: UInt32](hiddeviceclient/vendorid.md)
  The vendor ID for the device.
- [var versionNumber: UInt64?](hiddeviceclient/versionnumber.md)
  The version of the device, if known.
- [var elements: [HIDElement]](hiddeviceclient/elements.md)
  All HID elements associated with the device.
### Interact with the device
- [func dispatchGetReportRequest(type: HIDReportType, id: HIDReportID?, timeout: Duration?) async throws -> Data](hiddeviceclient/dispatchgetreportrequest(type:id:timeout:).md)
  Send a get report request to the device over the transport.
- [func dispatchSetReportRequest(type: HIDReportType, id: HIDReportID?, data: Data, timeout: Duration?) async throws](hiddeviceclient/dispatchsetreportrequest(type:id:data:timeout:).md)
  Send a set report request to the device over the transport.
- [func seizeDevice() throws](hiddeviceclient/seizedevice.md)
  Attempt to obtain the device so that this client is the only active client.
### Monitor device notifications
- [func monitorNotifications(reportIDsToMonitor: [ClosedRange<HIDReportID>], elementsToMonitor: [HIDElement]) -> AsyncThrowingStream<HIDDeviceClient.Notification, any Error>](hiddeviceclient/monitornotifications(reportidstomonitor:elementstomonitor:).md)
  Creates an asynchronous that receives notifications about the associated device.
- [HIDDeviceClient.Notification](hiddeviceclient/notification.md)
  Notifications for a HID device.
### Update element values
- [func updateElements([any HIDElementUpdate], timeout: Duration?) async -> HIDDeviceClient.HIDElementUpdateResult](hiddeviceclient/updateelements(_:timeout:).md)
  Provide new update values for, or request current values from, lists of elements.
- [HIDDeviceClient.RequestElementUpdate](hiddeviceclient/requestelementupdate.md)
  A request to pull the current value from a list of HID elements
- [HIDDeviceClient.ProvideElementUpdate](hiddeviceclient/provideelementupdate.md)
  A structure that provides values for a list of HID elements.
- [HIDDeviceClient.HIDElementUpdateResult](hiddeviceclient/hidelementupdateresult.md)
  A class to hold the results of an element update.
### Structures
- [HIDDeviceClient.UnsafeProperty](hiddeviceclient/unsafeproperty.md)
  A wrapper around an object to facilitate working with subscripts.
### Instance Properties
- [var unownedExecutor: UnownedSerialExecutor](hiddeviceclient/unownedexecutor.md)
  Retrieve the executor for this actor as an optimized, unowned reference.
### Subscripts
- [subscript(String) -> HIDDeviceClient.UnsafeProperty?](hiddeviceclient/subscript(_:).md)
  Get or set a property from the device.
### Default Implementations
- [Actor Implementations](hiddeviceclient/actor-implementations.md)
- [CustomStringConvertible Implementations](hiddeviceclient/customstringconvertible-implementations.md)
- [Equatable Implementations](hiddeviceclient/equatable-implementations.md)
- [Hashable Implementations](hiddeviceclient/hashable-implementations.md)

## Relationships

### Conforms To
- [Actor](../Swift/Actor.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Communicating with human interface devices](communicatingwithhiddevices.md)
  Interact with and obtain data from devices such as keyboards and mice.
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
- [enum HIDDeviceTransport](hiddevicetransport.md)
  Common transport types that transmit data to or from a HID device.
- [enum HIDDeviceLocalizationCode](hiddevicelocalizationcode.md)
  The localization codes that some HID devices declare to specify conformance to a certain format or language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient)*