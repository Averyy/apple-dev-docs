# QUIC.TLS

**Framework**: Network  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct TLS
```

## Topics

### Instance Methods
- [func cipherSuites([tls_ciphersuite_t]) -> QUIC](quic/tls-swift.struct/ciphersuites(_:).md)
- [func localIdentity(sec_identity_t) -> QUIC](quic/tls-swift.struct/localidentity(_:).md)
- [func peerAuthenticationOptional(Bool) -> QUIC](quic/tls-swift.struct/peerauthenticationoptional(_:).md)
- [func peerAuthenticationRequired(Bool) -> QUIC](quic/tls-swift.struct/peerauthenticationrequired(_:).md)
- [func verifyBlock((sec_protocol_metadata_t, sec_trust_t) async -> Bool) -> QUIC](quic/tls-swift.struct/verifyblock(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/quic/tls-swift.struct)*