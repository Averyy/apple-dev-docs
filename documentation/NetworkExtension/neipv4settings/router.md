# router

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The address of the next-hop gateway router represented as a dotted decimal string.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var router: String? { get set }
```

```objc
@property (copy, nullable) NSString * router;
```

#### Discussion

The system ignores this property for TUN interfaces.

## See Also

### Accessing IPv4 properties
- [var addresses: [String]](./addresses.md)
  The IPv4 addresses to assign to the TUN interface.
- [var subnetMasks: [String]](./subnetmasks.md)
  The IPv4 network masks to assign to the TUN interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv4settings/router)*