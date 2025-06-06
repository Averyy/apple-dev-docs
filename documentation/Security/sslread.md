# SSLRead(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Performs a normal application-level read operation.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func SSLRead(_ context: SSLContext, _ data: UnsafeMutableRawPointer, _ dataLength: Int, _ processed: UnsafeMutablePointer<Int>) -> OSStatus
```

## Mentions

- [Using the Secure Socket Layer for Network Communication](using-the-secure-socket-layer-for-network-communication.md)

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

The [`SSLRead(_:_:_:_:)`](sslread(_:_:_:_:).md) function might call the [`SSLReadFunc`](sslreadfunc.md) function that you provide (see [`SSLSetIOFuncs(_:_:_:)`](sslsetiofuncs(_:_:_:).md). Because you may configure the underlying connection to operate in a nonblocking manner, a read operation might return `errSSLWouldBlock`, indicating that less data than requested was actually transferred. In this case, you should repeat the call to [`SSLRead(_:_:_:_:)`](sslread(_:_:_:_:).md) until some other result is returned.

## Parameters

- `context`: An SSL session context reference.
- `data`: On return, points to the data read. You must allocate this buffer before calling the function. The size of this buffer must be equal to or greater than the value in the   parameter.
- `dataLength`: The amount of data you would like to read.
- `processed`: On return, points to the number of bytes actually read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslread(_:_:_:_:))*