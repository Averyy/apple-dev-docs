# SSLWrite(_:_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Performs a typical application-level write operation.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLWrite(_ context: SSLContext, _ data: UnsafeRawPointer?, _ dataLength: Int, _ processed: UnsafeMutablePointer<Int>) -> OSStatus
```

```c
OSStatus SSLWrite(SSLContextRef context, const void *data, size_t dataLength, size_t *processed);
```

## Mentions

- [Using the Secure Socket Layer for Network Communication](./using-the-secure-socket-layer-for-network-communication.md)

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

The [`SSLWrite(_:_:_:_:)`](./sslwrite%28_,_,_,_%29.md) function might call the [`SSLWriteFunc`](./sslwritefunc.md) function that you provide (see [`SSLSetIOFuncs(_:_:_:)`](./sslsetiofuncs%28_,_,_%29.md)). Because you may configure the underlying connection to operate in a no-blocking manner, a write operation might return `errSSLWouldBlock`, indicating that less data than requested was actually transferred. In this case, you should repeat the call to [`SSLWrite(_:_:_:_:)`](./sslwrite%28_,_,_,_%29.md) until some other result is returned.

## Parameters

- `context`: An SSL session context reference.
- `data`: A pointer to the buffer of data to write.
- `dataLength`: The amount, in bytes, of data to write.
- `processed`: On return, the length, in bytes, of the data actually written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslwrite(_:_:_:_:))*