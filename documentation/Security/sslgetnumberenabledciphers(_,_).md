# SSLGetNumberEnabledCiphers(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Determines the number of cipher suites currently enabled.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLGetNumberEnabledCiphers(_ context: SSLContext, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus
```

```c
OSStatus SSLGetNumberEnabledCiphers(SSLContextRef context, size_t *numCiphers);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

You use the number of enabled cipher suites returned by this function when you call the [`SSLGetEnabledCiphers(_:_:_:)`](./sslgetenabledciphers%28_,_,_%29.md) function to retrieve the list of currently enabled cipher suites.

## Parameters

- `context`: An SSL session context reference.
- `numCiphers`: On return, points to the number of enabled cipher suites.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetnumberenabledciphers(_:_:))*