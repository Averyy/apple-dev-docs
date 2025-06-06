# init(_:_:)

**Framework**: Network  
**Kind**: init

Initializes an IPv4 address with data.

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

The provided data is expected to be an IPv4 address of 4 bytes.

## See Also

- [init?(String)](ipv4address/init(_:).md)
  Initializes an IPv4 address with a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ipv4address/init(_:_:))*