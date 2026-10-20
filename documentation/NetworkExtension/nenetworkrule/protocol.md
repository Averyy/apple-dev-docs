# NENetworkRule.Protocol

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

A type to represent network protocols used by routing rules.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum `Protocol`
```

```c
enum NENetworkRuleProtocol : NSInteger;
```

## Topics

### Protocols
- [NENetworkRule.Protocol.TCP](./protocol/tcp.md)
  A rule protocol to match TCP traffic.
- [NENetworkRule.Protocol.UDP](./protocol/udp.md)
  A rule protocol to match UDP traffic.
- [NENetworkRule.Protocol.any](./protocol/any.md)
  A rule protocol to match TCP and UDP traffic.
### Initializers
- [init?(rawValue: Int)](./protocol/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Matching network traffic characteristics
- [var matchRemoteEndpoint: NWHostEndpoint?](./matchremoteendpoint.md)
  The remote endpoint that the rule matches.
- [var matchRemotePrefix: Int](./matchremoteprefix.md)
  A number that specifies the remote sub-network that the rule matches.
- [var matchLocalNetwork: NWHostEndpoint?](./matchlocalnetwork.md)
  The local network that the rule matches.
- [var matchLocalPrefix: Int](./matchlocalprefix.md)
  A number that specifies the local sub-network that the rule matches.
- [var matchProtocol: NENetworkRule.Protocol](./matchprotocol.md)
  The protocol that the rule matches.
- [var matchDirection: NETrafficDirection](./matchdirection.md)
  The direction of network traffic that the rule matches.
- [enum NETrafficDirection](../netrafficdirection.md)
  A type to represent the direction of network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nenetworkrule/protocol)*