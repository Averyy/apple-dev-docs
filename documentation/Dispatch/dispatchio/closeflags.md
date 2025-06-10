# DispatchIO.CloseFlags

**Framework**: Dispatch  
**Kind**: struct

Additional flags to use when closing an I/O channel.

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
struct CloseFlags
```

## Topics

### Close Flags
- [static let stop: DispatchIO.CloseFlags](dispatchio/closeflags/stop.md)
  Stop any in-progress read/write operations when closed.
### Initializing the Type
- [var DISPATCH_IO_STOP: Int32](dispatch_io_stop.md)
  Stop any in-progress read and write operations when closed.

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

- [func close(flags: DispatchIO.CloseFlags)](dispatchio/close(flags:).md)
  Closes the channel to new read and write operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchio/closeflags)*