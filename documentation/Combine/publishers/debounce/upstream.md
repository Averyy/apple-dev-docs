# upstream

**Framework**: Combine  
**Kind**: property  
**Role**: Instance Property

The publisher from which this publisher receives elements.

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
let upstream: Upstream
```

## See Also

### Inspecting publisher properties
- [let dueTime: Context.SchedulerTimeType.Stride](./duetime.md)
  The amount of time the publisher should wait before publishing an element.
- [let scheduler: Context](./scheduler.md)
  The scheduler on which this publisher delivers elements.
- [let options: Context.SchedulerOptions?](./options.md)
  Scheduler options that customize this publisher’s delivery of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/debounce/upstream)*