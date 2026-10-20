# DDDiscoverySession

**Framework**: DeviceDiscoveryExtension  
**Kind**: class  
**Role**: Class

An object that relays device discovery events from the extension to the system.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
class DDDiscoverySession
```

```objc
@interface DDDiscoverySession : NSObject
```

#### Overview

The system passes the extension an instance of this class when it attempts to discover a device. Device discovery starts when an app displays [`AVRoutePickerView`](../AVKit/avroutepickerview.md) and the system calls the extension’s `startDiscovery(session:)` implementation.

## Topics

### Providing an event to the system
- [func report(DDDeviceEvent)](./dddiscoverysession/report%28_%29.md)
  Reports an event to the system.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Extension
- [protocol DDDiscoveryExtension](./dddiscoveryextension.md)
  A specification that enables the framework to start and stop the extension’s discovery process.
- [protocol DDDiscoveryExtensionConfigurationProtocol](./dddiscoveryextensionconfigurationprotocol.md)
  A specification that provides a communication channel between the extension and the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoverysession)*