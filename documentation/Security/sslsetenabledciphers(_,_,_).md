# SSLSetEnabledCiphers(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Specifies a restricted set of SSL cipher suites to be enabled by the current SSL session context.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLSetEnabledCiphers(_ context: SSLContext, _ ciphers: UnsafePointer<SSLCipherSuite>, _ numCiphers: Int) -> OSStatus
```

```c
OSStatus SSLSetEnabledCiphers(SSLContextRef context, const SSLCipherSuite *ciphers, size_t numCiphers);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

You can call this function, for example, to limit cipher suites to those that use exportable key sizes or to those supported by a particular protocol version.

This function can be called only when no session is active. The default set of enabled cipher suites is the complete set of supported cipher suites obtained by calling the [`SSLGetSupportedCiphers(_:_:_:)`](./sslgetsupportedciphers%28_,_,_%29.md) function.

Call the [`SSLGetEnabledCiphers(_:_:_:)`](./sslgetenabledciphers%28_,_,_%29.md) function to determine which SSL cipher suites are currently enabled.

## Parameters

- `context`: An SSL session context reference.
- `ciphers`: A pointer to the cipher suites to enable.
- `numCiphers`: The number of cipher suites to enable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetenabledciphers(_:_:_:))*