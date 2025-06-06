# CFSocketInvalidate(_:)

**Framework**: Core Foundation  
**Kind**: func

Invalidates a CFSocket object, stopping it from sending or receiving any more messages.

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
func CFSocketInvalidate(_ s: CFSocket!)
```

#### Discussion

You should always invalidate a socket object when you are through using it. Invalidating a CFSocket object prevents the object from sending or receiving any more messages, but does not release the socket object itself.

If a run loop source was created for `s`, the run loop source is invalidated.

If a release callback was specified in [`CFSocketContext`](cfsocketcontext.md) object, this function calls it to release the object in the  `info` field (which was provided when `s` was created).

By default, this call closes the underlying socket. If you have explicitly cleared the `kCFSocketCloseOnInvalidate` flag by calling [`CFSocketSetSocketFlags(_:_:)`](cfsocketsetsocketflags(_:_:).md), you must close the socket yourself  calling this function.

## Parameters

- `s`: The CFSocket object to invalidate.

## See Also

- [func CFSocketConnectToAddress(CFSocket!, CFData!, CFTimeInterval) -> CFSocketError](cfsocketconnecttoaddress(_:_:_:).md)
  Opens a connection to a remote socket.
- [func CFSocketCreateRunLoopSource(CFAllocator!, CFSocket!, CFIndex) -> CFRunLoopSource!](cfsocketcreaterunloopsource(_:_:_:).md)
  Creates a CFRunLoopSource object for a CFSocket object.
- [func CFSocketGetTypeID() -> CFTypeID](cfsocketgettypeid().md)
  Returns the type identifier for the CFSocket opaque type.
- [func CFSocketIsValid(CFSocket!) -> Bool](cfsocketisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFSocket object is valid and able to send or receive messages.
- [func CFSocketSendData(CFSocket!, CFData!, CFData!, CFTimeInterval) -> CFSocketError](cfsocketsenddata(_:_:_:_:).md)
  Sends data over a CFSocket object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketinvalidate(_:))*