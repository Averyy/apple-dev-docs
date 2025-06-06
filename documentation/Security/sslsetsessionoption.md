# SSLSetSessionOption(_:_:_:)

**Framework**: Security  
**Kind**: func

Specifies options for a specific session.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+

## Declaration

```swift
func SSLSetSessionOption(_ context: SSLContext, _ option: SSLSessionOption, _ value: Bool) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

This function must be called prior to the [`SSLHandshake(_:)`](sslhandshake(_:).md) function; consequently, this function can be called only when no session is active.

## Parameters

- `context`: An SSL session context reference.
- `option`: An SSL session option. Possible values are listed in  .
- `value`: Set to   to enable the option, or   to disable it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetsessionoption(_:_:_:))*