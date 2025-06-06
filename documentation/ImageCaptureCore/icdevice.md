# ICDevice

**Framework**: ImageCaptureCore  
**Kind**: class

An abstract object that represents a device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
class ICDevice
```

#### Overview

The device browser uses the concrete subclasses [`ICCameraDevice`](iccameradevice.md) and [`ICScannerDevice`](icscannerdevice.md) to represent the cameras and scanners it finds.

## Topics

### Identifying a Device
- [var name: String?](icdevice/name.md)
  The device’s name as reported by the device module, or if no device module is in control of this device, by the device transport.
- [var productKind: String?](icdevice/productkind.md)
  The device’s type.
- [var icon: CGImage?](icdevice/icon.md)
  The device’s icon image.
- [var uuidString: String?](icdevice/uuidstring.md)
  A string representation of the device’s universally unique identifier (UUID).
- [var persistentIDString: String?](icdevice/persistentidstring.md)
  A string representation of the device’s persistent ID.
- [var serialNumberString: String?](icdevice/serialnumberstring.md)
  The device’s serial number.
### Inspecting a Device’s Type and Location
- [var type: ICDeviceType](icdevice/type.md)
  A combination of the device’s type and its location type.
- [enum ICDeviceType](icdevicetype.md)
  The type of image capture device.
- [enum ICDeviceTypeMask](icdevicetypemask.md)
  Masks for detecting different device types.
- [var locationDescription: String?](icdevice/locationdescription.md)
  A nonlocalized location description for the device.
- [var modulePath: String](icdevice/modulepath.md)
  The file system path of the device module associated with this device.
- [var moduleVersion: String?](icdevice/moduleversion.md)
  The bundle version of the device module associated with this device.
- [enum ICDeviceLocationType](icdevicelocationtype.md)
  The location of the image capture device.
- [enum ICDeviceLocationTypeMask](icdevicelocationtypemask.md)
  Masks for detecting different device locations.
- [struct ICDeviceLocationOptions](icdevicelocationoptions.md)
  Options for the location of the image capture device.
- [var usbLocationID: Int32](icdevice/usblocationid.md)
  The USB location that the device is occupying.
- [var usbProductID: Int32](icdevice/usbproductid.md)
  The USB Product ID (PID) associated with the device.
- [var usbVendorID: Int32](icdevice/usbvendorid.md)
  The USB Vendor ID (VID) associated with the device.
### Inspecting a Device’s Transport Type
- [var transportType: String?](icdevice/transporttype.md)
  The hardware connection type the device is using.
- [struct ICDeviceTransport](icdevicetransport.md)
  The hardware connection types a device can use.
### Inspecting a Device’s Capabilities
- [var capabilities: [String]](icdevice/capabilities.md)
  The capabilities of the device as reported by the device module.
- [struct ICDeviceCapability](icdevicecapability.md)
  Constants that describe the capabilities of a camera.
- [struct ICSessionOptions](icsessionoptions.md)
  Session options for altering the delivery of the device contents.
### Subscribing to Device Status Notifications
- [struct ICDeviceStatus](icdevicestatus.md)
  The status types that a device might deliver while in use.
### Managing a Device
- [var delegate: (any ICDeviceDelegate)?](icdevice/delegate.md)
  The delegate to receive messages once a session is opened on the device.
- [protocol ICDeviceDelegate](icdevicedelegate.md)
  Methods for responding to device events and changes.
- [var hasOpenSession: Bool](icdevice/hasopensession.md)
  A Boolean value that indicates whether the device has an open session.
- [func requestOpenSession()](icdevice/requestopensession.md)
  Requests to open a session on the device.
- [func requestOpenSession(options: [ICSessionOptions : Any]?, completion: ((any Error)?) -> Void)](icdevice/requestopensession(options:completion:).md)
  Requests to open a session on the device, then executes the completion handler.
- [func requestSendMessage(UInt32, outData: Data, maxReturnedDataSize: UInt32, sendMessageDelegate: Any, didSendMessageSelector: Selector, contextInfo: UnsafeMutableRawPointer?)](icdevice/requestsendmessage(_:outdata:maxreturneddatasize:sendmessagedelegate:didsendmessageselector:contextinfo:).md)
  Asynchronously sends an arbitrary message with optional data to a device.
- [func requestCloseSession()](icdevice/requestclosesession.md)
  Requests to close an open session on the device.
- [func requestCloseSession(options: [ICSessionOptions : Any]?, completion: ((any Error)?) -> Void)](icdevice/requestclosesession(options:completion:).md)
  Requests to close an open session on the device, then executes the completion handler.
- [func requestEject()](icdevice/requesteject.md)
  Requests to eject the media if permitted by the device, or to disconnect from a remote device.
- [func requestEject(completion: ((any Error)?) -> Void)](icdevice/requesteject(completion:).md)
  Requests to eject the media if permitted by the device, or to disconnect from a remote device, then executes the completion handler.
### Configuring a Device’s Characteristics
- [var userData: NSMutableDictionary?](icdevice/userdata.md)
  A bookkeeping object for client convenience.
- [var autolaunchApplicationPath: String?](icdevice/autolaunchapplicationpath.md)
  The file system path of an application to launch automatically when this device is added.
- [var isRemote: Bool](icdevice/isremote.md)
  A Boolean value indicating whether the device is published by the Image Capture device-sharing facility.
### Deprecated Symbols
- [func requestEjectOrDisconnect()](icdevice/requestejectordisconnect.md)
  Requests to eject the media if permitted by the device, or to disconnect from a remote device.
- [func requestYield()](icdevice/requestyield.md)
  Requests that device module in control of this device yield control.
- [var moduleExecutableArchitecture: Int32](icdevice/moduleexecutablearchitecture.md)
  The executable architecture of the device module servicing the requests.
### Instance Properties
- [var systemSymbolName: String?](icdevice/systemsymbolname.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [ICCameraDevice](iccameradevice.md)
- [ICScannerDevice](icscannerdevice.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var isBrowsing: Bool](icdevicebrowser/isbrowsing.md)
  A Boolean value indicating whether the device browser is browsing for devices.
- [var devices: [ICDevice]?](icdevicebrowser/devices.md)
  All devices found by the browser.
- [var browsedDeviceTypeMask: ICDeviceTypeMask](icdevicebrowser/browseddevicetypemask.md)
  A mask whose set bits indicate the type of devices being browsed after the delegate receives the start message.
- [func start()](icdevicebrowser/start.md)
  Tells the delegate to start looking for devices.
- [func stop()](icdevicebrowser/stop.md)
  Tells the delegate to stop looking for devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice)*