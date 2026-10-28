# DDDiscoveryExtensionConfigurationProtocol

**Framework**: DeviceDiscoveryExtension  
**Kind**: protocol  
**Role**: Protocol

A specification that provides a communication channel between the extension and the framework.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst
- macOS 13.0+
- visionOS

## Declaration

```swift
protocol DDDiscoveryExtensionConfigurationProtocol : AppExtensionConfiguration
```

## Overview

The `DDDiscoveryExtensionConfiguration` class adopts this protocol. For an example, see `Appex.swift` in [Discovering a third-party media-streaming device](./discovering-a-third-party-media-streaming-device.md).

## Relationships

### Inherits From
- [AppExtensionConfiguration](../ExtensionFoundation/appextensionconfiguration.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Extension
- [protocol DDDiscoveryExtension](./dddiscoveryextension.md)
  A specification that enables the framework to start and stop the extension’s discovery process.
- [class DDDiscoverySession](./dddiscoverysession.md)
  An object that relays device discovery events from the extension to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoveryextensionconfigurationprotocol)*