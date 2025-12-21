# noChecksumPreferred(_:)

**Framework**: Network  
**Kind**: method

Skip computing checksums when sending UDP packets.

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
func noChecksumPreferred(_ noChecksum: Bool) -> UDP
```

#### Discussion

This will only take effect when running over IPv4 (`UDP_NOCKSUM`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/udp/nochecksumpreferred(_:))*