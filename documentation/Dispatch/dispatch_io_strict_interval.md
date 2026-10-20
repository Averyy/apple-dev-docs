# DISPATCH_IO_STRICT_INTERVAL

**Framework**: Dispatch  
**Kind**: var  
**Role**: Global Variable

Enqueue handlers for a channel at strict intervals regardless of how much data has been read or written.

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
var DISPATCH_IO_STRICT_INTERVAL: Int32 { get }
```

```c
#define DISPATCH_IO_STRICT_INTERVAL
```

#### Discussion

Setting this flag can lead to the handler being called even if the amount of data does not exceed the channel’s low-water mark.

## See Also

### Interval Flags
- [static let strictInterval: DispatchIO.IntervalFlags](./dispatchio/intervalflags/strictinterval.md)
  Enqueue handlers for a channel at strict intervals regardless of how much data has been read or written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_io_strict_interval)*