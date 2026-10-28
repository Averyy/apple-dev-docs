# SSLGetSessionState(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the state of an SSL session.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLGetSessionState(_ context: SSLContext, _ state: UnsafeMutablePointer<SSLSessionState>) -> OSStatus
```

```c
OSStatus SSLGetSessionState(SSLContextRef context, SSLSessionState *state);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Parameters

- `context`: An SSL session context reference.
- `state`: On return, points to a constant that indicates the state of the SSL session. See [`SSLSessionState`](./sslsessionstate.md) for possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetsessionstate(_:_:))*