# NEPacketTunnelFlow

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

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

```objc
@interface NEPacketTunnelFlow : NSObject
```

## Overview

Use the `NEPacketTunnelFlow` class to implement a custom-IP tunneling protocol for your packet tunnel. For example, use the APIs in this class to read packets from the virtual interface, so you can then encapsulate these packets and send them to a packet-tunnel server. Likewise, read packets from your packet-tunnel server and use these APIs to write the packets back to the tunnel’s virtual interface.

## Topics

### Handling IP packets
- [func readPacketObjects(completionHandler: ([NEPacket]) -> Void)](./nepackettunnelflow/readpacketobjects%28completionhandler%29.md)
  Read multiple IP packets from the TUN interface.
- [func writePacketObjects([NEPacket]) -> Bool](./nepackettunnelflow/writepacketobjects%28_%29.md)
  Write multiple IP packets to the TUN interface.
- [func readPackets(completionHandler: ([Data], [NSNumber]) -> Void)](./nepackettunnelflow/readpackets%28completionhandler%29.md)
  Reads IP packets from the TUN interface.
- [func writePackets([Data], withProtocols: [NSNumber]) -> Bool](./nepackettunnelflow/writepackets%28_,withprotocols%29.md)
  Writes IP packets to the TUN interface.

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

### Packet handling
- [class NEPacket](./nepacket.md)
  A network packet and its associated properties.
- [In-Provider Networking](./in-provider-networking.md)
  Network APIs for use by all types of NetworkExtension providers and by hotspot helpers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelflow)*