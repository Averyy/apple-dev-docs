# NENetworkRule

**Framework**: Network Extension  
**Kind**: class

A rule to match attributes of network traffic.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NENetworkRule
```

## Topics

### Creating a network rule
- [init(destinationNetwork: NWHostEndpoint, prefix: Int, protocol: NENetworkRule.Protocol)](nenetworkrule/init(destinationnetwork:prefix:protocol:).md)
  Creates a rule that matches network traffic destined for a host within a specific network.
- [init(destinationHost: NWHostEndpoint, protocol: NENetworkRule.Protocol)](nenetworkrule/init(destinationhost:protocol:).md)
  Creates a rule that matches network traffic destined for a host within a specific DNS domain.
- [init(remoteNetwork: NWHostEndpoint?, remotePrefix: Int, localNetwork: NWHostEndpoint?, localPrefix: Int, protocol: NENetworkRule.Protocol, direction: NETrafficDirection)](nenetworkrule/init(remotenetwork:remoteprefix:localnetwork:localprefix:protocol:direction:).md)
  Creates a rule that matches traffic by remote network, local network, protocol, and direction.
### Matching network traffic characteristics
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
- [enum NETrafficDirection](netrafficdirection.md)
  A type to represent the direction of network traffic.
### Initializers
- [convenience init(destinationHostEndpoint: NWEndpoint, protocol: NENetworkRule.Protocol)](nenetworkrule/init(destinationhostendpoint:protocol:).md)
- [convenience init(destinationNetworkEndpoint: NWEndpoint, prefix: Int, protocol: NENetworkRule.Protocol)](nenetworkrule/init(destinationnetworkendpoint:prefix:protocol:).md)
- [convenience init(remoteNetworkEndpoint: NWEndpoint?, remotePrefix: Int, localNetworkEndpoint: NWEndpoint?, localPrefix: Int, protocol: NENetworkRule.Protocol, direction: NETrafficDirection)](nenetworkrule/init(remotenetworkendpoint:remoteprefix:localnetworkendpoint:localprefix:protocol:direction:).md)
### Instance Properties
- [var matchLocalNetworkEndpoint: NWEndpoint?](nenetworkrule/matchlocalnetworkendpoint-62ttv.md)
- [var matchRemoteHostOrNetworkEndpoint: NWEndpoint?](nenetworkrule/matchremotehostornetworkendpoint-4a5ht.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NETransparentProxyManager](netransparentproxymanager.md)
  An object that configures and controls transparent proxies.
- [class NETransparentProxyProvider](netransparentproxyprovider.md)
  An object that implements the client side of a custom transparent network proxy solution.
- [class NETransparentProxyNetworkSettings](netransparentproxynetworksettings.md)
  A specification of what traffic to route through a transparent proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nenetworkrule)*