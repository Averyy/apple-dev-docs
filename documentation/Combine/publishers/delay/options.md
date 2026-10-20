# options

**Framework**: Combine  
**Kind**: property  
**Role**: Instance Property

Options relevant to the scheduler’s behavior.

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

### Inspecting publisher properties
- [let upstream: Upstream](./upstream.md)
  The publisher from which this publisher receives its elements.
- [let interval: Context.SchedulerTimeType.Stride](./interval.md)
  The amount of time to delay.
- [let tolerance: Context.SchedulerTimeType.Stride](./tolerance.md)
  The allowed tolerance in firing delayed events.
- [let scheduler: Context](./scheduler.md)
  The scheduler to deliver the delayed events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/delay/options)*