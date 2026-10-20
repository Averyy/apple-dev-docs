# init(_:_:)

**Framework**: Network  
**Kind**: init

Initializes an IPv6 address with data.

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
init?(_ rawValue: Data, _ interface: NWInterface? = nil)
```

#### Discussion

The provided data is expected to be an IPv6 address of 16 bytes.

## See Also

- [init?(String)](ipv6address/init(_:).md)
  Initializes an IPv6 address with a string.
- [var asIPv4: IPv4Address?](ipv6address/asipv4.md)
  Extracts the IPv4 address contained within the IPv6 address, if the IPv6 address is an IPv4-mapped or IPv4-compatible address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ipv6address/init(_:_:))*