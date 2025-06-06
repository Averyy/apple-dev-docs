# subnetMasks

**Framework**: Network Extension  
**Kind**: property

The IPv4 network masks to assign to the TUN interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var subnetMasks: [String] { get }
```

#### Discussion

Each mask in this array is combined with the IP address in the corresponding index in `addresses` to specify an IPv4 network that the TUN interface is (virtually) connected to.

## See Also

- [var addresses: [String]](neipv4settings/addresses.md)
  The IPv4 addresses to assign to the TUN interface.
- [var router: String?](neipv4settings/router.md)
  The address of the next-hop gateway router represented as a dotted decimal string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv4settings/subnetmasks)*