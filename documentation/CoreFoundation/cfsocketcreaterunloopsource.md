# CFSocketCreateRunLoopSource(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a CFRunLoopSource object for a CFSocket object.

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
func CFSocketCreateRunLoopSource(_ allocator: CFAllocator!, _ s: CFSocket!, _ order: CFIndex) -> CFRunLoopSource!
```

#### Return Value

The new CFRunLoopSource object for `s`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The run loop source is not automatically added to a run loop. To add the source to a run loop, use [`CFRunLoopAddSource(_:_:_:)`](cfrunloopaddsource(_:_:_:).md).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `s`: The CFSocket object for which to create a run loop source.
- `order`: A priority index indicating the order in which run loop sources are processed. When multiple run loop sources are firing in a single pass through the run loop, the sources are processed in increasing order of this parameter. If the run loop is set to process only one source per loop, only the highest priority source, the one with the lowest   value, is processed.

## See Also

- [func CFSocketConnectToAddress(CFSocket!, CFData!, CFTimeInterval) -> CFSocketError](cfsocketconnecttoaddress(_:_:_:).md)
  Opens a connection to a remote socket.
- [func CFSocketGetTypeID() -> CFTypeID](cfsocketgettypeid().md)
  Returns the type identifier for the CFSocket opaque type.
- [func CFSocketInvalidate(CFSocket!)](cfsocketinvalidate(_:).md)
  Invalidates a CFSocket object, stopping it from sending or receiving any more messages.
- [func CFSocketIsValid(CFSocket!) -> Bool](cfsocketisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFSocket object is valid and able to send or receive messages.
- [func CFSocketSendData(CFSocket!, CFData!, CFData!, CFTimeInterval) -> CFSocketError](cfsocketsenddata(_:_:_:_:).md)
  Sends data over a CFSocket object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketcreaterunloopsource(_:_:_:))*