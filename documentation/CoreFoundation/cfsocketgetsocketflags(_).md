# CFSocketGetSocketFlags(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns flags that control certain behaviors of a CFSocket object.

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
func CFSocketGetSocketFlags(_ s: CFSocket!) -> CFOptionFlags
```

```c
extern CFOptionFlags CFSocketGetSocketFlags(CFSocketRef s);
```

#### Return Value

A bitwise-OR combination of flags controlling the behavior of `s`. See [CFSocket Flags](./api-1560944-cfsocket-flags.md) for the list of available flags.

#### Discussion

See [`CFSocketSetSocketFlags(_:_:)`](./cfsocketsetsocketflags%28_,_%29.md) for details on what the flags of a CFSocket mean.

## Parameters

- `s`: The CFSocket to examine.

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
- [func CFSocketGetContext(CFSocket!, UnsafeMutablePointer<CFSocketContext>!)](./cfsocketgetcontext%28_,_%29.md)
  Returns the context information for a CFSocket object.
- [func CFSocketGetNative(CFSocket!) -> CFSocketNativeHandle](./cfsocketgetnative%28_%29.md)
  Returns the native socket associated with a CFSocket object.
- [func CFSocketSetAddress(CFSocket!, CFData!) -> CFSocketError](./cfsocketsetaddress%28_,_%29.md)
  Binds a local address to a CFSocket object and configures it for listening.
- [func CFSocketSetSocketFlags(CFSocket!, CFOptionFlags)](./cfsocketsetsocketflags%28_,_%29.md)
  Sets flags that control certain behaviors of a CFSocket object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketgetsocketflags(_:))*