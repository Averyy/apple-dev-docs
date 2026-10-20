# CFMachPortCallBack

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

Callback invoked to process a message received on a CFMachPort object.

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
typealias CFMachPortCallBack = (CFMachPort?, UnsafeMutableRawPointer?, CFIndex, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(struct __CFMachPort *, void *, long, void *) CFMachPortCallBack;
```

#### Discussion

You specify this callback when creating a CFMachPort object with either [`CFMachPortCreate(_:_:_:_:)`](./cfmachportcreate%28_,_,_,_%29.md) or [`CFMachPortCreateWithPort(_:_:_:_:_:)`](./cfmachportcreatewithport%28_,_,_,_,_%29.md). To receive messages on a CFMachPort object (and have this callback invoked), you must create a run loop source for the port and add it to a run loop.

## Parameters

- `port`: The CFMachPort object on which the message `msg` was received.
- `msg`: The Mach message received on `port`. The pointer is to a `mach_msg_header_t` structure.
- `size`: Size of the Mach message `msg`, excluding the message trailer.
- `info`: The `info` member of the [`CFMachPortContext`](./cfmachportcontext.md) structure used when creating `port`.

## See Also

### Callbacks
- [typealias CFMachPortInvalidationCallBack](./cfmachportinvalidationcallback.md)
  Callback invoked when a CFMachPort object is invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachportcallback)*