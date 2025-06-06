# DDDiscoveryExtension

**Framework**: DeviceDiscoveryExtension  
**Kind**: protocol

A specification that enables the framework to start and stop the extension’s discovery process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
protocol DDDiscoveryExtension : AppExtension
```

#### Overview

Your extension adopts this protocol as the primary entry and exit points for device discovery.

The system calls your extension’s [`startDiscovery(session:)`](dddiscoveryextension/startdiscovery(session:).md) when [`AVRoutePickerView`](https://developer.apple.com/documentation/AVKit/AVRoutePickerView) displays so your extension can include a specific third-party device in the picker. When the picker UI dismisses or the user selects a device, the system calls your extension’s [`stopDiscovery(session:)`](dddiscoveryextension/stopdiscovery(session:).md) implementation to instruct it to perform any cleanup.

## Topics

### Controlling discovery
- [func startDiscovery(session: DDDiscoverySession)](dddiscoveryextension/startdiscovery(session:).md)
  Begins the extension’s device discovery process.
- [func stopDiscovery(session: DDDiscoverySession)](dddiscoveryextension/stopdiscovery(session:).md)
  Ends the extension’s device discovery process.
### Observing state changes
- [func didReceiveEvent(DDDeviceEvent)](dddiscoveryextension/didreceiveevent(_:).md)
  Provides a device event from the system to the extension.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)

## See Also

- [class DDDiscoverySession](dddiscoverysession.md)
  An object that relays device discovery events from the extension to the system.
- [class DDDiscoveryExtensionConfiguration](dddiscoveryextensionconfiguration.md)
  An object that manages the extension’s communication with the framework.
- [protocol DDDiscoveryExtensionConfigurationProtocol](dddiscoveryextensionconfigurationprotocol.md)
  A specification that provides a communication channel between the extension and the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoveryextension)*