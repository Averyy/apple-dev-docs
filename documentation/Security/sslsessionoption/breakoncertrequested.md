# SSLSessionOption.breakOnCertRequested

**Framework**: Security  
**Kind**: case

Enables returning from [`SSLHandshake(_:)`](sslhandshake(_:).md) (with a result of `errSSLClientCertRequested`) when the server requests a client certificate.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
case breakOnCertRequested
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsessionoption/breakoncertrequested)*