# SSLSetError(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the status of a session context.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.13+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLSetError(_ context: SSLContext, _ status: OSStatus) -> OSStatus
```

```c
OSStatus SSLSetError(SSLContextRef context, OSStatus status);
```

#### Return Value

A result code that represents the outcome of this function call, not to be confused with the `status` parameter. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

Call this function after handling the steps of an SSL handshake, such as server certificate validation.

## Parameters

- `context`: A session context.
- `status`: A status result for the context, not to be confused with the return result of this function call. See [Secure Transport Result Codes](./secure-transport-result-codes.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslseterror(_:_:))*