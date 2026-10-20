# SSLReadFunc

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

A pointer to a customized read function that secure transport calls to read data from the connection.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias SSLReadFunc = (SSLConnectionRef, UnsafeMutableRawPointer, UnsafeMutablePointer<Int>) -> OSStatus
```

```c
typedef int (*)(const void *, void *, unsigned long *) SSLReadFunc;
```

## Mentions

- [Using the Secure Socket Layer for Network Communication](./using-the-secure-socket-layer-for-network-communication.md)

#### Return Value

Your callback must return an appropriate result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

Before using the secure transport API, you must create a read function (conforming to the [`SSLReadFunc`](./sslreadfunc.md) prototype) and a write function (conforming to  the [`SSLWriteFunc`](./sslwritefunc.md) prototype) and provide them to the library by calling the [`SSLSetIOFuncs(_:_:_:)`](./sslsetiofuncs%28_,_,_%29.md) function.

You may configure the underlying connection to operate in a non-blocking manner; in that case, a read operation may well return [`errSSLWouldBlock`](./errsslwouldblock.md), indicating less data than requested was transferred and nothing is wrong except that the requested I/O hasn’t completed. This result is returned to the caller from the functions [`SSLRead(_:_:_:_:)`](./sslread%28_,_,_,_%29.md), [`SSLWrite(_:_:_:_:)`](./sslwrite%28_,_,_,_%29.md), or [`SSLHandshake(_:)`](./sslhandshake%28_%29.md).

## Parameters

- `connection`: A connection reference.
- `data`: On return, your callback should overwrite the memory at this location with the data read from the connection.
- `dataLength`: On input, a pointer to an integer representing the length of the data in bytes. On return, your callback should overwrite that integer with the number of bytes actually transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslreadfunc)*