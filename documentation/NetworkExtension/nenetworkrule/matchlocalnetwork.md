# matchLocalNetwork

**Framework**: Network Extension  
**Kind**: property

The local network that the rule matches.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var matchLocalNetwork: NWHostEndpoint? { get }
```

## See Also

- [var matchRemoteEndpoint: NWHostEndpoint?](nenetworkrule/matchremoteendpoint.md)
  The remote endpoint that the rule matches.
- [var matchRemotePrefix: Int](nenetworkrule/matchremoteprefix.md)
  A number that specifies the remote sub-network that the rule matches.
- [var matchLocalPrefix: Int](nenetworkrule/matchlocalprefix.md)
  A number that specifies the local sub-network that the rule matches.
- [var matchProtocol: NENetworkRule.Protocol](nenetworkrule/matchprotocol.md)
  The protocol that the rule matches.
- [NENetworkRule.Protocol](nenetworkrule/protocol.md)
  A type to represent network protocols used by routing rules.
- [var matchDirection: NETrafficDirection](nenetworkrule/matchdirection.md)
  The direction of network traffic that the rule matches.
- [enum NETrafficDirection](netrafficdirection.md)
  A type to represent the direction of network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nenetworkrule/matchlocalnetwork)*