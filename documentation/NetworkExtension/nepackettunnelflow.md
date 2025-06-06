# NEPacketTunnelFlow

**Framework**: Network Extension  
**Kind**: class

An object you use to read and write packets to and from the tunnel’s virtual interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEPacketTunnelFlow
```

#### Overview

Use the `NEPacketTunnelFlow` class to implement a custom-IP tunneling protocol for your packet tunnel. For example, use the APIs in this class to read packets from the virtual interface, so you can then encapsulate these packets and send them to a packet-tunnel server. Likewise, read packets from your packet-tunnel server and use these APIs to write the packets back to the tunnel’s virtual interface.

## Topics

### Handling IP packets
- [func readPacketObjects(completionHandler: ([NEPacket]) -> Void)](nepackettunnelflow/readpacketobjects(completionhandler:).md)
  Read multiple IP packets from the TUN interface.
- [func writePacketObjects([NEPacket]) -> Bool](nepackettunnelflow/writepacketobjects(_:).md)
  Write multiple IP packets to the TUN interface.
- [func readPackets(completionHandler: ([Data], [NSNumber]) -> Void)](nepackettunnelflow/readpackets(completionhandler:).md)
  Reads IP packets from the TUN interface.
- [func writePackets([Data], withProtocols: [NSNumber]) -> Bool](nepackettunnelflow/writepackets(_:withprotocols:).md)
  Writes IP packets to the TUN interface.

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

- [class NEPacket](nepacket.md)
  A network packet and its associated properties.
- [In-Provider Networking](in-provider-networking.md)
  Network APIs for use by all types of NetworkExtension providers and by hotspot helpers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelflow)*