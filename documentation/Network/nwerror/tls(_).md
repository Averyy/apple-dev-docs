# NWError.tls(_:)

**Framework**: Network  
**Kind**: case  
**Role**: Case

A TLS error reported by a TLS connection or listener.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
case tls(OSStatus)
```

## See Also

### Checking Error Types
- [case posix(POSIXErrorCode)](./posix%28_%29.md)
  A POSIX error, which is used for most network protocol and routing errors.
- [case dns(DNSServiceErrorType)](./dns%28_%29.md)
  A DNS error encountered in resolving, browsing, or advertising.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwerror/tls(_:))*