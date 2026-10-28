# CFSocketDisableCallBacks(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Disables the callback function of a CFSocket object for certain types of socket activity.

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
func CFSocketDisableCallBacks(_ s: CFSocket!, _ callBackTypes: CFOptionFlags)
```

```c
extern void CFSocketDisableCallBacks(CFSocketRef s, CFOptionFlags callBackTypes);
```

## Discussion

If you no longer want certain types of callbacks that you requested when creating `s`, you can use this function to temporarily disable the callback. Use [`CFSocketEnableCallBacks(_:_:)`](./cfsocketenablecallbacks%28_,_%29.md) to reenable a callback type.

## Parameters

- `s`: The CFSocket object to modify.
- `callBackTypes`: A bitwise-OR combination of CFSocket activity types that should not cause the callback function of `s` to be called. See [`CFSocketCallBackType`](./cfsocketcallbacktype.md) for a list of callback types.

## See Also

### Configuring Sockets
- [func CFSocketCopyAddress(CFSocket!) -> CFData!](./cfsocketcopyaddress%28_%29.md)
  Returns the local address of a CFSocket object.
- [func CFSocketCopyPeerAddress(CFSocket!) -> CFData!](./cfsocketcopypeeraddress%28_%29.md)
  Returns the remote address to which a CFSocket object is connected.
- [func CFSocketEnableCallBacks(CFSocket!, CFOptionFlags)](./cfsocketenablecallbacks%28_,_%29.md)
  Enables the callback function of a CFSocket object for certain types of socket activity.
- [func CFSocketGetContext(CFSocket!, UnsafeMutablePointer<CFSocketContext>!)](./cfsocketgetcontext%28_,_%29.md)
  Returns the context information for a CFSocket object.
- [func CFSocketGetNative(CFSocket!) -> CFSocketNativeHandle](./cfsocketgetnative%28_%29.md)
  Returns the native socket associated with a CFSocket object.
- [func CFSocketGetSocketFlags(CFSocket!) -> CFOptionFlags](./cfsocketgetsocketflags%28_%29.md)
  Returns flags that control certain behaviors of a CFSocket object.
- [func CFSocketSetAddress(CFSocket!, CFData!) -> CFSocketError](./cfsocketsetaddress%28_,_%29.md)
  Binds a local address to a CFSocket object and configures it for listening.
- [func CFSocketSetSocketFlags(CFSocket!, CFOptionFlags)](./cfsocketsetsocketflags%28_,_%29.md)
  Sets flags that control certain behaviors of a CFSocket object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketdisablecallbacks(_:_:))*