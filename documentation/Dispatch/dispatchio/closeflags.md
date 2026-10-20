# DispatchIO.CloseFlags

**Framework**: Dispatch  
**Kind**: struct  
**Role**: Structure

Additional flags to use when closing an I/O channel.

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
struct CloseFlags
```

## Topics

### Close Flags
- [static let stop: DispatchIO.CloseFlags](./closeflags/stop.md)
  Stop any in-progress read/write operations when closed.
### Initializing the Type
- [var DISPATCH_IO_STOP: Int32](../dispatch_io_stop.md)
  Stop any in-progress read and write operations when closed.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Closing the File
- [func close(flags: DispatchIO.CloseFlags)](./close%28flags%29.md)
  Closes the channel to new read and write operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchio/closeflags)*