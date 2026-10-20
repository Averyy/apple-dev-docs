# readPacketObjects(completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Read multiple IP packets from the TUN interface.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func readPacketObjects(completionHandler: @escaping @Sendable ([NEPacket]) -> Void)
```

```swift
func readPacketObjects() async -> [NEPacket]
```

```objc
- (void) readPacketObjectsWithCompletionHandler:(void (^)(NSArray<NEPacket *> *packets)) completionHandler;
```

## See Also

### Handling IP packets
- [func writePacketObjects([NEPacket]) -> Bool](./writepacketobjects%28_%29.md)
  Write multiple IP packets to the TUN interface.
- [func readPackets(completionHandler: ([Data], [NSNumber]) -> Void)](./readpackets%28completionhandler%29.md)
  Reads IP packets from the TUN interface.
- [func writePackets([Data], withProtocols: [NSNumber]) -> Bool](./writepackets%28_,withprotocols%29.md)
  Writes IP packets to the TUN interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelflow/readpacketobjects(completionhandler:))*