# CFSocketCallBackType

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

Types of socket activity that can cause the callback function of a CFSocket object to be called.

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
struct CFSocketCallBackType
```

```c
enum CFSocketCallBackType : CFOptionFlags;
```

#### Overview

The callback types for which a callback is made is determined when the CFSocket object is created, such as with [`CFSocketCreate(_:_:_:_:_:_:_:)`](./cfsocketcreate%28_,_,_,_,_,_,_%29.md), or later with [`CFSocketEnableCallBacks(_:_:)`](./cfsocketenablecallbacks%28_,_%29.md) and [`CFSocketDisableCallBacks(_:_:)`](./cfsocketdisablecallbacks%28_,_%29.md).

The `kCFSocketReadCallBack`, `kCFSocketAcceptCallBack`, and `kCFSocketDataCallBack` callbacks are mutually exclusive.

##### Version-Notes

`kCFSocketWriteCallBack` is available in macOS 10.2 and later.

## Topics

### Constants
- [static var readCallBack: CFSocketCallBackType](./cfsocketcallbacktype/readcallback.md)
  The callback is called when data is available to be read or a new connection is waiting to be accepted. The data is not automatically read; the callback must read the data itself.
- [static var acceptCallBack: CFSocketCallBackType](./cfsocketcallbacktype/acceptcallback.md)
  New connections will be automatically accepted and the callback is called with the data argument being a pointer to a [`CFSocketNativeHandle`](./cfsocketnativehandle.md) of the child socket. This callback is usable only with listening sockets.
- [static var dataCallBack: CFSocketCallBackType](./cfsocketcallbacktype/datacallback.md)
  Incoming data will be read in chunks in the background and the callback is called with the data argument being a CFData object containing the read data.
- [static var connectCallBack: CFSocketCallBackType](./cfsocketcallbacktype/connectcallback.md)
- [static var writeCallBack: CFSocketCallBackType](./cfsocketcallbacktype/writecallback.md)
  The callback is called when the socket is writable. This callback type may be useful when large amounts of data are being sent rapidly over the socket and you want a notification when there is space in the kernel buffers for more data.
- [kCFSocketNoCallBack](./cfsocketcallbacktype/kcfsocketnocallback.md)
  No callback should be made for any activity.
### Initializers
- [init(rawValue: CFOptionFlags)](./cfsocketcallbacktype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Constants
- [CFSocket Flags](./api-1560944-cfsocket-flags.md)
  Flags that can be set on a CFSocket object to control its behavior.
- [enum CFSocketError](./cfsocketerror.md)
  Error codes for many CFSocket functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype)*