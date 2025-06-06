# gatewayAddress

**Framework**: Network Extension  
**Kind**: property

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

#### Discussion

The default value of this property is nil. When this property is nil, the route’s next-hop gateway will be set to the TUN interface unless it is a Split Exclude route.

## See Also

- [var destinationAddress: String](neipv4route/destinationaddress.md)
  The destination network address of the route.
- [var destinationSubnetMask: String](neipv4route/destinationsubnetmask.md)
  The destination network mask of the route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv4route/gatewayaddress)*