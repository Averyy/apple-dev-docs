# writePackets(_:withProtocols:)

**Framework**: Network Extension  
**Kind**: method

Writes IP packets to the TUN interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func writePackets(_ packets: [Data], withProtocols protocols: [NSNumber]) -> Bool
```

#### Discussion

The number of NSData objects in `packets` must be exactly equal to the number of NSNumber objects in `protocols`.

## Parameters

- `packets`: An array of NSData objects containing the IP packets to the written.
- `protocols`: An array of NSNumber objects containing the protocol numbers (e.g. AF_INET or AF_INET6) of the IP packets in   in host byte order.

## See Also

- [func readPacketObjects(completionHandler: ([NEPacket]) -> Void)](nepackettunnelflow/readpacketobjects(completionhandler:).md)
  Read multiple IP packets from the TUN interface.
- [func writePacketObjects([NEPacket]) -> Bool](nepackettunnelflow/writepacketobjects(_:).md)
  Write multiple IP packets to the TUN interface.
- [func readPackets(completionHandler: ([Data], [NSNumber]) -> Void)](nepackettunnelflow/readpackets(completionhandler:).md)
  Reads IP packets from the TUN interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelflow/writepackets(_:withprotocols:))*