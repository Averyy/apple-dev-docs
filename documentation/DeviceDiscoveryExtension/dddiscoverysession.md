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

The system passes the extension an instance of this class when it attempts to discover a device. Device discovery starts when an app displays [`AVRoutePickerView`](https://developer.apple.com/documentation/avkit/avroutepickerview) and the system calls the extension’s `startDiscovery(session:)` implementation.

## Topics

### Providing an event to the system
- [func report(DDDeviceEvent)](dddiscoverysession/report(_:).md)
  Reports an event to the system.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [protocol DDDiscoveryExtension](dddiscoveryextension.md)
  A specification that enables the framework to start and stop the extension’s discovery process.
- [protocol DDDiscoveryExtensionConfigurationProtocol](dddiscoveryextensionconfigurationprotocol.md)
  A specification that provides a communication channel between the extension and the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoverysession)*