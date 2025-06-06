# init(destinationNetwork:prefix:protocol:)

**Framework**: Network Extension  
**Kind**: init

Creates a rule that matches network traffic destined for a host within a specific network.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(destinationNetwork networkEndpoint: NWHostEndpoint, prefix destinationPrefix: Int, protocol: NENetworkRule.Protocol)
```

#### Discussion

If the port string of `networkEndpoint` is `0` or the empty string, the rule matches traffic on any port destined for the given address or network.

## Parameters

- `networkEndpoint`: An endpoint instance that matches the port and address or network that the rule matches. This endpoint must contain an address, not a hostname.
- `destinationPrefix`: An integer that in combination with the address in the endpoint specifies the destination network that the rule matches.
- `protocol`: The protocol that the rule matches.

## See Also

- [init(destinationHost: NWHostEndpoint, protocol: NENetworkRule.Protocol)](nenetworkrule/init(destinationhost:protocol:).md)
  Creates a rule that matches network traffic destined for a host within a specific DNS domain.
- [init(remoteNetwork: NWHostEndpoint?, remotePrefix: Int, localNetwork: NWHostEndpoint?, localPrefix: Int, protocol: NENetworkRule.Protocol, direction: NETrafficDirection)](nenetworkrule/init(remotenetwork:remoteprefix:localnetwork:localprefix:protocol:direction:).md)
  Creates a rule that matches traffic by remote network, local network, protocol, and direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nenetworkrule/init(destinationnetwork:prefix:protocol:))*