# DDDevice

**Framework**: DeviceDiscoveryExtension  
**Kind**: class

An object that describes a discovered device of interest.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
class DDDevice
```

#### Overview

The extension creates an instance of this class for a discovered device of interest and passes it to the system for display in the device picker UI ([`AVRoutePickerView`](https://developer.apple.com/documentation/AVKit/AVRoutePickerView)).

The extension discovers devices through either Core Bluetooth or the local network (that is, using [`Bonjour`](https://developer.apple.com/documentation/Foundation/bonjour)).

For device discovery extensions of third-party media receivers, an instance of this class corresponds to the media receiver of interest.

The extension reports the status of discovered devices to the system using the [`report(_:)`](dddiscoverysession/report(_:).md) function, and it receives status updates about the device from the system by implementing [`didReceiveEvent(_:)`](dddiscoveryextension/didreceiveevent(_:).md).

## Topics

### Initializing a device
- [init(displayName: String, category: DDDevice.Category, protocolType: UTType, identifier: String)](dddevice/init(displayname:category:protocoltype:identifier:).md)
  Creates an object that describes a discovered device.
### Identifying the device
- [var displayName: String](dddevice/displayname.md)
  A name for the device to display to the user.
- [var identifier: String](dddevice/identifier.md)
  A unique identifier for the device.
- [var category: DDDevice.Category](dddevice/category-swift.property.md)
  An option that determies the icon that the picker UI displays for the device.
- [DDDevice.Category](dddevice/category-swift.enum.md)
  An option that determines the icon for the device in the picker UI.
### Indicating the protocol
- [var `protocol`: DDDevice.Protocol](dddevice/protocol-swift.property.md)
  The manner in which the system applies your app’s device discovery extension.
- [DDDevice.Protocol](dddevice/protocol-swift.enum.md)
  An identifier for the manner in which an app interacts with a device.
- [var protocolType: UTType](dddevice/protocoltype.md)
  A custom universal type that describes the device’s manner of communication with the extension.
- [var bluetoothIdentifier: UUID?](dddevice/bluetoothidentifier.md)
  An identifier to communicate with the device through Bluetooth wireless technology.
- [var networkEndpoint: NWEndpoint?](dddevice/networkendpoint-3lah1.md)
  An object that describes a local-network device.
### Setting the device state
- [var state: DDDeviceState](dddevice/state.md)
  A state that represents the level of user interaction with the device.
- [var txtRecord: NWTXTRecord?](dddevice/txtrecord.md)
  A dictionary of metadata for the device that the extension communicates with over the local network.
- [var url: URL](dddevice/url.md)
  A resource locator for the simple service discovery protocol.
- [var supportsGrouping: Bool](dddevice/supportsgrouping.md)
  A Boolean value that indicates whether to group the device with others in the AirPlay UI.
### Communicating device content and playback status
- [var mediaContentTitle: String?](dddevice/mediacontenttitle.md)
  A title for the current media that the device plays.
- [var mediaContentSubtitle: String?](dddevice/mediacontentsubtitle.md)
  A subtitle for the current media that the device plays.
- [var mediaPlaybackState: DDDevice.MediaPlaybackState](dddevice/mediaplaybackstate-swift.property.md)
  A playback status for the device’s current media.
- [DDDevice.MediaPlaybackState](dddevice/mediaplaybackstate-swift.enum.md)
  States that indicate the status of a device’s media playback.
### Instance Properties
- [var deviceSupports: DDDeviceSupports](dddevice/devicesupports.md)
- [var displayImageName: String?](dddevice/displayimagename.md)
- [var ssid: String?](dddevice/ssid.md)
- [var wifiAwareModelName: String?](dddevice/wifiawaremodelname.md)
  Device’s Wi-Fi Aware model name.
- [var wifiAwareServiceName: String?](dddevice/wifiawareservicename.md)
  Device’s Wi-Fi Aware’s service name.
- [var wifiAwareServiceRole: DDDevice.WiFiAwareServiceRole](dddevice/wifiawareservicerole-swift.property.md)
  Device’s Wi-Fi Aware’s service. Default is `DDDeviceWiFiAwareServiceRoleSubscriber`
- [var wifiAwareVendorName: String?](dddevice/wifiawarevendorname.md)
  Device’s Wi-Fi Aware vendor name.
### Enumerations
- [DDDevice.WiFiAwareServiceRole](dddevice/wifiawareservicerole-swift.enum.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice)*