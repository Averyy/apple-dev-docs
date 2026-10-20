# init(_:)

**Framework**: Network  
**Kind**: init  
**Role**: Initializer  
**Required**: Yes

Initializes an IP address with a string.

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
init?(_ string: String)
```

#### Discussion

The provided string will be interpreted as an IPv4 or IPv6 address. If the string cannot be interpreted as an address, the initialization will fail.

## See Also

### Creating Addresses
- [init?(Data, NWInterface?)](./init%28_,_%29.md)
  Initializes an IP address with data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ipaddress/init(_:))*