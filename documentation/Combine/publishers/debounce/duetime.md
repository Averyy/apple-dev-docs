# dueTime

**Framework**: Combine  
**Kind**: property

The amount of time the publisher should wait before publishing an element.

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
let dueTime: Context.SchedulerTimeType.Stride
```

## See Also

- [let upstream: Upstream](publishers/debounce/upstream.md)
  The publisher from which this publisher receives elements.
- [let scheduler: Context](publishers/debounce/scheduler.md)
  The scheduler on which this publisher delivers elements.
- [let options: Context.SchedulerOptions?](publishers/debounce/options.md)
  Scheduler options that customize this publisher’s delivery of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/debounce/duetime)*