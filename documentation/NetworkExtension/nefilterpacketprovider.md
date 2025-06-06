# NEFilterPacketProvider

**Framework**: Network Extension  
**Kind**: class

A filter provider that evaluates network packets and decides whether to block, allow, or delay the packets.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NEFilterPacketProvider
```

## Topics

### Filtering packets
- [var packetHandler: NEFilterPacketHandler?](nefilterpacketprovider/packethandler.md)
  A Swift closure or an ObjectiveC block that handles each packet received by the filter.
- [typealias NEFilterPacketHandler](nefilterpackethandler.md)
  A type for Swift closures or ObjectiveC blocks that make filtering decisions about network packets.
- [class NEFilterPacketContext](nefilterpacketcontext.md)
  The context object provided to the filter packet handler.
- [enum NETrafficDirection](netrafficdirection.md)
  A type to represent the direction of network traffic.
- [NEFilterPacketProvider.Verdict](nefilterpacketprovider/verdict.md)
  The verdict returned by a packet handler indicating what the framework should do with a packet.
### Delaying packets
- [func delayCurrentPacket(NEFilterPacketContext) -> NEPacket](nefilterpacketprovider/delaycurrentpacket(_:).md)
  Delay a packet currently processed by a packet handler.
- [func allow(NEPacket)](nefilterpacketprovider/allow(_:).md)
  Allow delivery of a previously-delayed packet.
### Instance Properties
- [var handler: ((NEFilterPacketContext, NWInterface, NETrafficDirection, UnsafeRawBufferPointer) -> NEFilterPacketProvider.Verdict)?](nefilterpacketprovider/handler.md)

## Relationships

### Inherits From
- [NEFilterProvider](nefilterprovider.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NEFilterDataProvider](nefilterdataprovider.md)
  The principal class for a filter data provider extension.
- [class NEFilterControlProvider](nefiltercontrolprovider.md)
  The principal class for a filter control provider extension.
- [class NEFilterProvider](nefilterprovider.md)
  An abstract base class shared by content filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterpacketprovider)*