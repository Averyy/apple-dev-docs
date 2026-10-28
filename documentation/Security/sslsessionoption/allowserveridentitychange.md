# SSLSessionOption.allowServerIdentityChange

**Framework**: Security  
**Kind**: case  
**Role**: Case

Allow server identity change on renegotiation.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

## Declaration

```swift
case allowServerIdentityChange
```

```c
kSSLSessionOptionAllowServerIdentityChange
```

## Discussion

Disallow by default to avoid the Triple Handshake attack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsessionoption/allowserveridentitychange)*