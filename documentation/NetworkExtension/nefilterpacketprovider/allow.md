# allow(_:)

**Framework**: Network Extension  
**Kind**: method

Allow delivery of a previously-delayed packet.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func allow(_ packet: NEPacket)
```

#### Discussion

Use this method to allow a previously-delayed packet to continue its journey into or out of the networking stack.

## Parameters

- `packet`: The packet previously delayed by the packet handler.

## See Also

- [func delayCurrentPacket(NEFilterPacketContext) -> NEPacket](nefilterpacketprovider/delaycurrentpacket(_:).md)
  Delay a packet currently processed by a packet handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterpacketprovider/allow(_:))*