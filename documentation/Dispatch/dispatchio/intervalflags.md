# DispatchIO.IntervalFlags

**Framework**: Dispatch  
**Kind**: struct  
**Role**: Structure

The desired delivery behavior for interval events.

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
struct IntervalFlags
```

## Topics

### Interval Flags
- [static let strictInterval: DispatchIO.IntervalFlags](./intervalflags/strictinterval.md)
  Enqueue handlers for a channel at strict intervals regardless of how much data has been read or written.
- [var DISPATCH_IO_STRICT_INTERVAL: Int32](../dispatch_io_strict_interval.md)
  Enqueue handlers for a channel at strict intervals regardless of how much data has been read or written.
### Initializing the Type
- [init(nilLiteral: ())](./intervalflags/init%28nilliteral%29.md)

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

### Managing the File Descriptor
- [var fileDescriptor: Int32](./filedescriptor.md)
  Returns the file descriptor associated with the specified channel.
- [func setLimit(highWater: Int)](./setlimit%28highwater%29.md)
  Sets the maximum number of bytes to process before enqueueing a handler block.
- [func setLimit(lowWater: Int)](./setlimit%28lowwater%29.md)
  Sets the minimum number of bytes to process before enqueueing a handler block.
- [func setInterval(interval: DispatchTimeInterval, flags: DispatchIO.IntervalFlags)](./setinterval%28interval,flags%29.md)
  Sets the interval, in nanoseconds, at which to invoke the I/O handlers for the channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchio/intervalflags)*