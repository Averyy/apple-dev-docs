# TLS

**Framework**: Network  
**Kind**: struct

The system definition of the Transport Layer Security (TLS) protocol.

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

Supports sending and receiving encrypted byte streams.

## Topics

### Initializers
- [init()](tls/init.md)
  Create a TLS protocol to use in a protocol stack.
- [init(() -> TCP)](tls/init(_:).md)
  Create a TLS protocol to use in a protocol stack.
### Instance Methods
- [func applicationProtocols([String]) -> TLS](tls/applicationprotocols(_:).md)
  Set application protocols supported by clients of this protocol.
- [func certificateValidator((sec_protocol_metadata_t, sec_trust_t) async -> Bool) -> TLS](tls/certificatevalidator(_:).md)
  Set a closure to provide custom verification of the peer’s credentials during the TLS handshake.
- [func cipherSuiteGroups([tls_ciphersuite_group_t]) -> TLS](tls/ciphersuitegroups(_:).md)
  Set TLS ciphersuite groups to the set of enabled ciphersuites.
- [func cipherSuites([tls_ciphersuite_t]) -> TLS](tls/ciphersuites(_:).md)
  Set TLS ciphersuites to the set of enabled ciphersuites.
- [func earlyDataEnabled(Bool) -> TLS](tls/earlydataenabled(_:).md)
  Enable early data (0-RTT) for TLS.
- [func localIdentity(sec_identity_t) -> TLS](tls/localidentity(_:).md)
  Set the local identity TLS uses during the handshake.
- [func peerAuthentication(TLS.PeerAuthentication) -> TLS](tls/peerauthentication(_:).md)
  Specify a preference for how to authenticate the peer.
- [func ticketsEnabled(Bool) -> TLS](tls/ticketsenabled(_:).md)
  Enable TLS session ticket support.
- [func version(min: tls_protocol_version_t?, max: tls_protocol_version_t?) -> TLS](tls/version(min:max:).md)
### Enumerations
- [enum PeerAuthentication](tls/peerauthentication.md)
  PeerAuthentication specifies how to authenticate the peer end of the connection.

## Relationships

### Conforms To
- [NetworkProtocolOptions](networkprotocoloptions.md)
- [OneToOneProtocol](onetooneprotocol.md)
- [StreamProtocol](streamprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tls)*