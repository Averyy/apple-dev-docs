# destinationAddress

**Framework**: Network Extension  
**Kind**: property

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

#### Discussion

This string is combined with `destinationSubnetMask` to specify the destination network of the route.

## See Also

- [var destinationSubnetMask: String](neipv4route/destinationsubnetmask.md)
  The destination network mask of the route.
- [var gatewayAddress: String?](neipv4route/gatewayaddress.md)
  The address of the next-hop gateway of the route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv4route/destinationaddress)*