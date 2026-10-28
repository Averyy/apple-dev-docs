# destinationAddress

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The destination network address of the route.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var destinationAddress: String { get }
```

```objc
@property (readonly) NSString * destinationAddress;
```

## Discussion

This string is combined with `destinationNetworkPrefixLength` to specify the destination network of the route.

## See Also

### Accessing IPv6 Route Properties
- [var destinationNetworkPrefixLength: NSNumber](./destinationnetworkprefixlength.md)
  The destination network prefix length of the route.
- [var gatewayAddress: String?](./gatewayaddress.md)
  The address of the next-hop gateway of the route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv6route/destinationaddress)*