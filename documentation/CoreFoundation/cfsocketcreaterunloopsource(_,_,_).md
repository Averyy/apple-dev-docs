# CFSocketCreateRunLoopSource(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a CFRunLoopSource object for a CFSocket object.

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
func CFSocketCreateRunLoopSource(_ allocator: CFAllocator!, _ s: CFSocket!, _ order: CFIndex) -> CFRunLoopSource!
```

```c
extern CFRunLoopSourceRefCFSocketCreateRunLoopSource(CFAllocatorRef allocator, CFSocketRef s, CFIndex order);
```

#### Return Value

The new CFRunLoopSource object for `s`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The run loop source is not automatically added to a run loop. To add the source to a run loop, use [`CFRunLoopAddSource(_:_:_:)`](./cfrunloopaddsource%28_,_,_%29.md).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `s`: The CFSocket object for which to create a run loop source.
- `order`: A priority index indicating the order in which run loop sources are processed. When multiple run loop sources are firing in a single pass through the run loop, the sources are processed in increasing order of this parameter. If the run loop is set to process only one source per loop, only the highest priority source, the one with the lowest `order` value, is processed.

## See Also

### Using Sockets
- [func CFSocketConnectToAddress(CFSocket!, CFData!, CFTimeInterval) -> CFSocketError](./cfsocketconnecttoaddress%28_,_,_%29.md)
  Opens a connection to a remote socket.
- [func CFSocketGetTypeID() -> CFTypeID](./cfsocketgettypeid%28%29.md)
  Returns the type identifier for the CFSocket opaque type.
- [func CFSocketInvalidate(CFSocket!)](./cfsocketinvalidate%28_%29.md)
  Invalidates a CFSocket object, stopping it from sending or receiving any more messages.
- [func CFSocketIsValid(CFSocket!) -> Bool](./cfsocketisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFSocket object is valid and able to send or receive messages.
- [func CFSocketSendData(CFSocket!, CFData!, CFData!, CFTimeInterval) -> CFSocketError](./cfsocketsenddata%28_,_,_,_%29.md)
  Sends data over a CFSocket object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketcreaterunloopsource(_:_:_:))*