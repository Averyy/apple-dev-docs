# DDDiscoveryExtensionConfigurationProtocol

**Framework**: DeviceDiscoveryExtension  
**Kind**: protocol

A specification that provides a communication channel between the extension and the framework.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
protocol DDDiscoveryExtensionConfigurationProtocol : AppExtensionConfiguration
```

#### Overview

The [`DDDiscoveryExtensionConfiguration`](dddiscoveryextensionconfiguration.md) class adopts this protocol. For an example, see `Appex.swift` in [`Discovering a third-party media-streaming device`](discovering-a-third-party-media-streaming-device.md).

## Relationships

### Inherits From
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [DDDiscoveryExtensionConfiguration](dddiscoveryextensionconfiguration.md)

## See Also

- [protocol DDDiscoveryExtension](dddiscoveryextension.md)
  A specification that enables the framework to start and stop the extension’s discovery process.
- [class DDDiscoverySession](dddiscoverysession.md)
  An object that relays device discovery events from the extension to the system.
- [class DDDiscoveryExtensionConfiguration](dddiscoveryextensionconfiguration.md)
  An object that manages the extension’s communication with the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoveryextensionconfigurationprotocol)*