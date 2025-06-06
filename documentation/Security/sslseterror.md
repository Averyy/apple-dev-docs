# SSLSetError(_:_:)

**Framework**: Security  
**Kind**: func

Sets the status of a session context.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+

## Declaration

```swift
func SSLSetError(_ context: SSLContext, _ status: OSStatus) -> OSStatus
```

#### Return Value

A result code that represents the outcome of this function call, not to be confused with the `status` parameter. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

Call this function after handling the steps of an SSL handshake, such as server certificate validation.

## Parameters

- `context`: A session context.
- `status`: A status result for the context, not to be confused with the return result of this function call. See  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslseterror(_:_:))*