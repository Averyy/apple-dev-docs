# options

**Framework**: Combine  
**Kind**: property

Scheduler options that customize this publisher’s delivery of elements.

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
let options: Context.SchedulerOptions?
```

## See Also

- [let upstream: Upstream](publishers/debounce/upstream.md)
  The publisher from which this publisher receives elements.
- [let dueTime: Context.SchedulerTimeType.Stride](publishers/debounce/duetime.md)
  The amount of time the publisher should wait before publishing an element.
- [let scheduler: Context](publishers/debounce/scheduler.md)
  The scheduler on which this publisher delivers elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/debounce/options)*