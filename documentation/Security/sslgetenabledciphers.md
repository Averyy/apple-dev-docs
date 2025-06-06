# SSLGetEnabledCiphers(_:_:_:)

**Framework**: Security  
**Kind**: func

Determines which SSL cipher suites are currently enabled.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func SSLGetEnabledCiphers(_ context: SSLContext, _ ciphers: UnsafeMutablePointer<SSLCipherSuite>, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md). If the supplied buffer is too small, [`errSSLBufferOverflow`](errsslbufferoverflow.md) is returned.

#### Discussion

Call the [`SSLSetEnabledCiphers(_:_:_:)`](sslsetenabledciphers(_:_:_:).md) function to specify which SSL cipher suites are enabled.

## Parameters

- `context`: An SSL session context reference.
- `ciphers`: On return, points to the enabled cipher suites. Before calling, you must allocate this buffer using the number of enabled cipher suites retrieved from a call to the   function.
- `numCiphers`: Pointer to the number of enabled cipher suites. Before calling, retrieve this value by calling the   function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetenabledciphers(_:_:_:))*