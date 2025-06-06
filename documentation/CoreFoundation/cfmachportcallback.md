# CFMachPortCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Callback invoked to process a message received on a CFMachPort object.

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
typealias CFMachPortCallBack = (CFMachPort?, UnsafeMutableRawPointer?, CFIndex, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

You specify this callback when creating a CFMachPort object with either [`CFMachPortCreate(_:_:_:_:)`](cfmachportcreate(_:_:_:_:).md) or [`CFMachPortCreateWithPort(_:_:_:_:_:)`](cfmachportcreatewithport(_:_:_:_:_:).md). To receive messages on a CFMachPort object (and have this callback invoked), you must create a run loop source for the port and add it to a run loop.

## Parameters

- `port`: The CFMachPort object on which the message   was received.
- `msg`: The Mach message received on  . The pointer is to a   structure.
- `size`: Size of the Mach message  , excluding the message trailer.
- `info`: The   member of the   structure used when creating  .

## See Also

- [typealias CFMachPortInvalidationCallBack](cfmachportinvalidationcallback.md)
  Callback invoked when a CFMachPort object is invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachportcallback)*