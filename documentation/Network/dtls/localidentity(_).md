# localIdentity(_:)

**Framework**: Network  
**Kind**: method

Set the local identity DTLS uses during the handshake.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func localIdentity(_ identity: sec_identity_t) -> DTLS
```

## Parameters

- `identity`: The local identity to be used during the DTLS handshake.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/dtls/localidentity(_:))*