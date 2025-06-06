# asIPv4

**Framework**: Network  
**Kind**: property

Extracts the IPv4 address contained within the IPv6 address, if the IPv6 address is an IPv4-mapped or IPv4-compatible address.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var asIPv4: IPv4Address? { get }
```

## See Also

- [init?(String)](ipv6address/init(_:).md)
  Initializes an IPv6 address with a string.
- [init?(Data, NWInterface?)](ipv6address/init(_:_:).md)
  Initializes an IPv6 address with data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ipv6address/asipv4)*