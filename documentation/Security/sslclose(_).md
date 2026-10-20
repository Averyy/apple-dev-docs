# SSLClose(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Terminates the current SSL session.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLClose(_ context: SSLContext) -> OSStatus
```

```c
OSStatus SSLClose(SSLContextRef context);
```

## Mentions

- [Using the Secure Socket Layer for Network Communication](./using-the-secure-socket-layer-for-network-communication.md)

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Parameters

- `context`: The SSL session context reference of the session you want to terminate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslclose(_:))*