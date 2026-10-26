# dispatch_io_set_interval

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Sets the interval (in nanoseconds) at which to invoke the I/O handlers for the channel.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void dispatch_io_set_interval(dispatch_io_t channel, uint64_t interval, dispatch_io_interval_flags_t flags);
```

#### Discussion

A channel interval is a way for you to receive periodic progress reports on the state of a read or write operation. You can use this feedback to update progress bars or other parts of your application.

If you set an interval on a channel, the handlers for any read or write operations are enqueued at the given interval only if the amount of data that has been processed exceeds the current low-water mark for the channel. Passing the [`DISPATCH_IO_STRICT_INTERVAL`](./dispatch_io_strict_interval.md) constant in the `flags` parameter forces the enqueueing of the handlers even if the low-water mark is not exceeded.

The system may add a small amount of leeway to the specified interval in order to align the delivery of handlers with other system activity. The purpose of this behavior is to improve overall performance or power consumption for the system.

## Parameters

- `channel`: The channel whose interval you want to configure.
- `interval`: The number of nanoseconds that must elapse before the scheduling of any I/O handlers is desired.
- `flags`: Flags indicating the desired delivery behavior at the interval time. For a list of flags, see [`dispatch_io_interval_flags_t`](./dispatch_io_interval_flags_t.md).

## See Also

### Managing the File Descriptor
- [var fileDescriptor: Int32](./dispatchio/filedescriptor.md)
  Returns the file descriptor associated with the specified channel.
- [dispatch_io_interval_flags_t](./dispatch_io_interval_flags_t.md)
  The desired delivery behavior for interval events.
- [func setLimit(lowWater: Int)](./dispatchio/setlimit%28lowwater%29.md)
  Sets the minimum number of bytes to process before enqueueing a handler block.
- [func setLimit(highWater: Int)](./dispatchio/setlimit%28highwater%29.md)
  Sets the maximum number of bytes to process before enqueueing a handler block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_io_set_interval)*