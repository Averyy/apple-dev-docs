# SSLSetProtocolVersionMax(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the maximum protocol version allowed by the application for a given SSL context.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLSetProtocolVersionMax(_ context: SSLContext, _ maxVersion: SSLProtocol) -> OSStatus
```

```c
OSStatus SSLSetProtocolVersionMax(SSLContextRef context, SSLProtocol maxVersion);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Parameters

- `context`: The SSL context associated with the connection.
- `maxVersion`: The new maximum version ([`SSLProtocol.tlsProtocol1`](./sslprotocol/tlsprotocol1.md), for example). See [`SSLProtocol`](./sslprotocol.md) for a complete list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetprotocolversionmax(_:_:))*