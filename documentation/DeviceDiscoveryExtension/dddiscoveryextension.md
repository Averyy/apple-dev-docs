# DDDiscoveryExtension

**Framework**: DeviceDiscoveryExtension  
**Kind**: protocol  
**Role**: Protocol

A specification that enables the framework to start and stop the extension’s discovery process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst
- macOS 13.0+
- visionOS

## Declaration

```swift
protocol DDDiscoveryExtension : AppExtension
```

## Overview

Your extension adopts this protocol as the primary entry and exit points for device discovery.

The system calls your extension’s [`startDiscovery(session:)`](./dddiscoveryextension/startdiscovery%28session%29.md) when [`AVRoutePickerView`](../AVKit/avroutepickerview.md) displays so your extension can include a specific third-party device in the picker. When the picker UI dismisses or the user selects a device, the system calls your extension’s [`stopDiscovery(session:)`](./dddiscoveryextension/stopdiscovery%28session%29.md) implementation to instruct it to perform any cleanup.

## Topics

### Controlling discovery
- [func startDiscovery(session: DDDiscoverySession)](./dddiscoveryextension/startdiscovery%28session%29.md)
  Begins the extension’s device discovery process.
- [func stopDiscovery(session: DDDiscoverySession)](./dddiscoveryextension/stopdiscovery%28session%29.md)
  Ends the extension’s device discovery process.
### Observing state changes
- [func didReceiveEvent(DDDeviceEvent)](./dddiscoveryextension/didreceiveevent%28_%29.md)
  Provides a device event from the system to the extension.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/appextension.md)

## See Also

### Extension
- [class DDDiscoverySession](./dddiscoverysession.md)
  An object that relays device discovery events from the extension to the system.
- [protocol DDDiscoveryExtensionConfigurationProtocol](./dddiscoveryextensionconfigurationprotocol.md)
  A specification that provides a communication channel between the extension and the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoveryextension)*