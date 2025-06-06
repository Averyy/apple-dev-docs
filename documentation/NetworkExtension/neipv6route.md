# NEIPv6Route

**Framework**: Network Extension  
**Kind**: class

The settings for an IPv6 route.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEIPv6Route
```

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

## Topics

### Creating an IPv6 Route
- [init(destinationAddress: String, networkPrefixLength: NSNumber)](neipv6route/init(destinationaddress:networkprefixlength:).md)
  Initialize the NEIPv6Route
- [class func `default`() -> NEIPv6Route](neipv6route/default.md)
  A convenience method for creating the default IPv4 route.
### Accessing IPv6 Route Properties
- [var destinationAddress: String](neipv6route/destinationaddress.md)
  The destination network address of the route.
- [var destinationNetworkPrefixLength: NSNumber](neipv6route/destinationnetworkprefixlength.md)
  The destination network prefix length of the route.
- [var gatewayAddress: String?](neipv6route/gatewayaddress.md)
  The address of the next-hop gateway of the route.

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

- [var includedRoutes: [NEIPv6Route]?](neipv6settings/includedroutes.md)
  The IPv6 network traffic that the system routes to the TUN interface.
- [var excludedRoutes: [NEIPv6Route]?](neipv6settings/excludedroutes.md)
  The IPv6 network traffic that the system routes to the primary physical interface, not the TUN interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv6route)*