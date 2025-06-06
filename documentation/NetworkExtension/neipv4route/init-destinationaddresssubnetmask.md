# init(destinationAddress:subnetMask:)

**Framework**: Network Extension  
**Kind**: init

Initialize the [`NEIPv4Route`](neipv4route.md) object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(destinationAddress address: String, subnetMask: String)
```

## Parameters

- `address`: An IPv4 address string. This string is combined with   to specify the destination network of the route.
- `subnetMask`: An IPv4 network mask string. This string is combined with   to specify the destination network of the route.

## See Also

- [class func `default`() -> NEIPv4Route](neipv4route/default.md)
  A convenience method for creating the default IPv4 route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv4route/init(destinationaddress:subnetmask:))*