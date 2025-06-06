# NWError

**Framework**: Network  
**Kind**: enum

The errors returned by objects in the Network framework.

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
enum NWError
```

## Topics

### Checking Error Types
- [case posix(POSIXErrorCode)](nwerror/posix(_:).md)
  A POSIX error, which is used for most network protocol and routing errors.
- [case dns(DNSServiceErrorType)](nwerror/dns(_:).md)
  A DNS error encountered in resolving, browsing, or advertising.
- [case tls(OSStatus)](nwerror/tls(_:).md)
  A TLS error reported by a TLS connection or listener.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwerror)*