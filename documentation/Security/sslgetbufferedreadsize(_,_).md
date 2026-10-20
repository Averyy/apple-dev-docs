# SSLGetBufferedReadSize(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Determines how much data is available to be read.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLGetBufferedReadSize(_ context: SSLContext, _ bufferSize: UnsafeMutablePointer<Int>) -> OSStatus
```

```c
OSStatus SSLGetBufferedReadSize(SSLContextRef context, size_t *bufferSize);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

This function determines how much data you can be guaranteed to obtain in a call to the [`SSLRead(_:_:_:_:)`](./sslread%28_,_,_,_%29.md) function. This function does not block or cause any low-level read operations to occur.

## Parameters

- `context`: An SSL session context reference.
- `bufferSize`: On return, the size of the data to be read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetbufferedreadsize(_:_:))*