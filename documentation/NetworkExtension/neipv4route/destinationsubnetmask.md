# destinationSubnetMask

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The destination network mask of the route.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var destinationSubnetMask: String { get }
```

```objc
@property (readonly) NSString * destinationSubnetMask;
```

#### Discussion

This string is combined with `destinationAddress` to specify the destination network of the route.

## See Also

### Accessing IPv4 Route Properties
- [var destinationAddress: String](./destinationaddress.md)
  The destination network address of the route.
- [var gatewayAddress: String?](./gatewayaddress.md)
  The address of the next-hop gateway of the route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv4route/destinationsubnetmask)*