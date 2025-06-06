# SSLGetSessionOption(_:_:_:)

**Framework**: Security  
**Kind**: func

Indicates the current setting of Secure Sockets Layer (SSL) session options.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+

## Declaration

```swift
func SSLGetSessionOption(_ context: SSLContext, _ option: SSLSessionOption, _ value: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

## Parameters

- `context`: An SSL session context reference.
- `option`: An SSL session option. Possible values are listed in  .
- `value`: On return,   if the option is enabled, or   otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetsessionoption(_:_:_:))*