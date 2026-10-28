# default()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Type Method

A convenience method for creating the default IPv4 route.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class func `default`() -> NEIPv4Route
```

```objc
+ (NEIPv4Route * const) defaultRoute;
```

## Return Value

An [`NEIPv4Route`](../neipv4route.md) object containing the default IPv4 route.

## Discussion

Set this route in the `includedRoutes` array in the [`NEIPv4Settings`](../neipv4settings.md) object to specify that all IPv4 network traffic be routed to the TUN interface by default.

## See Also

### Creating an IPv4 Route
- [init(destinationAddress: String, subnetMask: String)](./init%28destinationaddress,subnetmask%29.md)
  Initialize the [`NEIPv4Route`](../neipv4route.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv4route/default())*