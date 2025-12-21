# minimumMTU(_:)

**Framework**: Network  
**Kind**: method

Configure IP to use the minimum MTU value.

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
func minimumMTU(_ useMinimumMTU: Bool) -> IP
```

#### Discussion

The minimum MTU value is 1280 bytes for IPv6 (`IPV6_USE_MIN_MTU`). This value has no effect for IPv4.

## Parameters

- `useMinimumMTU`: True to use the minimum MTU value, false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ip/minimummtu(_:))*