# SSLClientCertificateState.certSent

**Framework**: Security  
**Kind**: case

Indicates that the server asked for a certificate, the client sent one, and the server validated it. The application can inspect the certificate using the function `SSLGetPeerCertificates`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
case certSent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslclientcertificatestate/certsent)*