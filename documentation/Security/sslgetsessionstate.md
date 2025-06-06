# SSLGetSessionState(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the state of an SSL session.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func SSLGetSessionState(_ context: SSLContext, _ state: UnsafeMutablePointer<SSLSessionState>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

## Parameters

- `context`: An SSL session context reference.
- `state`: On return, points to a constant that indicates the state of the SSL session. See   for possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetsessionstate(_:_:))*