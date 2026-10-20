# matchRemoteEndpoint

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The remote endpoint that the rule matches.

**Availability**:
- macOS 10.15+ - Deprecated in 15.0

## Declaration

```swift
var matchRemoteEndpoint: NWHostEndpoint? { get }
```

```objc
@property (readonly, nullable) NWHostEndpoint * matchRemoteEndpoint;
```

## See Also

### Matching network traffic characteristics
- [var matchRemotePrefix: Int](./matchremoteprefix.md)
  A number that specifies the remote sub-network that the rule matches.
- [var matchLocalNetwork: NWHostEndpoint?](./matchlocalnetwork.md)
  The local network that the rule matches.
- [var matchLocalPrefix: Int](./matchlocalprefix.md)
  A number that specifies the local sub-network that the rule matches.
- [var matchProtocol: NENetworkRule.Protocol](./matchprotocol.md)
  The protocol that the rule matches.
- [NENetworkRule.Protocol](./protocol.md)
  A type to represent network protocols used by routing rules.
- [var matchDirection: NETrafficDirection](./matchdirection.md)
  The direction of network traffic that the rule matches.
- [enum NETrafficDirection](../netrafficdirection.md)
  A type to represent the direction of network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nenetworkrule/matchremoteendpoint)*