# fragmentationDisabled(_:)

**Framework**: Network  
**Kind**: method

Configure IP to disable fragmentation on outgoing packets.

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
func fragmentationDisabled(_ dontFragment: Bool) -> IP
```

#### Discussion

Equivalent to `IP_DONTFRAG` for IPv4 and `IPV6_DONTFRAG` for IPv6.

## Parameters

- `dontFragment`: True to disable fragmentation, false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ip/fragmentationdisabled(_:))*