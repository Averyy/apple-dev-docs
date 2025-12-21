# localIdentity(_:)

**Framework**: Network  
**Kind**: method

Set the local identity TLS uses during the handshake.

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
func localIdentity(_ identity: sec_identity_t) -> TLS
```

## Parameters

- `identity`: The local identity to be used during the TLS handshake.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tls/localidentity(_:))*