# NENetworkRule.Protocol

**Framework**: Network Extension  
**Kind**: enum

A type to represent network protocols used by routing rules.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum `Protocol`
```

## Topics

### Protocols
- [NENetworkRule.Protocol.TCP](nenetworkrule/protocol/tcp.md)
  A rule protocol to match TCP traffic.
- [NENetworkRule.Protocol.UDP](nenetworkrule/protocol/udp.md)
  A rule protocol to match UDP traffic.
- [NENetworkRule.Protocol.any](nenetworkrule/protocol/any.md)
  A rule protocol to match TCP and UDP traffic.
### Initializers
- [init?(rawValue: Int)](nenetworkrule/protocol/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [var matchDirection: NETrafficDirection](nenetworkrule/matchdirection.md)
  The direction of network traffic that the rule matches.
- [enum NETrafficDirection](netrafficdirection.md)
  A type to represent the direction of network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nenetworkrule/protocol)*