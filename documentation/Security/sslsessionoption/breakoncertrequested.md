# SSLSessionOption.breakOnCertRequested

**Framework**: Security  
**Kind**: case  
**Role**: Case

Enables returning from [`SSLHandshake(_:)`](../sslhandshake%28_%29.md) (with a result of `errSSLClientCertRequested`) when the server requests a client certificate.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

## Declaration

```swift
case breakOnCertRequested
```

```c
kSSLSessionOptionBreakOnCertRequested
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsessionoption/breakoncertrequested)*