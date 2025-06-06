# SSLGetConnection(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves an I/O connection—such as a socket or endpoint—for a specific session.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func SSLGetConnection(_ context: SSLContext, _ connection: UnsafeMutablePointer<SSLConnectionRef?>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

You can use this function on either the client or server to retrieve the connection associated with a secure session.

## Parameters

- `context`: An SSL session context reference.
- `connection`: On return, a pointer to a session connection reference. If no connection has been set using the   function, then this parameter is   on return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetconnection(_:_:))*