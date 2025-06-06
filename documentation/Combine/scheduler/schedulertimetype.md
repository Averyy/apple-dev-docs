# SchedulerTimeType

**Framework**: Combine  
**Kind**: associatedtype  
**Required**: Yes

Describes an instant in time for this scheduler.

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
associatedtype SchedulerTimeType : Strideable where Self.SchedulerTimeType.Stride : SchedulerTimeIntervalConvertible
```

## See Also

- [associatedtype SchedulerOptions](scheduler/scheduleroptions.md)
  A type that defines options accepted by the scheduler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/scheduler/schedulertimetype)*