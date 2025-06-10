# NETrafficDirection

**Framework**: Network Extension  
**Kind**: enum

A type to represent the direction of network traffic.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum NETrafficDirection
```

## Topics

### Directions
- [NETrafficDirection.inbound](netrafficdirection/inbound.md)
  The inbound traffic direction.
- [NETrafficDirection.outbound](netrafficdirection/outbound.md)
  The outbound traffic direction.
- [NETrafficDirection.any](netrafficdirection/any.md)
  A direction that matches either inbound or outbound traffic.
### Initializers
- [init?(rawValue: Int)](netrafficdirection/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var matchRemoteEndpoint: NWHostEndpoint?](nenetworkrule/matchremoteendpoint.md)
  The remote endpoint that the rule matches.
- [var matchRemotePrefix: Int](nenetworkrule/matchremoteprefix.md)
  A number that specifies the remote sub-network that the rule matches.
- [var matchLocalNetwork: NWHostEndpoint?](nenetworkrule/matchlocalnetwork.md)
  The local network that the rule matches.
- [var matchLocalPrefix: Int](nenetworkrule/matchlocalprefix.md)
  A number that specifies the local sub-network that the rule matches.
- [var matchProtocol: NENetworkRule.Protocol](nenetworkrule/matchprotocol.md)
  The protocol that the rule matches.
- [NENetworkRule.Protocol](nenetworkrule/protocol.md)
  A type to represent network protocols used by routing rules.
- [var matchDirection: NETrafficDirection](nenetworkrule/matchdirection.md)
  The direction of network traffic that the rule matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netrafficdirection)*