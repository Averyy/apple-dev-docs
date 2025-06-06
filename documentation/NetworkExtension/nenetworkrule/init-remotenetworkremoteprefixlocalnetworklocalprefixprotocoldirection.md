# init(remoteNetwork:remotePrefix:localNetwork:localPrefix:protocol:direction:)

**Framework**: Network Extension  
**Kind**: init

Creates a rule that matches traffic by remote network, local network, protocol, and direction.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(remoteNetwork: NWHostEndpoint?, remotePrefix: Int, localNetwork: NWHostEndpoint?, localPrefix: Int, protocol: NENetworkRule.Protocol, direction: NETrafficDirection)
```

#### Discussion

If the port string of `remoteNetwork` is `0` or the empty string, then the rule matches traffic on any port coming from the remote network. If `remoteNetwork` is `nil`, the rule matches any remote network.

If the port string of `localNetwork` is `0` or the empty string, then the rule matches traffic on any port coming from the local network. If `localNetwork` is `nil`, the rule matches any local network.

## Parameters

- `remoteNetwork`: An endpoint instance that contains the remote port and the remote address or network that the rule matches. This endpoint must contain an address, not a hostname.
- `remotePrefix`: An integer that in combination with the address in   specifies the remote network that the rule matches.
- `localNetwork`: An endpoint instance that contains the local port and the local address or network that the rule matches. This endpoint must contain an address, not a hostname.
- `localPrefix`: An integer that in combination with the address in localNetwork specifies the local network that the rule matches. The rule ignores this parameter if   is  .
- `protocol`: The protocol that the rule matches.
- `direction`: The direction of network traffic that the rule matches.

## See Also

- [init(destinationNetwork: NWHostEndpoint, prefix: Int, protocol: NENetworkRule.Protocol)](nenetworkrule/init(destinationnetwork:prefix:protocol:).md)
  Creates a rule that matches network traffic destined for a host within a specific network.
- [init(destinationHost: NWHostEndpoint, protocol: NENetworkRule.Protocol)](nenetworkrule/init(destinationhost:protocol:).md)
  Creates a rule that matches network traffic destined for a host within a specific DNS domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nenetworkrule/init(remotenetwork:remoteprefix:localnetwork:localprefix:protocol:direction:))*