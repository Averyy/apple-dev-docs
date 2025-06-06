# queryStepCountStarting(from:to:to:withHandler:)

**Framework**: Core Motion  
**Kind**: method

Gathers and returns historical step count data for the specified time period.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func queryStepCountStarting(from start: Date, to end: Date, to queue: OperationQueue, withHandler handler: @escaping CMStepQueryHandler)
```

#### Discussion

This method runs asynchronously, returning immediately and delivering the results to the specified `handler` block. The system stores only the last seven days worth of step data at most. If there are no samples for the specified range of time, a value of 0 is passed to the `handler` block.

## Parameters

- `start`: The start time to use when gathering step count data. This parameter must not be  .
- `end`: The end time to use when gathering step count data. This parameter must not be  .
- `queue`: The operation queue on which to execute the specified   block. You can specify a custom queue or use the operation queue associated with your app’s main thread. This parameter must not be  .
- `handler`: The block to execute with the results. For information about the parameters of this block, see  . This parameter must not be  .

## See Also

- [typealias CMStepQueryHandler](cmstepqueryhandler.md)
  A block that reports the number of steps for a query operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmstepcounter/querystepcountstarting(from:to:to:withhandler:))*