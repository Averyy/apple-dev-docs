# DDDiscoveryExtensionConfiguration

**Framework**: DeviceDiscoveryExtension  
**Kind**: class

An object that manages the extension’s communication with the framework.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class DDDiscoveryExtensionConfiguration<T> where T : DDDiscoveryExtension
```

#### Overview

Your app’s primary extension class provides a property of this type. Create the instance by calling [`init(discoveryExtension:)`](dddiscoveryextensionconfiguration/init(discoveryextension:).md) with the argument set to `self`.

## Topics

### Creating an extension configuration
- [init(discoveryExtension: T)](dddiscoveryextensionconfiguration/init(discoveryextension:).md)
  Creates an extension configuration with a reference to a specific extension.

## Relationships

### Conforms To
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [DDDiscoveryExtensionConfigurationProtocol](dddiscoveryextensionconfigurationprotocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol DDDiscoveryExtension](dddiscoveryextension.md)
  A specification that enables the framework to start and stop the extension’s discovery process.
- [class DDDiscoverySession](dddiscoverysession.md)
  An object that relays device discovery events from the extension to the system.
- [protocol DDDiscoveryExtensionConfigurationProtocol](dddiscoveryextensionconfigurationprotocol.md)
  A specification that provides a communication channel between the extension and the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoveryextensionconfiguration)*