# SchedulerOptions

**Framework**: Combine  
**Kind**: associatedtype  
**Required**: Yes

A type that defines options accepted by the scheduler.

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
associatedtype SchedulerOptions
```

#### Discussion

This type is freely definable by each `Scheduler`. Typically, operations that take a `Scheduler` parameter will also take `SchedulerOptions`.

## See Also

- [associatedtype SchedulerTimeType : Strideable](scheduler/schedulertimetype.md)
  Describes an instant in time for this scheduler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/scheduler/scheduleroptions)*