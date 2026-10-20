# writePackets(_:withProtocols:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) writePackets:(NSArray<NSData *> *) packets withProtocols:(NSArray<NSNumber *> *) protocols;
```

#### Discussion

The number of NSData objects in `packets` must be exactly equal to the number of NSNumber objects in `protocols`.

## Parameters

- `packets`: An array of NSData objects containing the IP packets to the written.
- `protocols`: An array of NSNumber objects containing the protocol numbers (e.g. AF_INET or AF_INET6) of the IP packets in `packets` in host byte order.

## See Also

### Handling IP packets
- [func readPacketObjects(completionHandler: ([NEPacket]) -> Void)](./readpacketobjects%28completionhandler%29.md)
  Read multiple IP packets from the TUN interface.
- [func writePacketObjects([NEPacket]) -> Bool](./writepacketobjects%28_%29.md)
  Write multiple IP packets to the TUN interface.
- [func readPackets(completionHandler: ([Data], [NSNumber]) -> Void)](./readpackets%28completionhandler%29.md)
  Reads IP packets from the TUN interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelflow/writepackets(_:withprotocols:))*