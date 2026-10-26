# readCallBack

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

The callback is called when data is available to be read or a new connection is waiting to be accepted. The data is not automatically read; the callback must read the data itself.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
static var readCallBack: CFSocketCallBackType { get }
```

```c
kCFSocketReadCallBack
```

## See Also

### Constants
- [static var acceptCallBack: CFSocketCallBackType](./acceptcallback.md)
  New connections will be automatically accepted and the callback is called with the data argument being a pointer to a [`CFSocketNativeHandle`](../cfsocketnativehandle.md) of the child socket. This callback is usable only with listening sockets.
- [static var dataCallBack: CFSocketCallBackType](./datacallback.md)
  Incoming data will be read in chunks in the background and the callback is called with the data argument being a CFData object containing the read data.
- [static var connectCallBack: CFSocketCallBackType](./connectcallback.md)
- [static var writeCallBack: CFSocketCallBackType](./writecallback.md)
  The callback is called when the socket is writable. This callback type may be useful when large amounts of data are being sent rapidly over the socket and you want a notification when there is space in the kernel buffers for more data.
- [kCFSocketNoCallBack](./kcfsocketnocallback.md)
  No callback should be made for any activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype/readcallback)*