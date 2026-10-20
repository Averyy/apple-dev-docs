# dueTime

**Framework**: Combine  
**Kind**: property  
**Role**: Instance Property

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

### Inspecting publisher properties
- [let upstream: Upstream](./upstream.md)
  The publisher from which this publisher receives elements.
- [let scheduler: Context](./scheduler.md)
  The scheduler on which this publisher delivers elements.
- [let options: Context.SchedulerOptions?](./options.md)
  Scheduler options that customize this publisher’s delivery of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/debounce/duetime)*