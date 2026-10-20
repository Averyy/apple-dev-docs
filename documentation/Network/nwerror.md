# NWError

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

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
- [case posix(POSIXErrorCode)](./nwerror/posix%28_%29.md)
  A POSIX error, which is used for most network protocol and routing errors.
- [case dns(DNSServiceErrorType)](./nwerror/dns%28_%29.md)
  A DNS error encountered in resolving, browsing, or advertising.
- [case tls(OSStatus)](./nwerror/tls%28_%29.md)
  A TLS error reported by a TLS connection or listener.
### Enumeration Cases
- [NWError.wifiAware(_:)](./nwerror/wifiaware%28_%29.md)
  The error code will be a Wi-Fi Aware error as defined in <WifiAware/errors.swift>
### Instance Properties
- [var wifiAware: WAError?](./nwerror/wifiaware.md)
  The underlying error that occurred, if applicable.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomNSError](../Foundation/customnserror.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwerror)*