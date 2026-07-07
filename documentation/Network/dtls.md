# DTLS

**Framework**: Network  
**Kind**: struct

The system definition of the Datagram Transport Layer Security (DTLS) protocol.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct DTLS
```

#### Overview

Supports sending and receiving encrypted byte datagrams.

## Topics

### Initializers
- [init()](dtls/init.md)
  Create a DTLS protocol to use in a protocol stack.
- [init(() -> UDP)](dtls/init(_:).md)
  Create a DTLS protocol to use in a protocol stack.
### Instance Methods
- [func applicationProtocols([String]) -> DTLS](dtls/applicationprotocols(_:).md)
  Set application protocols supported by clients of this protocol.
- [func certificateValidator((sec_protocol_metadata_t, sec_trust_t) async -> Bool) -> DTLS](dtls/certificatevalidator(_:).md)
  Set a closure to provide custom verification of the peer’s credentials during the DTLS handshake.
- [func cipherSuiteGroups([tls_ciphersuite_group_t]) -> DTLS](dtls/ciphersuitegroups(_:).md)
  Set DTLS ciphersuite groups to the set of enabled ciphersuites.
- [func cipherSuites([tls_ciphersuite_t]) -> DTLS](dtls/ciphersuites(_:).md)
  Set DTLS ciphersuites to the set of enabled ciphersuites.
- [func earlyDataEnabled(Bool) -> DTLS](dtls/earlydataenabled(_:).md)
  Enable early data (0-RTT) for DTLS.
- [func localIdentity(sec_identity_t) -> DTLS](dtls/localidentity(_:).md)
  Set the local identity DTLS uses during the handshake.
- [func peerAuthentication(DTLS.PeerAuthentication) -> DTLS](dtls/peerauthentication(_:).md)
  Specify a preference for how to authenticate the peer.
- [func ticketsEnabled(Bool) -> DTLS](dtls/ticketsenabled(_:).md)
  Enable DTLS session ticket support.
- [func version(min: tls_protocol_version_t?, max: tls_protocol_version_t?) -> DTLS](dtls/version(min:max:).md)
### Enumerations
- [DTLS.PeerAuthentication](dtls/peerauthentication.md)
  PeerAuthentication specifies how to authenticate the peer end of the connection.

## Relationships

### Conforms To
- [DatagramProtocol](datagramprotocol.md)
- [MessageProtocol](messageprotocol.md)
- [NetworkProtocolOptions](networkprotocoloptions.md)
- [OneToOneProtocol](onetooneprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/dtls)*