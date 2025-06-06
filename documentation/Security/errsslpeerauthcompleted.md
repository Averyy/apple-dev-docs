# errSSLPeerAuthCompleted

**Framework**: Security  
**Kind**: var

A non-fatal result indicating the peer certificate is valid, or was ignored if verification is disabled.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var errSSLPeerAuthCompleted: OSStatus { get }
```

#### Discussion

The peer’s certificate chain is valid, or was ignored if certificate verification was disabled via [`SSLSetEnableCertVerify`](sslsetenablecertverify.md). In response, you may decide to continue with the handshake (by calling [`SSLHandshake(_:)`](sslhandshake(_:).md) again) or just close the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/errsslpeerauthcompleted)*