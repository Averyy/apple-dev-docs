# destinationNetworkPrefixLength

**Framework**: Network Extension  
**Kind**: property

The destination network prefix length of the route.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var destinationNetworkPrefixLength: NSNumber { get }
```

#### Discussion

This string is combined with `destinationAddress` to specify the destination network of the route.

## See Also

- [var destinationAddress: String](neipv6route/destinationaddress.md)
  The destination network address of the route.
- [var gatewayAddress: String?](neipv6route/gatewayaddress.md)
  The address of the next-hop gateway of the route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv6route/destinationnetworkprefixlength)*