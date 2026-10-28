# SSLReHandshake(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Requests renegotiation of the SSL handshake. Server only.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLReHandshake(_ context: SSLContext) -> OSStatus
```

```c
OSStatus SSLReHandshake(SSLContextRef context);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

On success, call the [`SSLHandshake(_:)`](./sslhandshake%28_%29.md) function or the [`SSLRead(_:_:_:_:)`](./sslread%28_,_,_,_%29.md) function, or both, as appropriate, as you would for the original handshake.

## Parameters

- `context`: An SSL session context reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslrehandshake(_:))*