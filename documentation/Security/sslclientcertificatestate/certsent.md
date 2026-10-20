# SSLClientCertificateState.certSent

**Framework**: Security  
**Kind**: case  
**Role**: Case

Indicates that the server asked for a certificate, the client sent one, and the server validated it. The application can inspect the certificate using the function `SSLGetPeerCertificates`.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

## Declaration

```swift
case certSent
```

```c
kSSLClientCertSent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslclientcertificatestate/certsent)*