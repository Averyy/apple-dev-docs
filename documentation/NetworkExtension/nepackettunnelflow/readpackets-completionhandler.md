# readPackets(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Reads IP packets from the TUN interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func readPackets() async -> ([Data], [NSNumber])
```

#### Discussion

Each call to this method results in a single execution of the completion handler. The caller should call this method after each `completionHandler` execution in order to continue to receive packets from the TUN interface.

## Parameters

- `completionHandler`: A Swift closure or an ObjectiveC block that runs when some packets are read from the TUN interface.   The packets that were read are passed to this block in the   array.   The protocol numbers of the packets that were read are passed to this block in the   array.   Each packet has a protocol number in the corresponding index in the   array.   The protocol numbers are given in host byte order.   Valid protocol numbers include   and  .   See  .

## See Also

- [func readPacketObjects(completionHandler: ([NEPacket]) -> Void)](nepackettunnelflow/readpacketobjects(completionhandler:).md)
  Read multiple IP packets from the TUN interface.
- [func writePacketObjects([NEPacket]) -> Bool](nepackettunnelflow/writepacketobjects(_:).md)
  Write multiple IP packets to the TUN interface.
- [func writePackets([Data], withProtocols: [NSNumber]) -> Bool](nepackettunnelflow/writepackets(_:withprotocols:).md)
  Writes IP packets to the TUN interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelflow/readpackets(completionhandler:))*