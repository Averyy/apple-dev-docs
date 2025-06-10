# DispatchIO.IntervalFlags

**Framework**: Dispatch  
**Kind**: struct

The desired delivery behavior for interval events.

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
struct IntervalFlags
```

## Topics

### Interval Flags
- [static let strictInterval: DispatchIO.IntervalFlags](dispatchio/intervalflags/strictinterval.md)
  Enqueue handlers for a channel at strict intervals regardless of how much data has been read or written.
- [var DISPATCH_IO_STRICT_INTERVAL: Int32](dispatch_io_strict_interval.md)
  Enqueue handlers for a channel at strict intervals regardless of how much data has been read or written.
### Initializing the Type
- [init(nilLiteral: ())](dispatchio/intervalflags/init(nilliteral:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var fileDescriptor: Int32](dispatchio/filedescriptor.md)
  Returns the file descriptor associated with the specified channel.
- [func setLimit(highWater: Int)](dispatchio/setlimit(highwater:).md)
  Sets the maximum number of bytes to process before enqueueing a handler block.
- [func setLimit(lowWater: Int)](dispatchio/setlimit(lowwater:).md)
  Sets the minimum number of bytes to process before enqueueing a handler block.
- [func setInterval(interval: DispatchTimeInterval, flags: DispatchIO.IntervalFlags)](dispatchio/setinterval(interval:flags:).md)
  Sets the interval, in nanoseconds, at which to invoke the I/O handlers for the channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchio/intervalflags)*