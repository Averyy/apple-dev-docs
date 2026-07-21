# Core HID

**Framework**: Core HID  
**Kind**: module

Interact with keyboards, mice, and other human interface devices.

**Availability**:
- macOS 15.0+

#### Overview

The CoreHID framework facilitates interaction with human interface devices (HID), like a keyboard, mouse, or other device. Interactions include receiving data that a device generates, such as a key press or mouse click. CoreHID also allows sending requests to a device, such as a request to turn on an LED. You can also emulate a device connected to the system, such as a virtual game controller, and send input to other apps without physical hardware.

![An image showing the Swift logo on the left. Three arrows emerge from it and point to the right. The first arrow points to a game controller. The second arrow points to a mouse. The third arrow points to a keyboard.](https://docs-assets.developer.apple.com/published/45cd6758ca7b3a8491fd51c7d1f525b3/core-hid-overview%402x.png)

To learn more about HID devices, see the [`USB standards website`](https://developer.apple.comhttps://www.usb.org/hid).

## Topics

### Discovery
- [Discovering HID devices from Terminal](discoveringhiddevicesfromterminal.md)
  Identify devices connected to your Mac from the command line.
- [actor HIDDeviceManager](hiddevicemanager.md)
  A helper for discovering human interface devices (HID) connected to the system.
- [HIDDeviceManager.DeviceMatchingCriteria](hiddevicemanager/devicematchingcriteria.md)
  Matching criteria used to filter HID devices.
### Interaction
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
- [enum HIDDeviceTransport](hiddevicetransport.md)
  Common transport types that transmit data to or from a HID device.
- [enum HIDDeviceLocalizationCode](hiddevicelocalizationcode.md)
  The localization codes that some HID devices declare to specify conformance to a certain format or language.
### Simulation
- [Creating virtual devices](creatingvirtualdevices.md)
  Use and interact with a virtual human interface device for testing and development.
- [actor HIDVirtualDevice](hidvirtualdevice.md)
  A virtual service to emulate a HID device connected to the system.
- [protocol HIDVirtualDeviceDelegate](hidvirtualdevicedelegate.md)
  The delegate to receive notifications for a virtual HID device.
- [HIDVirtualDevice.Properties](hidvirtualdevice/properties.md)
  The properties for a virtual HID device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreHID)*