# localIdentity(_:)

**Framework**: Network  
**Kind**: method

Set the local identity TLS uses during the QUIC handshake.

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
func localIdentity(_ identity: sec_identity_t) -> QUIC
```

## Parameters

- `identity`: The local identity to be used during the QUIC handshake.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/quic/tls-swift.struct/localidentity(_:))*