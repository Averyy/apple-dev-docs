# CFSocketSetAddress(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Binds a local address to a CFSocket object and configures it for listening.

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
func CFSocketSetAddress(_ s: CFSocket!, _ address: CFData!) -> CFSocketError
```

#### Return Value

An error code indicating success or failure.

#### Discussion

This function binds the socket by calling bind, and if the socket supports it, configures the socket for listening by calling listen with a backlog of 256.

Once `s` is bound to `address`, depending on the socket’s protocol, other processes and computers can connect to `s`.

## Parameters

- `s`: The CFSocket object to modify.
- `address`: A CFData object containing a   appropriate for the protocol family of   (  or  , for example). This data object is used only for the duration of the function call.

## See Also

- [func CFSocketCopyAddress(CFSocket!) -> CFData!](cfsocketcopyaddress(_:).md)
  Returns the local address of a CFSocket object.
- [func CFSocketCopyPeerAddress(CFSocket!) -> CFData!](cfsocketcopypeeraddress(_:).md)
  Returns the remote address to which a CFSocket object is connected.
- [func CFSocketDisableCallBacks(CFSocket!, CFOptionFlags)](cfsocketdisablecallbacks(_:_:).md)
  Disables the callback function of a CFSocket object for certain types of socket activity.
- [func CFSocketEnableCallBacks(CFSocket!, CFOptionFlags)](cfsocketenablecallbacks(_:_:).md)
  Enables the callback function of a CFSocket object for certain types of socket activity.
- [func CFSocketGetContext(CFSocket!, UnsafeMutablePointer<CFSocketContext>!)](cfsocketgetcontext(_:_:).md)
  Returns the context information for a CFSocket object.
- [func CFSocketGetNative(CFSocket!) -> CFSocketNativeHandle](cfsocketgetnative(_:).md)
  Returns the native socket associated with a CFSocket object.
- [func CFSocketGetSocketFlags(CFSocket!) -> CFOptionFlags](cfsocketgetsocketflags(_:).md)
  Returns flags that control certain behaviors of a CFSocket object.
- [func CFSocketSetSocketFlags(CFSocket!, CFOptionFlags)](cfsocketsetsocketflags(_:_:).md)
  Sets flags that control certain behaviors of a CFSocket object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketsetaddress(_:_:))*