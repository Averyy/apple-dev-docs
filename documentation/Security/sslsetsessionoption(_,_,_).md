# SSLSetSessionOption(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Specifies options for a specific session.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.6+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLSetSessionOption(_ context: SSLContext, _ option: SSLSessionOption, _ value: Bool) -> OSStatus
```

```c
OSStatus SSLSetSessionOption(SSLContextRef context, SSLSessionOption option, Boolean value);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

This function must be called prior to the [`SSLHandshake(_:)`](./sslhandshake%28_%29.md) function; consequently, this function can be called only when no session is active.

## Parameters

- `context`: An SSL session context reference.
- `option`: An SSL session option. Possible values are listed in [`SSLSessionOption`](./sslsessionoption.md).
- `value`: Set to [`true`](../Swift/true.md) to enable the option, or [`false`](../Swift/false.md) to disable it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetsessionoption(_:_:_:))*