# addOperation(_:)

**Framework**: Foundation  
**Kind**: method

Adds the specified operation to the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addOperation(_ op: Operation)
```

#### Discussion

Once added, the specified operation remains in the queue until it finishes executing.

> ❗ **Important**:  An operation object can be in at most one operation queue at a time and this method throws an [`invalidArgumentException`](nsexceptionname/invalidargumentexception.md) exception if the operation is already in another queue. Similarly, this method throws an [`invalidArgumentException`](nsexceptionname/invalidargumentexception.md) exception if the operation is currently executing or has already finished executing.

 An operation object can be in at most one operation queue at a time and this method throws an [`invalidArgumentException`](nsexceptionname/invalidargumentexception.md) exception if the operation is already in another queue. Similarly, this method throws an [`invalidArgumentException`](nsexceptionname/invalidargumentexception.md) exception if the operation is currently executing or has already finished executing.

## Parameters

- `op`: The operation to be added to the queue.

## See Also

- [func cancel()](operation/cancel.md)
  Advises the operation object that it should stop executing its task.
- [var isExecuting: Bool](operation/isexecuting.md)
  A Boolean value indicating whether the operation is currently executing.
- [func addOperations([Operation], waitUntilFinished: Bool)](operationqueue/addoperations(_:waituntilfinished:).md)
  Adds the specified operations to the queue.
- [func addOperation(() -> Void)](operationqueue/addoperation(_:)-5s294.md)
  Wraps the specified block in an operation and adds it to the receiver.
- [func addBarrierBlock(() -> Void)](operationqueue/addbarrierblock(_:).md)
  Invokes a block when the queue finishes all enqueued operations, and prevents subsequent operations from starting until the block has completed.
- [func cancelAllOperations()](operationqueue/cancelalloperations.md)
  Cancels all queued and executing operations.
- [func waitUntilAllOperationsAreFinished()](operationqueue/waituntilalloperationsarefinished.md)
  Blocks the current thread until all the receiver’s queued and executing operations finish executing.
- [var operations: [Operation]](operationqueue/operations.md)
  The operations currently in the queue.
- [var operationCount: Int](operationqueue/operationcount.md)
  The number of operations currently in the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/addoperation(_:)-64o8a)*