# SSLGetNegotiatedCipher(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the cipher suite negotiated for this session.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLGetNegotiatedCipher(_ context: SSLContext, _ cipherSuite: UnsafeMutablePointer<SSLCipherSuite>) -> OSStatus
```

```c
OSStatus SSLGetNegotiatedCipher(SSLContextRef context, SSLCipherSuite *cipherSuite);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

You should call this function only when a session is active.

## Parameters

- `context`: An SSL session context reference.
- `cipherSuite`: On return, points to the cipher suite that was negotiated for this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetnegotiatedcipher(_:_:))*