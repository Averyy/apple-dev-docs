# SSLClientCertificateState.certRejected

**Framework**: Security  
**Kind**: case  
**Role**: Case

Indicates that the client sent a certificate but the certificate failed validation. This value is seen only on the server side. The server application can inspect the certificate using the function `SSLGetPeerCertificates`.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

## Declaration

```swift
case certRejected
```

```c
kSSLClientCertRejected
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslclientcertificatestate/certrejected)*