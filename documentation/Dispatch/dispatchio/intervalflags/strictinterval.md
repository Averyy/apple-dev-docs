# strictInterval

**Framework**: Dispatch  
**Kind**: property

Enqueue handlers for a channel at strict intervals regardless of how much data has been read or written.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static let strictInterval: DispatchIO.IntervalFlags
```

#### Discussion

Setting this flag can lead to the handler being called even if the amount of data does not exceed the channel’s low-water mark.

## See Also

- [var DISPATCH_IO_STRICT_INTERVAL: Int32](dispatch_io_strict_interval.md)
  Enqueue handlers for a channel at strict intervals regardless of how much data has been read or written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchio/intervalflags/strictinterval)*