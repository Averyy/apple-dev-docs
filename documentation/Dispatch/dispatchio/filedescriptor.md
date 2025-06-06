# fileDescriptor

**Framework**: Dispatch  
**Kind**: property

Returns the file descriptor associated with the specified channel.

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
var fileDescriptor: Int32 { get }
```

#### Discussion

If the path name associated with the channel has not yet been opened, calling this function does not normally open the corresponding file, with one exception. If you call the function from a barrier block scheduled on the channel, the function does open the file and return the resulting file descriptor.

## See Also

- [func setLimit(highWater: Int)](dispatchio/setlimit(highwater:).md)
  Sets the maximum number of bytes to process before enqueueing a handler block.
- [func setLimit(lowWater: Int)](dispatchio/setlimit(lowwater:).md)
  Sets the minimum number of bytes to process before enqueueing a handler block.
- [func setInterval(interval: DispatchTimeInterval, flags: DispatchIO.IntervalFlags)](dispatchio/setinterval(interval:flags:).md)
  Sets the interval, in nanoseconds, at which to invoke the I/O handlers for the channel.
- [DispatchIO.IntervalFlags](dispatchio/intervalflags.md)
  The desired delivery behavior for interval events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchio/filedescriptor)*