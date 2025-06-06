# CFSocketGetContext(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the context information for a CFSocket object.

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
func CFSocketGetContext(_ s: CFSocket!, _ context: UnsafeMutablePointer<CFSocketContext>!)
```

#### Discussion

The context version number for CFSocket is currently 0. Before calling this function, you need to initialize the `version` member of `context` to 0.

## Parameters

- `s`: The CFSocket object to examine.
- `context`: A pointer to the structure into which the context information for   is to be copied. The information being returned is usually the same information you passed to  ,  ,  , or   when creating the CFSocket object. However, if   returned a cached CFSocket object instead of creating a new object,   is filled with information from the original CFSocket object instead of the information you passed to the function.

## See Also

- [func CFSocketCopyAddress(CFSocket!) -> CFData!](cfsocketcopyaddress(_:).md)
  Returns the local address of a CFSocket object.
- [func CFSocketCopyPeerAddress(CFSocket!) -> CFData!](cfsocketcopypeeraddress(_:).md)
  Returns the remote address to which a CFSocket object is connected.
- [func CFSocketDisableCallBacks(CFSocket!, CFOptionFlags)](cfsocketdisablecallbacks(_:_:).md)
  Disables the callback function of a CFSocket object for certain types of socket activity.
- [func CFSocketEnableCallBacks(CFSocket!, CFOptionFlags)](cfsocketenablecallbacks(_:_:).md)
  Enables the callback function of a CFSocket object for certain types of socket activity.
- [func CFSocketGetNative(CFSocket!) -> CFSocketNativeHandle](cfsocketgetnative(_:).md)
  Returns the native socket associated with a CFSocket object.
- [func CFSocketGetSocketFlags(CFSocket!) -> CFOptionFlags](cfsocketgetsocketflags(_:).md)
  Returns flags that control certain behaviors of a CFSocket object.
- [func CFSocketSetAddress(CFSocket!, CFData!) -> CFSocketError](cfsocketsetaddress(_:_:).md)
  Binds a local address to a CFSocket object and configures it for listening.
- [func CFSocketSetSocketFlags(CFSocket!, CFOptionFlags)](cfsocketsetsocketflags(_:_:).md)
  Sets flags that control certain behaviors of a CFSocket object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketgetcontext(_:_:))*