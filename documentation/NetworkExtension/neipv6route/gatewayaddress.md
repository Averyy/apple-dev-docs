# gatewayAddress

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The address of the next-hop gateway of the route.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var gatewayAddress: String? { get set }
```

```objc
@property (copy, nullable) NSString * gatewayAddress;
```

#### Discussion

The default value of this property is nil. When this property is nil, the route’s next-hop gateway will be set to the TUN interface.

## See Also

### Accessing IPv6 Route Properties
- [var destinationAddress: String](./destinationaddress.md)
  The destination network address of the route.
- [var destinationNetworkPrefixLength: NSNumber](./destinationnetworkprefixlength.md)
  The destination network prefix length of the route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv6route/gatewayaddress)*