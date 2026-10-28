# SSLSessionOption.sendOneByteRecord

**Framework**: Security  
**Kind**: case  
**Role**: Case

Enables `1/n-1` record splitting for BEAST attack mitigation.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

## Declaration

```swift
case sendOneByteRecord
```

```c
kSSLSessionOptionSendOneByteRecord
```

## Discussion

When enabled, record splitting is performed only for TLS 1.0 connections based on a block cipher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsessionoption/sendonebyterecord)*