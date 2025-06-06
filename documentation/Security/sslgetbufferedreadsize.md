# SSLGetBufferedReadSize(_:_:)

**Framework**: Security  
**Kind**: func

Determines how much data is available to be read.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func SSLGetBufferedReadSize(_ context: SSLContext, _ bufferSize: UnsafeMutablePointer<Int>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

This function determines how much data you can be guaranteed to obtain in a call to the [`SSLRead(_:_:_:_:)`](sslread(_:_:_:_:).md) function. This function does not block or cause any low-level read operations to occur.

## Parameters

- `context`: An SSL session context reference.
- `bufferSize`: On return, the size of the data to be read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetbufferedreadsize(_:_:))*