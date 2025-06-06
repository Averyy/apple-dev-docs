# NEPacket

**Framework**: Network Extension  
**Kind**: class

A network packet and its associated properties.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEPacket
```

## Topics

### Initializing a packet
- [init(data: Data, protocolFamily: sa_family_t)](nepacket/init(data:protocolfamily:).md)
### Accessing packet properties
- [var data: Data](nepacket/data.md)
- [var metadata: NEFlowMetaData?](nepacket/metadata.md)
- [var protocolFamily: sa_family_t](nepacket/protocolfamily.md)
- [var direction: NETrafficDirection](nepacket/direction.md)
  The direction of the packet.
- [enum NETrafficDirection](netrafficdirection.md)
  A type to represent the direction of network traffic.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NEPacketTunnelFlow](nepackettunnelflow.md)
  An object you use to read and write packets to and from the tunnel’s virtual interface.
- [In-Provider Networking](in-provider-networking.md)
  Network APIs for use by all types of NetworkExtension providers and by hotspot helpers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepacket)*