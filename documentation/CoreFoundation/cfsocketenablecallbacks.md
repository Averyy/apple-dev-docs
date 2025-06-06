# CFSocketEnableCallBacks(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Enables the callback function of a CFSocket object for certain types of socket activity.

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
func CFSocketEnableCallBacks(_ s: CFSocket!, _ callBackTypes: CFOptionFlags)
```

#### Discussion

If a callback type is not automatically reenabled, you can use this function to enable the callback (once).

This call does not affect whether the callback type will be automatically reenabled in the future; use [`CFSocketSetSocketFlags(_:_:)`](cfsocketsetsocketflags(_:_:).md) if you want to set a callback type to be reenabled automatically.

Be sure to enable only callback types that your CFSocket object actually possesses and has requested when creating the CFSocket object; the result of enabling other callback types is undefined.

## Parameters

- `s`: The CFSocket object to modify.
- `callBackTypes`: A bitwise-OR combination of CFSocket activity types that should cause the callback function of   to be called. See   for a list of callback types.

## See Also

- [func CFSocketCopyAddress(CFSocket!) -> CFData!](cfsocketcopyaddress(_:).md)
  Returns the local address of a CFSocket object.
- [func CFSocketCopyPeerAddress(CFSocket!) -> CFData!](cfsocketcopypeeraddress(_:).md)
  Returns the remote address to which a CFSocket object is connected.
- [func CFSocketDisableCallBacks(CFSocket!, CFOptionFlags)](cfsocketdisablecallbacks(_:_:).md)
  Disables the callback function of a CFSocket object for certain types of socket activity.
- [func CFSocketGetContext(CFSocket!, UnsafeMutablePointer<CFSocketContext>!)](cfsocketgetcontext(_:_:).md)
  Returns the context information for a CFSocket object.
- [func CFSocketGetNative(CFSocket!) -> CFSocketNativeHandle](cfsocketgetnative(_:).md)
  Returns the native socket associated with a CFSocket object.
- [func CFSocketGetSocketFlags(CFSocket!) -> CFOptionFlags](cfsocketgetsocketflags(_:).md)
  Returns flags that control certain behaviors of a CFSocket object.
- [func CFSocketSetAddress(CFSocket!, CFData!) -> CFSocketError](cfsocketsetaddress(_:_:).md)
  Binds a local address to a CFSocket object and configures it for listening.
- [func CFSocketSetSocketFlags(CFSocket!, CFOptionFlags)](cfsocketsetsocketflags(_:_:).md)
  Sets flags that control certain behaviors of a CFSocket object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketenablecallbacks(_:_:))*