# DeviceDiscoveryExtension

**Framework**: DeviceDiscoveryExtension  
**Kind**: module

Stream media to a third-party device that a user selects in a system menu.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 15.0+
- visionOS 1.0+

#### Overview

Use DeviceDiscoveryExtension (DDE) to discover third-party media receivers to which your app can stream AV content.

When a user invokes your app’s media-streaming UI, you can offer a third-party, local-network, or Bluetooth device as a streaming destination in a route picker view ([`AVRoutePickerView`](https://developer.apple.com/documentation/AVKit/AVRoutePickerView)). The figure below illustrates actors in the discovery process. As depicted in the System section, your app’s device discovery extension loads when the view displays.

![A flowchart with four boxes in a horizontal row from left to right, each labeled respectively: user, app, system, and third-party device. Lines that represent channels extend downward from each box. At the top of the user channel is the start of a continuous arrow that traces a path with switchbacks through all the channels. Multiple steps of the device discovery process are shown in this path with arrows that indicate the order in which they occur, from the user invoking it until the third-party device plays the media.](https://docs-assets.developer.apple.com/published/1729cdc9d04d8250ae66a99bd7c12dfa/media-4056835%402x.png)

Once the extension loads:

- The extension runs in a system process and searches the local network and Bluetooth devices for a specific media receiver.
- When the extension finds the device, it returns the device to the system, which displays it in the picker view as an available option.
- The user makes a selection and the system passes the chosen device to the app, which can then stream media to the device.

Because DDE runs in a system sandbox, the extension doesn’t need to ask the user for local-network or Bluetooth permissions. The picker view displays discovered third-party devices and protocols in the same system menu as AirPlay, which provides a unified device-selection experience.

> **Note**:  To stream to a third-party device that you don’t manufacture, bundle your app with the device discovery extension that the manufacturer provides as part of its SDK.

 To stream to a third-party device that you don’t manufacture, bundle your app with the device discovery extension that the manufacturer provides as part of its SDK.

## Topics

### Essentials
- [Discovering a third-party media-streaming device](discovering-a-third-party-media-streaming-device.md)
  Build an extension that streams media to a server app in iOS or macOS.
- [Media Device Discovery Extension](../BundleResources/Entitlements/com.apple.developer.media-device-discovery-extension.md)
  An entitlement for an app extension that adds a specific third-party media receiver to a system device-picker UI.
### Extension
- [protocol DDDiscoveryExtension](dddiscoveryextension.md)
  A specification that enables the framework to start and stop the extension’s discovery process.
- [class DDDiscoverySession](dddiscoverysession.md)
  An object that relays device discovery events from the extension to the system.
- [class DDDiscoveryExtensionConfiguration](dddiscoveryextensionconfiguration.md)
  An object that manages the extension’s communication with the framework.
- [protocol DDDiscoveryExtensionConfigurationProtocol](dddiscoveryextensionconfigurationprotocol.md)
  A specification that provides a communication channel between the extension and the framework.
### Life cycle
- [class DDDeviceEvent](dddeviceevent.md)
  An object that provides a device or communicates its change in status.
- [DDDeviceEvent.EventType](dddeviceevent/eventtype-swift.enum.md)
  Identifiers for the types of events that occur in the device discovery life cycle.
- [func DDEventTypeToString(DDDeviceEvent.EventType) -> String](ddeventtypetostring(_:).md)
  Returns human-readable text for the specified event identifier.
- [typealias DDEventHandler](ddeventhandler.md)
  A function that the extension invokes to signal an event.
### Device information
- [class DDDevice](dddevice.md)
  An object that describes a discovered device of interest.
- [DDDevice.Category](dddevice/category-swift.enum.md)
  An option that determines the icon for the device in the picker UI.
- [enum DDDeviceState](dddevicestate.md)
  A state that represents the level of user interaction with the device.
- [func DDDeviceCategoryToString(DDDevice.Category) -> String](dddevicecategorytostring(_:).md)
  Returns human-readable text for the specified identifier that describes a device’s category.
- [func DDDeviceStateToString(DDDeviceState) -> String](dddevicestatetostring(_:).md)
  Returns human-readable text for the specified identifier that describes a device’s status.
- [DDDevice.Protocol](dddevice/protocol-swift.enum.md)
  An identifier for the manner in which an app interacts with a device.
- [func DDDeviceProtocolToString(DDDevice.Protocol) -> String](dddeviceprotocoltostring(_:).md)
  Returns human-readable text for the specified protocol identifier.
- [struct DDDeviceProtocolString](dddeviceprotocolstring.md)
  String values for the manner in which an app interacts with a device.
- [func DDDeviceMediaPlaybackStateToString(DDDevice.MediaPlaybackState) -> String](dddevicemediaplaybackstatetostring(_:).md)
  Returns human-readable text for the specified media playback state.
### Errors
- [struct DDError](dderror.md)
  An error that the framework reports.
- [DDError.Code](dderror/code.md)
  Codes that identify errors that can occur during the framework’s use.
- [typealias DDErrorHandler](dderrorhandler.md)
  A function that executes code you provide when an operation returns an error or completes successfully.
- [typealias DDErrorOutType](dderrorouttype.md)
  A type for framework functions that return error references.
- [let DDErrorDomain: String](dderrordomain.md)
  A unique error domain for the framework.
### Reference
- [DeviceDiscoveryExtension Enumerations](devicediscoveryextension-enumerations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeviceDiscoveryExtension)*