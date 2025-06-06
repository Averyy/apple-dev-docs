# NETransparentProxyManager

**Framework**: Network Extension  
**Kind**: class

An object that configures and controls transparent proxies.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NETransparentProxyManager
```

## Topics

### Loading proxy configurations
- [class func loadAllFromPreferences(completionHandler: ([NETransparentProxyManager]?, (any Error)?) -> Void)](netransparentproxymanager/loadallfrompreferences(completionhandler:).md)
  Loads all previously-saved transparent proxy configurations.

## Relationships

### Inherits From
- [NEVPNManager](nevpnmanager.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NETransparentProxyProvider](netransparentproxyprovider.md)
  An object that implements the client side of a custom transparent network proxy solution.
- [class NETransparentProxyNetworkSettings](netransparentproxynetworksettings.md)
  A specification of what traffic to route through a transparent proxy.
- [class NENetworkRule](nenetworkrule.md)
  A rule to match attributes of network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netransparentproxymanager)*