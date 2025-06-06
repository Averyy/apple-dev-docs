# acceptCallBack

**Framework**: Core Foundation  
**Kind**: property

New connections will be automatically accepted and the callback is called with the data argument being a pointer to a [`CFSocketNativeHandle`](cfsocketnativehandle.md) of the child socket. This callback is usable only with listening sockets.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static var acceptCallBack: CFSocketCallBackType { get }
```

## See Also

- [static var readCallBack: CFSocketCallBackType](cfsocketcallbacktype/readcallback.md)
  The callback is called when data is available to be read or a new connection is waiting to be accepted. The data is not automatically read; the callback must read the data itself.
- [static var dataCallBack: CFSocketCallBackType](cfsocketcallbacktype/datacallback.md)
  Incoming data will be read in chunks in the background and the callback is called with the data argument being a CFData object containing the read data.
- [static var connectCallBack: CFSocketCallBackType](cfsocketcallbacktype/connectcallback.md)
- [static var writeCallBack: CFSocketCallBackType](cfsocketcallbacktype/writecallback.md)
  The callback is called when the socket is writable. This callback type may be useful when large amounts of data are being sent rapidly over the socket and you want a notification when there is space in the kernel buffers for more data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype/acceptcallback)*