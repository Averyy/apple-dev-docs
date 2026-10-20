# allow(_:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Allow delivery of a previously-delayed packet.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func allow(_ packet: NEPacket)
```

```objc
- (void) allowPacket:(NEPacket *) packet;
```

#### Discussion

Use this method to allow a previously-delayed packet to continue its journey into or out of the networking stack.

## Parameters

- `packet`: The packet previously delayed by the packet handler.

## See Also

### Delaying packets
- [func delayCurrentPacket(NEFilterPacketContext) -> NEPacket](./delaycurrentpacket%28_%29.md)
  Delay a packet currently processed by a packet handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterpacketprovider/allow(_:))*