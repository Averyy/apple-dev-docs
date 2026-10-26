# connectCallBack

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

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
static var connectCallBack: CFSocketCallBackType { get }
```

```c
kCFSocketConnectCallBack
```

#### Discussion

If a connection attempt is made in the background by calling [`CFSocketConnectToAddress(_:_:_:)`](../cfsocketconnecttoaddress%28_,_,_%29.md) or [`CFSocketCreateConnectedToSocketSignature(_:_:_:_:_:_:)`](../cfsocketcreateconnectedtosocketsignature%28_,_,_,_,_,_%29.md) with a negative timeout value, this callback type is made when the connect finishes. In this case the data argument is either `NULL` or a pointer to an `SInt32` error code, if the connect failed. This callback will never be sent more than once for a given socket.

## See Also

### Constants
- [static var readCallBack: CFSocketCallBackType](./readcallback.md)
  The callback is called when data is available to be read or a new connection is waiting to be accepted. The data is not automatically read; the callback must read the data itself.
- [static var acceptCallBack: CFSocketCallBackType](./acceptcallback.md)
  New connections will be automatically accepted and the callback is called with the data argument being a pointer to a [`CFSocketNativeHandle`](../cfsocketnativehandle.md) of the child socket. This callback is usable only with listening sockets.
- [static var dataCallBack: CFSocketCallBackType](./datacallback.md)
  Incoming data will be read in chunks in the background and the callback is called with the data argument being a CFData object containing the read data.
- [static var writeCallBack: CFSocketCallBackType](./writecallback.md)
  The callback is called when the socket is writable. This callback type may be useful when large amounts of data are being sent rapidly over the socket and you want a notification when there is space in the kernel buffers for more data.
- [kCFSocketNoCallBack](./kcfsocketnocallback.md)
  No callback should be made for any activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype/connectcallback)*