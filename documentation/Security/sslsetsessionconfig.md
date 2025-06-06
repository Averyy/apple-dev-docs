# SSLSetSessionConfig(_:_:)

**Framework**: Security  
**Kind**: func

Sets a predefined configuration for the Secure Sockets Layer (SSL) session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+

## Declaration

```swift
func SSLSetSessionConfig(_ context: SSLContext, _ config: CFString) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

## Parameters

- `context`: An SSL session context reference.
- `config`: The predefined configuration you want to apply to the SSL session. You can configure enabled protocol versions, enabled cipher suites, and the   session option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetsessionconfig(_:_:))*