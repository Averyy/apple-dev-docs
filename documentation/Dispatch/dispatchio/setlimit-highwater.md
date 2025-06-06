# setLimit(highWater:)

**Framework**: Dispatch  
**Kind**: method

Sets the maximum number of bytes to process before enqueueing a handler block.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setLimit(highWater high_water: Int)
```

#### Discussion

During a read or write operation, the channel uses the high- and low-water mark values to determine how often to enqueue the associated handler block. It enqueues the block when the number of bytes read or written is between these two values.

The default high-water mark for channels is set to `SIZE_MAX`.

## Parameters

- `high_water`: The maximum number of bytes to read or write before enqueueing the corresponding I/O handler block.

## See Also

- [var fileDescriptor: Int32](dispatchio/filedescriptor.md)
  Returns the file descriptor associated with the specified channel.
- [func setLimit(lowWater: Int)](dispatchio/setlimit(lowwater:).md)
  Sets the minimum number of bytes to process before enqueueing a handler block.
- [func setInterval(interval: DispatchTimeInterval, flags: DispatchIO.IntervalFlags)](dispatchio/setinterval(interval:flags:).md)
  Sets the interval, in nanoseconds, at which to invoke the I/O handlers for the channel.
- [DispatchIO.IntervalFlags](dispatchio/intervalflags.md)
  The desired delivery behavior for interval events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchio/setlimit(highwater:))*