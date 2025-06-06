# perform

**Framework**: Core Foundation  
**Kind**: property

A perform callback for the run loop source. This callback is called when the source has fired.

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
var perform: ((UnsafeMutableRawPointer?, CFIndex, CFAllocator?, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!
```

#### Return Value

An optional Mach message to be sent in response to the received message. The message must be allocated using `allocator`. Return `NULL` if you want an empty reply returned to the sender.

#### Discussion

You only need to provide this callback if you create your own version 1 run loop source. CFMachPort and CFMessagePort run loop sources already implement this callback to forward the received message to the CFMachPort’s or CFMessagePort’s own callback function, which you do need to implement.

## Parameters

- `msg`: The Mach message received on the Mach port. The pointer is to a   structure. A version 0 format trailer ( ) is at the end of the Mach message.
- `size`: Size of the Mach message in  , excluding the message trailer.
- `allocator`: The allocator object that should be used to allocate a reply message.
- `info`: The   member of the   structure that was used when creating the run loop source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/perform)*