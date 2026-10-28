# SSLGetSessionOption(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Indicates the current setting of Secure Sockets Layer (SSL) session options.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.6+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLGetSessionOption(_ context: SSLContext, _ option: SSLSessionOption, _ value: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus
```

```c
OSStatus SSLGetSessionOption(SSLContextRef context, SSLSessionOption option, Boolean *value);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Parameters

- `context`: An SSL session context reference.
- `option`: An SSL session option. Possible values are listed in [`SSLSessionOption`](./sslsessionoption.md).
- `value`: On return, `true` if the option is enabled, or `false` otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetsessionoption(_:_:_:))*