# NWInterface

**Framework**: Network  
**Kind**: struct

An interface that a network connection uses to send and receive data.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
struct NWInterface
```

## Topics

### Inspecting Interfaces
- [var type: NWInterface.InterfaceType](nwinterface/type.md)
  The type of the interface, such as Wi-Fi or loopback.
- [NWInterface.InterfaceType](nwinterface/interfacetype.md)
  Types of network interfaces, based on their link layer media types.
- [var name: String](nwinterface/name.md)
  The name of the interface.
- [var index: Int](nwinterface/index.md)
  The system interface index associated with the interface.
### Enumerations
- [NWInterface.RadioType](nwinterface/radiotype.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct NWPath](nwpath.md)
  An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- [class NWPathMonitor](nwpathmonitor.md)
  An observer that you use to monitor and react to network changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwinterface)*