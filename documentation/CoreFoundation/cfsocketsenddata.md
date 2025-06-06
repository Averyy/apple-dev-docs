# CFSocketSendData(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sends data over a CFSocket object.

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
func CFSocketSendData(_ s: CFSocket!, _ address: CFData!, _ data: CFData!, _ timeout: CFTimeInterval) -> CFSocketError
```

#### Return Value

An error code indicating success or failure.

#### Discussion

This function sets the send timeout of the underlying socket (the `SO_SNDTIMEO` option at the `SOL_SOCKET` level), then calls send (or sendto if you provided an address) with the provided data.

This function makes no attempt to queue data for delivery beyond the queueing provided by the socket buffer itself. This means:

- If this function returns [`CFSocketError.success`](cfsocketerror/success.md), then by the time it returns, the data has been queued in the socket buffer for delivery.
- If the socket buffer is full and the timeout is nonzero, the function may return an error. If this happens, the app should wait for the socket buffer to have enough space available for writing before calling this function again.

## Parameters

- `s`: The CFSocket object to use.
- `address`: The address, stored as a   appropriate for the protocol family (  or  , for example) in a CFData object, to which to send the contents of  . If  , the data are sent to the address to which   is already connected. This data object is used only for the duration of the function call.
- `data`: The data to send.
- `timeout`: The time to wait for the data to be sent.

## See Also

- [func CFSocketConnectToAddress(CFSocket!, CFData!, CFTimeInterval) -> CFSocketError](cfsocketconnecttoaddress(_:_:_:).md)
  Opens a connection to a remote socket.
- [func CFSocketCreateRunLoopSource(CFAllocator!, CFSocket!, CFIndex) -> CFRunLoopSource!](cfsocketcreaterunloopsource(_:_:_:).md)
  Creates a CFRunLoopSource object for a CFSocket object.
- [func CFSocketGetTypeID() -> CFTypeID](cfsocketgettypeid().md)
  Returns the type identifier for the CFSocket opaque type.
- [func CFSocketInvalidate(CFSocket!)](cfsocketinvalidate(_:).md)
  Invalidates a CFSocket object, stopping it from sending or receiving any more messages.
- [func CFSocketIsValid(CFSocket!) -> Bool](cfsocketisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFSocket object is valid and able to send or receive messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketsenddata(_:_:_:_:))*