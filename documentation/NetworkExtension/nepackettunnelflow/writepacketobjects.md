# writePacketObjects(_:)

**Framework**: Network Extension  
**Kind**: method

Write multiple IP packets to the TUN interface.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func writePacketObjects(_ packets: [NEPacket]) -> Bool
```

## See Also

- [func readPacketObjects(completionHandler: ([NEPacket]) -> Void)](nepackettunnelflow/readpacketobjects(completionhandler:).md)
  Read multiple IP packets from the TUN interface.
- [func readPackets(completionHandler: ([Data], [NSNumber]) -> Void)](nepackettunnelflow/readpackets(completionhandler:).md)
  Reads IP packets from the TUN interface.
- [func writePackets([Data], withProtocols: [NSNumber]) -> Bool](nepackettunnelflow/writepackets(_:withprotocols:).md)
  Writes IP packets to the TUN interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelflow/writepacketobjects(_:))*