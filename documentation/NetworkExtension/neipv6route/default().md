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
class func `default`() -> NEIPv6Route
```

```objc
+ (NEIPv6Route * const) defaultRoute;
```

## Return Value

A `NEIPv6Route` object containing the default IPv6 route.

## Discussion

Set this route in the `includedRoutes` array in `NEIPv6Settings` to specify that all IPv6 network traffic be routed to the TUN interface by default.

## See Also

### Creating an IPv6 Route
- [init(destinationAddress: String, networkPrefixLength: NSNumber)](./init%28destinationaddress,networkprefixlength%29.md)
  Initialize the NEIPv6Route


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv6route/default())*