# fileDescriptor

**Framework**: Dispatch  
**Kind**: property  
**Role**: Instance Property

Returns the file descriptor associated with the specified channel.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var fileDescriptor: Int32 { get }
```

```c
extern dispatch_fd_t dispatch_io_get_descriptor(dispatch_io_t channel);
```

#### Discussion

If the path name associated with the channel has not yet been opened, calling this function does not normally open the corresponding file, with one exception. If you call the function from a barrier block scheduled on the channel, the function does open the file and return the resulting file descriptor.

## See Also

### Managing the File Descriptor
- [func setLimit(highWater: Int)](./setlimit%28highwater%29.md)
  Sets the maximum number of bytes to process before enqueueing a handler block.
- [func setLimit(lowWater: Int)](./setlimit%28lowwater%29.md)
  Sets the minimum number of bytes to process before enqueueing a handler block.
- [func setInterval(interval: DispatchTimeInterval, flags: DispatchIO.IntervalFlags)](./setinterval%28interval,flags%29.md)
  Sets the interval, in nanoseconds, at which to invoke the I/O handlers for the channel.
- [DispatchIO.IntervalFlags](./intervalflags.md)
  The desired delivery behavior for interval events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchio/filedescriptor)*