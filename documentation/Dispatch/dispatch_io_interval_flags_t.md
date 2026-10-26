# dispatch_io_interval_flags_t

**Framework**: Dispatch  
**Kind**: typealias  
**Role**: Type Alias

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

```c
typedef unsigned long dispatch_io_interval_flags_t;
```

## Topics

### Channel Configuration Options
- [var DISPATCH_IO_STRICT_INTERVAL: Int32](./dispatch_io_strict_interval.md)
  Enqueue handlers for a channel at strict intervals regardless of how much data has been read or written.

## See Also

### Managing the File Descriptor
- [var fileDescriptor: Int32](./dispatchio/filedescriptor.md)
  Returns the file descriptor associated with the specified channel.
- [dispatch_io_set_interval](./dispatch_io_set_interval.md)
  Sets the interval (in nanoseconds) at which to invoke the I/O handlers for the channel.
- [func setLimit(lowWater: Int)](./dispatchio/setlimit%28lowwater%29.md)
  Sets the minimum number of bytes to process before enqueueing a handler block.
- [func setLimit(highWater: Int)](./dispatchio/setlimit%28highwater%29.md)
  Sets the maximum number of bytes to process before enqueueing a handler block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_io_interval_flags_t)*