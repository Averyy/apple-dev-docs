# QUIC.TLS

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

The set of TLS options available when using QUIC.

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
struct TLS
```

#### Overview

Used to configure the TLS handshake that runs within the QUIC handshake.

## Topics

### Instance Methods
- [func certificateValidator((sec_protocol_metadata_t, sec_trust_t) async -> Bool) -> QUIC](./tls-swift.struct/certificatevalidator%28_%29.md)
  Set a block to provide custom verification of the peer’s credentials during the TLS handshake.
- [func cipherSuites([tls_ciphersuite_t]) -> QUIC](./tls-swift.struct/ciphersuites%28_%29.md)
  Set TLS cipher suites to the set of enabled ciphersuites.
- [func ciphersuiteGroups([tls_ciphersuite_group_t]) -> QUIC](./tls-swift.struct/ciphersuitegroups%28_%29.md)
  Set TLS cipher suite groups to the set of enabled ciphersuites.
- [func localIdentity(sec_identity_t) -> QUIC](./tls-swift.struct/localidentity%28_%29.md)
  Set the local identity TLS uses during the QUIC handshake.
- [func peerAuthentication(TLS.PeerAuthentication) -> QUIC](./tls-swift.struct/peerauthentication%28_%29.md)
  Specify a preference for how to authenticate the peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/quic/tls-swift.struct)*