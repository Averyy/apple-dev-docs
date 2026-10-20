# setLimit(highWater:)

**Framework**: Dispatch  
**Kind**: method  
**Role**: Instance Method

Sets the maximum number of bytes to process before enqueueing a handler block.

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
func setLimit(highWater high_water: Int)
```

```c
extern void dispatch_io_set_high_water(dispatch_io_t channel, size_t high_water);
```

#### Discussion

During a read or write operation, the channel uses the high- and low-water mark values to determine how often to enqueue the associated handler block. It enqueues the block when the number of bytes read or written is between these two values.

The default high-water mark for channels is set to `SIZE_MAX`.

## Parameters

- `high_water`: The maximum number of bytes to read or write before enqueueing the corresponding I/O handler block.

## See Also

### Managing the File Descriptor
- [var fileDescriptor: Int32](./filedescriptor.md)
  Returns the file descriptor associated with the specified channel.
- [func setLimit(lowWater: Int)](./setlimit%28lowwater%29.md)
  Sets the minimum number of bytes to process before enqueueing a handler block.
- [func setInterval(interval: DispatchTimeInterval, flags: DispatchIO.IntervalFlags)](./setinterval%28interval,flags%29.md)
  Sets the interval, in nanoseconds, at which to invoke the I/O handlers for the channel.
- [DispatchIO.IntervalFlags](./intervalflags.md)
  The desired delivery behavior for interval events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchio/setlimit(highwater:))*