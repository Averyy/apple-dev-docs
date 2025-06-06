# NEFilterPacketHandler

**Framework**: Network Extension  
**Kind**: typealias

A type for Swift closures or ObjectiveC blocks that make filtering decisions about network packets.

**Availability**:
- macOS 10.15+

## Declaration

```swift
typealias NEFilterPacketHandler = (NEFilterPacketContext, nw_interface_t, NETrafficDirection, UnsafeRawPointer, Int) -> NEFilterPacketProvider.Verdict
```

#### Return Value

A verdict on whether the framework should allow, drop, or delay the packet. If the verdict is [`NEFilterPacketProvider.Verdict.delay`](nefilterpacketprovider/verdict/delay.md), the framework assumes the handler already called [`delayCurrentPacket(_:)`](nefilterpacketprovider/delaycurrentpacket(_:).md).

## Parameters

- `context`: The current filtering context.
- `interface`: The ingress or egress interface of the packet.
- `direction`: The direction the packet is flowing.
- `packetBytes`: The packet’s bytes.
- `packetLength`: The length of the packet’s bytes.

## See Also

- [var packetHandler: NEFilterPacketHandler?](nefilterpacketprovider/packethandler.md)
  A Swift closure or an ObjectiveC block that handles each packet received by the filter.
- [class NEFilterPacketContext](nefilterpacketcontext.md)
  The context object provided to the filter packet handler.
- [enum NETrafficDirection](netrafficdirection.md)
  A type to represent the direction of network traffic.
- [NEFilterPacketProvider.Verdict](nefilterpacketprovider/verdict.md)
  The verdict returned by a packet handler indicating what the framework should do with a packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterpackethandler)*