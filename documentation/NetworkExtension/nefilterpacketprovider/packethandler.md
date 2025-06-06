# packetHandler

**Framework**: Network Extension  
**Kind**: property

A Swift closure or an ObjectiveC block that handles each packet received by the filter.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var packetHandler: NEFilterPacketHandler? { get set }
```

#### Discussion

Set this property to a handler that returns a [`NEFilterPacketProvider.Verdict`](nefilterpacketprovider/verdict.md) for each packet it receives.

Since there may be multiple filtering sources presenting frames to the provider, multiple simultaneous threads may execute this packet handler. Therefore, the packet handler must be able to handle execution in a multi-threaded environment.

## See Also

- [typealias NEFilterPacketHandler](nefilterpackethandler.md)
  A type for Swift closures or ObjectiveC blocks that make filtering decisions about network packets.
- [class NEFilterPacketContext](nefilterpacketcontext.md)
  The context object provided to the filter packet handler.
- [enum NETrafficDirection](netrafficdirection.md)
  A type to represent the direction of network traffic.
- [NEFilterPacketProvider.Verdict](nefilterpacketprovider/verdict.md)
  The verdict returned by a packet handler indicating what the framework should do with a packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterpacketprovider/packethandler)*