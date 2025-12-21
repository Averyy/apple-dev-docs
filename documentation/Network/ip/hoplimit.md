# hopLimit(_:)

**Framework**: Network  
**Kind**: method

Configure the IP hop limit.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func hopLimit(_ limit: UInt8) -> IP
```

#### Discussion

Equivalent to `IP_TTL` for IPv4 and `IPV6_HOPLIMIT` for IPv6.

## Parameters

- `limit`: The hop limit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ip/hoplimit(_:))*