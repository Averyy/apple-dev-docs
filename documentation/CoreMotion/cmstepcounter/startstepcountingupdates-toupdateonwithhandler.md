# startStepCountingUpdates(to:updateOn:withHandler:)

**Framework**: Core Motion  
**Kind**: method

Starts the delivery of current step-counting data to your app.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func startStepCountingUpdates(to queue: OperationQueue, updateOn stepCounts: Int, withHandler handler: @escaping CMStepUpdateHandler)
```

#### Discussion

This method initiates tracking of the user’s steps and calls the provided block periodically to deliver the results. When you call this method, the step counter resets the current step count value to 0 and begins counting. Each time the step counter records the number of steps in the `stepCounts` parameter, it executes the specified `handler` block. For example, if `stepCounts` is 100, it would send updates at 100 steps, 200 steps, 300 steps, and so on. The number of steps reported to your handler is always the total number of steps since you called this method.

The `handler` block is executed on a best effort basis each time the step count threshold is exceeded. If your app is suspended when the threshold is exceeded, the block is not executed. When your app resumes, the block is not executed until the threshold is exceeded again.

To stop the delivery of step-counting updates, call the [`stopStepCountingUpdates()`](cmstepcounter/stopstepcountingupdates().md) method. Updates also stop when the step counter object itself is deallocated.

## Parameters

- `queue`: The operation queue on which to execute the specified   block. You can specify a custom queue or use the operation queue associated with your app’s main thread. This parameter must not be  .
- `stepCounts`: The number of steps to record before executing the   block. The number of steps must be greater than 0.
- `handler`: The block to execute when the number of steps has been reached or exceeded. For information about the parameters of this block, see  . This property must not be  .

## See Also

- [func stopStepCountingUpdates()](cmstepcounter/stopstepcountingupdates.md)
  Stops the delivery of step-counting updates to your app.
- [typealias CMStepUpdateHandler](cmstepupdatehandler.md)
  A block that reports the number of steps recorded since updates began.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmstepcounter/startstepcountingupdates(to:updateon:withhandler:))*