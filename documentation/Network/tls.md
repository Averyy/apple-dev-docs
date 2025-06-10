# TLS

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

### Initializers
- [init()](tls/init.md)
- [init(() -> TCP)](tls/init(_:).md)
### Instance Properties
- [let belowProtocol: TCP](tls/belowprotocol.md)
- [var nw: nw_protocol_options_t](tls/nw.md)
### Instance Methods
- [func applicationProtocols([String]) -> TLS](tls/applicationprotocols(_:).md)
- [func cipherSuiteGroups([tls_ciphersuite_group_t]) -> TLS](tls/ciphersuitegroups(_:).md)
- [func cipherSuites([tls_ciphersuite_t]) -> TLS](tls/ciphersuites(_:).md)
- [func earlyDataEnabled(Bool) -> TLS](tls/earlydataenabled(_:).md)
- [func localIdentity(sec_identity_t) -> TLS](tls/localidentity(_:).md)
- [func maxVersion(tls_protocol_version_t) -> TLS](tls/maxversion(_:).md)
- [func minVersion(tls_protocol_version_t) -> TLS](tls/minversion(_:).md)
- [func peerAuthentication(TLS.PeerAuthentication) -> TLS](tls/peerauthentication(_:).md)
- [func ticketsEnabled(Bool) -> TLS](tls/ticketsenabled(_:).md)
- [func verifyBlock((sec_protocol_metadata_t, sec_trust_t) async -> Bool) -> TLS](tls/verifyblock(_:).md)
### Enumerations
- [enum PeerAuthentication](tls/peerauthentication.md)

## Relationships

### Conforms To
- [NetworkProtocolOptions](networkprotocoloptions.md)
- [OneToOneProtocol](onetooneprotocol.md)
- [StreamProtocol](streamprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tls)*