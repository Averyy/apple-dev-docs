# SSLReHandshake(_:)

**Framework**: Security  
**Kind**: func

Requests renegotiation of the SSL handshake. Server only.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+

## Declaration

```swift
func SSLReHandshake(_ context: SSLContext) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

On success, call the [`SSLHandshake(_:)`](sslhandshake(_:).md) function or the [`SSLRead(_:_:_:_:)`](sslread(_:_:_:_:).md) function, or both, as appropriate, as you would for the original handshake.

## Parameters

- `context`: An SSL session context reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslrehandshake(_:))*