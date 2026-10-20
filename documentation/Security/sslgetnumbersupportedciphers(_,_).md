# SSLGetNumberSupportedCiphers(_:_:)

**Framework**: Security  
**Kind**: func

Determines the number of cipher suites supported.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func SSLGetNumberSupportedCiphers(_ context: SSLContext, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

You use the number of enabled cipher suites returned by this function when you call the [`SSLGetNumberSupportedCiphers(_:_:)`](sslgetnumbersupportedciphers(_:_:).md) function to retrieve the list of currently enabled cipher suites.

## Parameters

- `context`: An SSL session context reference.
- `numCiphers`: On return, points to the number of supported cipher suites.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetnumbersupportedciphers(_:_:))*