# SSLSessionOption.breakOnServerAuth

**Framework**: Security  
**Kind**: case  
**Role**: Case

Enables returning from [`SSLHandshake(_:)`](../sslhandshake%28_%29.md) (with a result of `errSSLServerAuthCompleted`) when the server authentication portion of the handshake is complete to allow your application to perform its own certificate verification.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

## Declaration

```swift
case breakOnServerAuth
```

```c
kSSLSessionOptionBreakOnServerAuth
```

#### Discussion

Note that in iOS (all versions) and macOS 10.8 and later, setting this option disables Secure Transport’s automatic verification of server certificates.

If you set this option, your application should perform its own certificate verification when `errSSLServerAuthCompleted` is returned before continuing with the handshake.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsessionoption/breakonserverauth)*