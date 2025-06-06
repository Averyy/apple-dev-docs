# CFSocketGetTypeID()

**Framework**: Core Foundation  
**Kind**: func

Returns the type identifier for the CFSocket opaque type.

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
func CFSocketGetTypeID() -> CFTypeID
```

#### Return Value

The type identifier for the CFSocket opaque type.

## See Also

- [func CFSocketConnectToAddress(CFSocket!, CFData!, CFTimeInterval) -> CFSocketError](cfsocketconnecttoaddress(_:_:_:).md)
  Opens a connection to a remote socket.
- [func CFSocketCreateRunLoopSource(CFAllocator!, CFSocket!, CFIndex) -> CFRunLoopSource!](cfsocketcreaterunloopsource(_:_:_:).md)
  Creates a CFRunLoopSource object for a CFSocket object.
- [func CFSocketInvalidate(CFSocket!)](cfsocketinvalidate(_:).md)
  Invalidates a CFSocket object, stopping it from sending or receiving any more messages.
- [func CFSocketIsValid(CFSocket!) -> Bool](cfsocketisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFSocket object is valid and able to send or receive messages.
- [func CFSocketSendData(CFSocket!, CFData!, CFData!, CFTimeInterval) -> CFSocketError](cfsocketsenddata(_:_:_:_:).md)
  Sends data over a CFSocket object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketgettypeid())*