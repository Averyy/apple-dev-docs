# CFSocketConnectToAddress(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Opens a connection to a remote socket.

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
func CFSocketConnectToAddress(_ s: CFSocket!, _ address: CFData!, _ timeout: CFTimeInterval) -> CFSocketError
```

#### Return Value

An error code indicating success or failure of the connection attempt.

## Parameters

- `s`: The CFSocket object with which to connect to  .
- `address`: A CFData object containing a   appropriate for the protocol family of   (  or  , for example), indicating the remote address to which to connect. This data object is used only for the duration of the function call.
- `timeout`: The time to wait for a connection to succeed. If a negative value is used, this function does not wait for the connection and instead lets the connection attempt happen in the background. If   requested a  , you will receive a callback when the background connection succeeds or fails.

## See Also

- [func CFSocketCreateRunLoopSource(CFAllocator!, CFSocket!, CFIndex) -> CFRunLoopSource!](cfsocketcreaterunloopsource(_:_:_:).md)
  Creates a CFRunLoopSource object for a CFSocket object.
- [func CFSocketGetTypeID() -> CFTypeID](cfsocketgettypeid().md)
  Returns the type identifier for the CFSocket opaque type.
- [func CFSocketInvalidate(CFSocket!)](cfsocketinvalidate(_:).md)
  Invalidates a CFSocket object, stopping it from sending or receiving any more messages.
- [func CFSocketIsValid(CFSocket!) -> Bool](cfsocketisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFSocket object is valid and able to send or receive messages.
- [func CFSocketSendData(CFSocket!, CFData!, CFData!, CFTimeInterval) -> CFSocketError](cfsocketsenddata(_:_:_:_:).md)
  Sends data over a CFSocket object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketconnecttoaddress(_:_:_:))*