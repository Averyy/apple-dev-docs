# advanced(by:)

**Framework**: Foundation  
**Kind**: method

Calculates an operation queue scheduler time by advancing the scheduler time type’s date by the given interval.

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
func advanced(by n: OperationQueue.SchedulerTimeType.Stride) -> OperationQueue.SchedulerTimeType
```

#### Return Value

An operation queue scheduler time advanced by the given interval from [`date`](operationqueue/schedulertimetype/date.md).

## Parameters

- `n`: The time interval to advance   by.

## See Also

- [var date: Date](operationqueue/schedulertimetype/date.md)
  The date this type represents.
- [func distance(to: OperationQueue.SchedulerTimeType) -> OperationQueue.SchedulerTimeType.Stride](operationqueue/schedulertimetype/distance(to:).md)
  The distance to another operation queue scheduler time.
- [OperationQueue.SchedulerTimeType.Stride](operationqueue/schedulertimetype/stride.md)
  The interval by which operation queue times advance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/schedulertimetype/advanced(by:))*