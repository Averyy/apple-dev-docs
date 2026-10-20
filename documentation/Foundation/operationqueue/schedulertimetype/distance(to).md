# distance(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

The distance to another operation queue scheduler time.

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
func distance(to other: OperationQueue.SchedulerTimeType) -> OperationQueue.SchedulerTimeType.Stride
```

#### Return Value

The time interval between this time and the other time.

## Parameters

- `other`: Another operation queue scheduler time.

## See Also

### Managing Scheduler Time Type Properties
- [var date: Date](./date.md)
  The date this type represents.
- [func advanced(by: OperationQueue.SchedulerTimeType.Stride) -> OperationQueue.SchedulerTimeType](./advanced%28by%29.md)
  Calculates an operation queue scheduler time by advancing the scheduler time type’s date by the given interval.
- [OperationQueue.SchedulerTimeType.Stride](./stride.md)
  The interval by which operation queue times advance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/schedulertimetype/distance(to:))*