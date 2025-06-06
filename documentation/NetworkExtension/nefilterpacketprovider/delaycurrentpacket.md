# delayCurrentPacket(_:)

**Framework**: Network Extension  
**Kind**: method

Delay a packet currently processed by a packet handler.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func delayCurrentPacket(_ context: NEFilterPacketContext) -> NEPacket
```

#### Discussion

This function is only valid within the [`packetHandler`](nefilterpacketprovider/packethandler.md) Swift closure or ObjectiveC block, which must return [`NEFilterPacketProvider.Verdict.delay`](nefilterpacketprovider/verdict/delay.md) after delaying the packet. The framework prevents further delivery of the packet through the network stack until it’s allowed or dropped. Allow the packet by calling [`allow(_:)`](nefilterpacketprovider/allow(_:).md), or drop it by releasing it.

## Parameters

- `context`: A context for the packet handler.

## See Also

- [func allow(NEPacket)](nefilterpacketprovider/allow(_:).md)
  Allow delivery of a previously-delayed packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterpacketprovider/delaycurrentpacket(_:))*