# init(_:_:)

**Framework**: Network  
**Kind**: init  
**Required**: Yes

Initializes an IP address with data.

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
init?(_ rawValue: Data, _ interface: NWInterface?)
```

#### Discussion

The provided data is expected to be either an IPv4 address of 4 bytes or an IPv6 address of 16 bytes.

## See Also

- [init?(String)](ipaddress/init(_:).md)
  Initializes an IP address with a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ipaddress/init(_:_:))*