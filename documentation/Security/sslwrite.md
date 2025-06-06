# SSLWrite(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Performs a typical application-level write operation.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func SSLWrite(_ context: SSLContext, _ data: UnsafeRawPointer?, _ dataLength: Int, _ processed: UnsafeMutablePointer<Int>) -> OSStatus
```

## Mentions

- [Using the Secure Socket Layer for Network Communication](using-the-secure-socket-layer-for-network-communication.md)

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

The [`SSLWrite(_:_:_:_:)`](sslwrite(_:_:_:_:).md) function might call the [`SSLWriteFunc`](sslwritefunc.md) function that you provide (see [`SSLSetIOFuncs(_:_:_:)`](sslsetiofuncs(_:_:_:).md)). Because you may configure the underlying connection to operate in a no-blocking manner, a write operation might return `errSSLWouldBlock`, indicating that less data than requested was actually transferred. In this case, you should repeat the call to [`SSLWrite(_:_:_:_:)`](sslwrite(_:_:_:_:).md) until some other result is returned.

## Parameters

- `context`: An SSL session context reference.
- `data`: A pointer to the buffer of data to write.
- `dataLength`: The amount, in bytes, of data to write.
- `processed`: On return, the length, in bytes, of the data actually written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslwrite(_:_:_:_:))*