# SSLGetConnection(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves an I/O connection—such as a socket or endpoint—for a specific session.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLGetConnection(_ context: SSLContext, _ connection: UnsafeMutablePointer<SSLConnectionRef?>) -> OSStatus
```

```c
OSStatus SSLGetConnection(SSLContextRef context, SSLConnectionRef*connection);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

You can use this function on either the client or server to retrieve the connection associated with a secure session.

## Parameters

- `context`: An SSL session context reference.
- `connection`: On return, a pointer to a session connection reference. If no connection has been set using the [`SSLSetConnection(_:_:)`](./sslsetconnection%28_,_%29.md) function, then this parameter is `NULL` on return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetconnection(_:_:))*