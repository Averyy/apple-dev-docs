# init(destinationNetwork:prefix:protocol:)

**Framework**: Network Extension  
**Kind**: init  
**Role**: Initializer

Creates a rule that matches network traffic destined for a host within a specific network.

**Availability**:
- macOS 10.15+ - Deprecated in 15.0

## Declaration

```swift
init(destinationNetwork networkEndpoint: NWHostEndpoint, prefix destinationPrefix: Int, protocol: NENetworkRule.Protocol)
```

```objc
- (instancetype) initWithDestinationNetwork:(NWHostEndpoint *) networkEndpoint prefix:(NSUInteger) destinationPrefix protocol:(NENetworkRuleProtocol) protocol;
```

## Discussion

If the port string of `networkEndpoint` is `0` or the empty string, the rule matches traffic on any port destined for the given address or network.

## Parameters

- `networkEndpoint`: An endpoint instance that matches the port and address or network that the rule matches. This endpoint must contain an address, not a hostname.
- `destinationPrefix`: An integer that in combination with the address in the endpoint specifies the destination network that the rule matches.
- `protocol`: The protocol that the rule matches.

## See Also

### Creating a network rule
- [init(destinationHost: NWHostEndpoint, protocol: NENetworkRule.Protocol)](./init%28destinationhost,protocol%29.md)
  Creates a rule that matches network traffic destined for a host within a specific DNS domain.
- [init(remoteNetwork: NWHostEndpoint?, remotePrefix: Int, localNetwork: NWHostEndpoint?, localPrefix: Int, protocol: NENetworkRule.Protocol, direction: NETrafficDirection)](./init%28remotenetwork,remoteprefix,localnetwork,localprefix,protocol,direction%29.md)
  Creates a rule that matches traffic by remote network, local network, protocol, and direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nenetworkrule/init(destinationnetwork:prefix:protocol:))*