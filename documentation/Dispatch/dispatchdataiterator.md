# DispatchDataIterator

**Framework**: Dispatch  
**Kind**: struct  
**Role**: Structure

A byte-by-byte iterator over the contents of a dispatch data object.

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
struct DispatchDataIterator
```

## Topics

### Iterating Over a Sequence’s Elements
- [func next() -> DispatchData.Element?](./dispatchdataiterator/next%28%29.md)

## Relationships

### Conforms To
- [IteratorProtocol](../Swift/iteratorprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### System Event Monitoring
- [class DispatchSource](./dispatchsource.md)
  An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [Dispatch Source](./dispatch-source.md)
  An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [class DispatchIO](./dispatchio.md)
  An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [struct DispatchData](./dispatchdata.md)
  An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [Dispatch I/O](./dispatch-i-o.md)
  An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [Dispatch Data](./dispatch-data.md)
  An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [protocol DispatchSourceProtocol](./dispatchsourceprotocol.md)
  Defines a common set of properties and methods that are shared with all dispatch source types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdataiterator)*