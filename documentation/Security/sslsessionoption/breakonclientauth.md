# SSLSessionOption.breakOnClientAuth

**Framework**: Security  
**Kind**: case

Enables returning from [`SSLHandshake(_:)`](sslhandshake(_:).md) (with a result of `errSSLClientAuthCompleted`) when the client authentication portion of the handshake is complete to allow your application to perform its own certificate verification.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
case breakOnClientAuth
```

#### Discussion

Note that in iOS (all versions) and macOS 10.8 and later, setting this option disables Secure Transport’s automatic verification of client certificates.

If you set this option, your application should perform its own certificate verification when `errSSLClientAuthCompleted` is returned before continuing with the handshake.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsessionoption/breakonclientauth)*