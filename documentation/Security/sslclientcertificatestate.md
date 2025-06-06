# SSLClientCertificateState

**Framework**: Security  
**Kind**: enum

An enumeration of the states of client certificate exchange.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SSLClientCertificateState
```

## Topics

### Constants
- [SSLClientCertificateState.certNone](sslclientcertificatestate/certnone.md)
  Indicates that the server hasn’t asked for a certificate and that the client hasn’t sent one.
- [SSLClientCertificateState.certRequested](sslclientcertificatestate/certrequested.md)
  Indicates that the server has asked for a certificate, but the client has not sent it.
- [SSLClientCertificateState.certSent](sslclientcertificatestate/certsent.md)
  Indicates that the server asked for a certificate, the client sent one, and the server validated it. The application can inspect the certificate using the function `SSLGetPeerCertificates`.
- [SSLClientCertificateState.certRejected](sslclientcertificatestate/certrejected.md)
  Indicates that the client sent a certificate but the certificate failed validation. This value is seen only on the server side. The server application can inspect the certificate using the function `SSLGetPeerCertificates`.
### Initializers
- [init?(rawValue: Int32)](sslclientcertificatestate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslclientcertificatestate)*