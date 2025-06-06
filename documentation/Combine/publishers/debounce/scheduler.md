# scheduler

**Framework**: Combine  
**Kind**: property

The scheduler on which this publisher delivers elements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let scheduler: Context
```

## See Also

- [let upstream: Upstream](publishers/debounce/upstream.md)
  The publisher from which this publisher receives elements.
- [let dueTime: Context.SchedulerTimeType.Stride](publishers/debounce/duetime.md)
  The amount of time the publisher should wait before publishing an element.
- [let options: Context.SchedulerOptions?](publishers/debounce/options.md)
  Scheduler options that customize this publisher’s delivery of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/debounce/scheduler)*