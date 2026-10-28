# advanced(by:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

## Return Value

An operation queue scheduler time advanced by the given interval from [`date`](./date.md).

## Parameters

- `n`: The time interval to advance [`date`](./date.md) by.

## See Also

### Managing Scheduler Time Type Properties
- [var date: Date](./date.md)
  The date this type represents.
- [func distance(to: OperationQueue.SchedulerTimeType) -> OperationQueue.SchedulerTimeType.Stride](./distance%28to%29.md)
  The distance to another operation queue scheduler time.
- [OperationQueue.SchedulerTimeType.Stride](./stride.md)
  The interval by which operation queue times advance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/schedulertimetype/advanced(by:))*