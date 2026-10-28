# SSLGetProtocolVersionMin(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Gets the minimum protocol version allowed by the application for a given SSL context.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLGetProtocolVersionMin(_ context: SSLContext, _ minVersion: UnsafeMutablePointer<SSLProtocol>) -> OSStatus
```

```c
OSStatus SSLGetProtocolVersionMin(SSLContextRef context, SSLProtocol *minVersion);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Parameters

- `context`: The SSL context associated with the connection.
- `minVersion`: The address of an [`SSLProtocol`](./sslprotocol.md) integer where the minimum version should be stored. See [`SSLProtocol`](./sslprotocol.md) for a list of possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetprotocolversionmin(_:_:))*