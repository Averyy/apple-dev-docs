# NEIPv4Route

**Framework**: Network Extension  
**Kind**: class

The settings for an IPv4 route.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEIPv4Route
```

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

## Topics

### Creating an IPv4 Route
- [init(destinationAddress: String, subnetMask: String)](neipv4route/init(destinationaddress:subnetmask:).md)
  Initialize the [`NEIPv4Route`](neipv4route.md) object.
- [class func `default`() -> NEIPv4Route](neipv4route/default.md)
  A convenience method for creating the default IPv4 route.
### Accessing IPv4 Route Properties
- [var destinationAddress: String](neipv4route/destinationaddress.md)
  The destination network address of the route.
- [var destinationSubnetMask: String](neipv4route/destinationsubnetmask.md)
  The destination network mask of the route.
- [var gatewayAddress: String?](neipv4route/gatewayaddress.md)
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

- [var includedRoutes: [NEIPv4Route]?](neipv4settings/includedroutes.md)
  The IPv4 network traffic that the system routes to the TUN interface.
- [var excludedRoutes: [NEIPv4Route]?](neipv4settings/excludedroutes.md)
  The IPv4 network traffic that the system routes to the primary physical interface, not the TUN interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv4route)*