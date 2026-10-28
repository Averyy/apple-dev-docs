# CFSocketGetTypeID()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the type identifier for the CFSocket opaque type.

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
func CFSocketGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CFSocketGetTypeID();
```

## Return Value

The type identifier for the CFSocket opaque type.

## See Also

### Using Sockets
- [func CFSocketConnectToAddress(CFSocket!, CFData!, CFTimeInterval) -> CFSocketError](./cfsocketconnecttoaddress%28_,_,_%29.md)
  Opens a connection to a remote socket.
- [func CFSocketCreateRunLoopSource(CFAllocator!, CFSocket!, CFIndex) -> CFRunLoopSource!](./cfsocketcreaterunloopsource%28_,_,_%29.md)
  Creates a CFRunLoopSource object for a CFSocket object.
- [func CFSocketInvalidate(CFSocket!)](./cfsocketinvalidate%28_%29.md)
  Invalidates a CFSocket object, stopping it from sending or receiving any more messages.
- [func CFSocketIsValid(CFSocket!) -> Bool](./cfsocketisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFSocket object is valid and able to send or receive messages.
- [func CFSocketSendData(CFSocket!, CFData!, CFData!, CFTimeInterval) -> CFSocketError](./cfsocketsenddata%28_,_,_,_%29.md)
  Sends data over a CFSocket object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketgettypeid())*