# CFSocketIsValid(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a Boolean value that indicates whether a CFSocket object is valid and able to send or receive messages.

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
func CFSocketIsValid(_ s: CFSocket!) -> Bool
```

#### Return Value

`true` if `s` can be used for communication, otherwise `false`.

## Parameters

- `s`: The CFSocket object to examine.

## See Also

- [func CFSocketConnectToAddress(CFSocket!, CFData!, CFTimeInterval) -> CFSocketError](cfsocketconnecttoaddress(_:_:_:).md)
  Opens a connection to a remote socket.
- [func CFSocketCreateRunLoopSource(CFAllocator!, CFSocket!, CFIndex) -> CFRunLoopSource!](cfsocketcreaterunloopsource(_:_:_:).md)
  Creates a CFRunLoopSource object for a CFSocket object.
- [func CFSocketGetTypeID() -> CFTypeID](cfsocketgettypeid().md)
  Returns the type identifier for the CFSocket opaque type.
- [func CFSocketInvalidate(CFSocket!)](cfsocketinvalidate(_:).md)
  Invalidates a CFSocket object, stopping it from sending or receiving any more messages.
- [func CFSocketSendData(CFSocket!, CFData!, CFData!, CFTimeInterval) -> CFSocketError](cfsocketsenddata(_:_:_:_:).md)
  Sends data over a CFSocket object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketisvalid(_:))*