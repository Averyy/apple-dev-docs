# DDDiscoverySession

**Framework**: DeviceDiscoveryExtension  
**Kind**: class

An object that relays device discovery events from the extension to the system.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
class DDDiscoverySession
```

#### Overview

The system passes the extension an instance of this class when it attempts to discover a device. Device discovery starts when an app displays [`AVRoutePickerView`](https://developer.apple.com/documentation/AVKit/AVRoutePickerView) and the system calls the extension’s `startDiscovery(session:)` implementation.

## Topics

### Providing an event to the system
- [func report(DDDeviceEvent)](dddiscoverysession/report(_:).md)
  Reports an event to the system.

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

- [protocol DDDiscoveryExtension](dddiscoveryextension.md)
  A specification that enables the framework to start and stop the extension’s discovery process.
- [class DDDiscoveryExtensionConfiguration](dddiscoveryextensionconfiguration.md)
  An object that manages the extension’s communication with the framework.
- [protocol DDDiscoveryExtensionConfigurationProtocol](dddiscoveryextensionconfigurationprotocol.md)
  A specification that provides a communication channel between the extension and the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoverysession)*