# NETransparentProxyManager

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

An object that configures and controls transparent proxies.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NETransparentProxyManager
```

```objc
@interface NETransparentProxyManager : NEVPNManager
```

## Topics

### Loading proxy configurations
- [class func loadAllFromPreferences(completionHandler: ([NETransparentProxyManager]?, (any Error)?) -> Void)](./netransparentproxymanager/loadallfrompreferences%28completionhandler%29.md)
  Loads all previously-saved transparent proxy configurations.

## Relationships

### Inherits From
- [NEVPNManager](./nevpnmanager.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Transparent proxy configuration
- [class NETransparentProxyProvider](./netransparentproxyprovider.md)
  An object that implements the client side of a custom transparent network proxy solution.
- [class NETransparentProxyNetworkSettings](./netransparentproxynetworksettings.md)
  A specification of what traffic to route through a transparent proxy.
- [class NENetworkRule](./nenetworkrule.md)
  A rule to match attributes of network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netransparentproxymanager)*