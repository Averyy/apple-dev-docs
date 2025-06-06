# NETransparentProxyProvider

**Framework**: Network Extension  
**Kind**: class

An object that implements the client side of a custom transparent network proxy solution.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class NETransparentProxyProvider
```

## Mentions

- [Handling Flow Copying](handling-flow-copying.md)

#### Overview

The [`NETransparentProxyProvider`](netransparentproxyprovider.md) class has the following behavior differences from its superclass [`NEAppProxyProvider`](neappproxyprovider.md):

- Returning `NO` from [`handleNewFlow(_:)`](neappproxyprovider/handlenewflow(_:).md) and [`handleNewUDPFlow(_:initialRemoteEndpoint:)`](neappproxyprovider/handlenewudpflow(_:initialremoteendpoint:).md) causes the flow to proceed to communicate directly with the flow’s ultimate destination, instead of closing the flow with a “Connection Refused” error.
- This provider ignores [`NEDNSSettings`](nednssettings.md) and [`NEProxySettings`](neproxysettings.md) specified within [`NETransparentProxyNetworkSettings`](netransparentproxynetworksettings.md). Flows that match the [`includedNetworkRules`](netransparentproxynetworksettings/includednetworkrules.md) within [`NETransparentProxyNetworkSettings`](netransparentproxynetworksettings.md) use the same DNS and proxy settings that other flows on the system currently use.
- Flows that are created using a “connect by name” API (such as [`Network`](https://developer.apple.com/documentation/Network) framework or [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession)) that match the [`includedNetworkRules`](netransparentproxynetworksettings/includednetworkrules.md) don’t bypass DNS resolution.

## Relationships

### Inherits From
- [NEAppProxyProvider](neappproxyprovider.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NETransparentProxyManager](netransparentproxymanager.md)
  An object that configures and controls transparent proxies.
- [class NETransparentProxyNetworkSettings](netransparentproxynetworksettings.md)
  A specification of what traffic to route through a transparent proxy.
- [class NENetworkRule](nenetworkrule.md)
  A rule to match attributes of network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netransparentproxyprovider)*