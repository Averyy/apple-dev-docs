# NEFilterPacketProvider

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

A filter provider that evaluates network packets and decides whether to block, allow, or delay the packets.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NEFilterPacketProvider
```

```objc
@interface NEFilterPacketProvider : NEFilterProvider
```

## Topics

### Filtering packets
- [var packetHandler: NEFilterPacketHandler?](./nefilterpacketprovider/packethandler.md)
  A Swift closure or an ObjectiveC block that handles each packet received by the filter.
- [typealias NEFilterPacketHandler](./nefilterpackethandler.md)
  A type for Swift closures or ObjectiveC blocks that make filtering decisions about network packets.
- [class NEFilterPacketContext](./nefilterpacketcontext.md)
  The context object provided to the filter packet handler.
- [enum NETrafficDirection](./netrafficdirection.md)
  A type to represent the direction of network traffic.
- [NEFilterPacketProvider.Verdict](./nefilterpacketprovider/verdict.md)
  The verdict returned by a packet handler indicating what the framework should do with a packet.
### Delaying packets
- [func delayCurrentPacket(NEFilterPacketContext) -> NEPacket](./nefilterpacketprovider/delaycurrentpacket%28_%29.md)
  Delay a packet currently processed by a packet handler.
- [func allow(NEPacket)](./nefilterpacketprovider/allow%28_%29.md)
  Allow delivery of a previously-delayed packet.
### Instance Properties
- [var handler: ((NEFilterPacketContext, NWInterface, NETrafficDirection, UnsafeRawBufferPointer) -> NEFilterPacketProvider.Verdict)?](./nefilterpacketprovider/handler.md)

## Relationships

### Inherits From
- [NEFilterProvider](./nefilterprovider.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Data and control providers
- [class NEFilterDataProvider](./nefilterdataprovider.md)
  The principal class for a filter data provider extension.
- [class NEFilterControlProvider](./nefiltercontrolprovider.md)
  The principal class for a filter control provider extension.
- [class NEFilterProvider](./nefilterprovider.md)
  An abstract base class shared by content filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterpacketprovider)*