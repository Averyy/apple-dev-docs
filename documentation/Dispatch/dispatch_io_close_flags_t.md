# dispatch_io_close_flags_t

**Framework**: Dispatch  
**Kind**: typealias  
**Role**: Type Alias

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

```c
typedef unsigned long dispatch_io_close_flags_t;
```

## Topics

### Channel Closing Options
- [var DISPATCH_IO_STOP: Int32](./dispatch_io_stop.md)
  Stop any in-progress read and write operations when closed.

## See Also

### Closing the File
- [dispatch_io_close](./dispatch_io_close.md)
  Closes the specified channel to new read and write operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_io_close_flags_t)*