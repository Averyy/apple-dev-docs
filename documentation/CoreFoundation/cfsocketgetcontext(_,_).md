# CFSocketGetContext(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the context information for a CFSocket object.

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
func CFSocketGetContext(_ s: CFSocket!, _ context: UnsafeMutablePointer<CFSocketContext>!)
```

```c
extern void CFSocketGetContext(CFSocketRef s, CFSocketContext *context);
```

#### Discussion

The context version number for CFSocket is currently 0. Before calling this function, you need to initialize the `version` member of `context` to 0.

## Parameters

- `s`: The CFSocket object to examine.
- `context`: A pointer to the structure into which the context information for `s` is to be copied. The information being returned is usually the same information you passed to [`CFSocketCreate(_:_:_:_:_:_:_:)`](./cfsocketcreate%28_,_,_,_,_,_,_%29.md), [`CFSocketCreateConnectedToSocketSignature(_:_:_:_:_:_:)`](./cfsocketcreateconnectedtosocketsignature%28_,_,_,_,_,_%29.md), [`CFSocketCreateWithNative(_:_:_:_:_:)`](./cfsocketcreatewithnative%28_,_,_,_,_%29.md), or [`CFSocketCreateWithSocketSignature(_:_:_:_:_:)`](./cfsocketcreatewithsocketsignature%28_,_,_,_,_%29.md) when creating the CFSocket object. However, if [`CFSocketCreateWithNative(_:_:_:_:_:)`](./cfsocketcreatewithnative%28_,_,_,_,_%29.md) returned a cached CFSocket object instead of creating a new object, `context` is filled with information from the original CFSocket object instead of the information you passed to the function.

## See Also

### Configuring Sockets
- [func CFSocketCopyAddress(CFSocket!) -> CFData!](./cfsocketcopyaddress%28_%29.md)
  Returns the local address of a CFSocket object.
- [func CFSocketCopyPeerAddress(CFSocket!) -> CFData!](./cfsocketcopypeeraddress%28_%29.md)
  Returns the remote address to which a CFSocket object is connected.
- [func CFSocketDisableCallBacks(CFSocket!, CFOptionFlags)](./cfsocketdisablecallbacks%28_,_%29.md)
  Disables the callback function of a CFSocket object for certain types of socket activity.
- [func CFSocketEnableCallBacks(CFSocket!, CFOptionFlags)](./cfsocketenablecallbacks%28_,_%29.md)
  Enables the callback function of a CFSocket object for certain types of socket activity.
- [func CFSocketGetNative(CFSocket!) -> CFSocketNativeHandle](./cfsocketgetnative%28_%29.md)
  Returns the native socket associated with a CFSocket object.
- [func CFSocketGetSocketFlags(CFSocket!) -> CFOptionFlags](./cfsocketgetsocketflags%28_%29.md)
  Returns flags that control certain behaviors of a CFSocket object.
- [func CFSocketSetAddress(CFSocket!, CFData!) -> CFSocketError](./cfsocketsetaddress%28_,_%29.md)
  Binds a local address to a CFSocket object and configures it for listening.
- [func CFSocketSetSocketFlags(CFSocket!, CFOptionFlags)](./cfsocketsetsocketflags%28_,_%29.md)
  Sets flags that control certain behaviors of a CFSocket object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketgetcontext(_:_:))*