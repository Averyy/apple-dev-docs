# SSLWriteFunc

**Framework**: Security  
**Kind**: typealias

A pointer to a customized write function that secure transport calls to write data to the connection.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias SSLWriteFunc = (SSLConnectionRef, UnsafeRawPointer, UnsafeMutablePointer<Int>) -> OSStatus
```

## Mentions

- [Using the Secure Socket Layer for Network Communication](using-the-secure-socket-layer-for-network-communication.md)

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

Before using the secure transport API, you must write the functions [`SSLReadFunc`](sslreadfunc.md) and [`SSLWriteFunc`](sslwritefunc.md) and provide them to the library by calling the [`SSLSetIOFuncs(_:_:_:)`](sslsetiofuncs(_:_:_:).md) function.

You may configure the underlying connection to operate in a non-blocking manner. In that case, a write operation may well return [`errSSLWouldBlock`](errsslwouldblock.md), indicating less data than requested was transferred and nothing is wrong except that the requested I/O hasn’t completed. This result is returned to the caller from the functions [`SSLRead(_:_:_:_:)`](sslread(_:_:_:_:).md), [`SSLWrite(_:_:_:_:)`](sslwrite(_:_:_:_:).md), or [`SSLHandshake(_:)`](sslhandshake(_:).md).

## Parameters

- `connection`: The SSL session connection reference.
- `data`: A pointer to the data to write to the connection.You must allocate this memory before calling this function.
- `dataLength`: Before calling, an integer representing the length of the data in bytes. On return, this is the number of bytes actually transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslwritefunc)*