# SSLGetSupportedCiphers(_:_:_:)

**Framework**: Security  
**Kind**: func

Determines the values of the supported cipher suites.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func SSLGetSupportedCiphers(_ context: SSLContext, _ ciphers: UnsafeMutablePointer<SSLCipherSuite>, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md). If the supplied buffer is too small, [`errSSLBufferOverflow`](errsslbufferoverflow.md) is returned.

#### Discussion

All the supported cipher suites are enabled by default. Use the [`SSLSetEnabledCiphers(_:_:_:)`](sslsetenabledciphers(_:_:_:).md) function to enable a subset of the supported cipher suites. Use the [`SSLGetEnabledCiphers(_:_:_:)`](sslgetenabledciphers(_:_:_:).md) function to determine which cipher suites are currently enabled.

## Parameters

- `context`: An SSL session context reference.
- `ciphers`: On return, points to the values of the supported cipher suites. Before calling, you must allocate this buffer using the number of supported cipher suites retrieved from a call to the   function.
- `numCiphers`: Points to the number of supported cipher suites that you want returned. Before calling, retrieve this value by calling the   function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetsupportedciphers(_:_:_:))*