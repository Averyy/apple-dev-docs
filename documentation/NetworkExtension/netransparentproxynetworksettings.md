# NETransparentProxyNetworkSettings

**Framework**: Network Extension  
**Kind**: class

A specification of what traffic to route through a transparent proxy.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NETransparentProxyNetworkSettings
```

#### Overview

A proxy network settings object contains two properties: an array of rules to include traffic ([`includedNetworkRules`](netransparentproxynetworksettings/includednetworkrules.md)) and an array of rules to exclude traffic ([`excludedNetworkRules`](netransparentproxynetworksettings/excludednetworkrules.md)). The exclusion rules take prirority. Therefore, if a given flow matches any of the [`excludedNetworkRules`](netransparentproxynetworksettings/excludednetworkrules.md), evaluation ends and the flow doesn’t route to the proxy. If there’s no match, then evaluation continues and attempts to match the flow against the [`includedNetworkRules`](netransparentproxynetworksettings/includednetworkrules.md).

## Topics

### Traffic routing rules
- [var includedNetworkRules: [NENetworkRule]?](netransparentproxynetworksettings/includednetworkrules.md)
  An array of rules that collectively specify what traffic to route through the transparent proxy.
- [var excludedNetworkRules: [NENetworkRule]?](netransparentproxynetworksettings/excludednetworkrules.md)
  An array of rules that collectively specify what traffic to not route through the transparent proxy.

## Relationships

### Inherits From
- [NETunnelNetworkSettings](netunnelnetworksettings.md)
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
- [class NENetworkRule](nenetworkrule.md)
  A rule to match attributes of network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netransparentproxynetworksettings)*