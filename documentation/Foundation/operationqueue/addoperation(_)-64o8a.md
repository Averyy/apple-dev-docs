# addOperation(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addOperation:(NSOperation *) op;
```

## Discussion

Once added, the specified operation remains in the queue until it finishes executing.

> ❗ **Important**:  An operation object can be in at most one operation queue at a time and this method throws an [`invalidArgumentException`](../nsexceptionname/invalidargumentexception.md) exception if the operation is already in another queue. Similarly, this method throws an [`invalidArgumentException`](../nsexceptionname/invalidargumentexception.md) exception if the operation is currently executing or has already finished executing.

## Parameters

- `op`: The operation to be added to the queue.

## See Also

### Related Documentation
- [func cancel()](../operation/cancel%28%29.md)
  Advises the operation object that it should stop executing its task.
- [var isExecuting: Bool](../operation/isexecuting.md)
  A Boolean value indicating whether the operation is currently executing.
### Managing Operations in the Queue
- [func addOperations([Operation], waitUntilFinished: Bool)](./addoperations%28_,waituntilfinished%29.md)
  Adds the specified operations to the queue.
- [func addOperation(() -> Void)](./addoperation%28_%29-5s294.md)
  Wraps the specified block in an operation and adds it to the receiver.
- [func addBarrierBlock(() -> Void)](./addbarrierblock%28_%29.md)
  Invokes a block when the queue finishes all enqueued operations, and prevents subsequent operations from starting until the block has completed.
- [func cancelAllOperations()](./cancelalloperations%28%29.md)
  Cancels all queued and executing operations.
- [func waitUntilAllOperationsAreFinished()](./waituntilalloperationsarefinished%28%29.md)
  Blocks the current thread until all the receiver’s queued and executing operations finish executing.
- [var operations: [Operation]](./operations.md)
  The operations currently in the queue.
- [var operationCount: Int](./operationcount.md)
  The number of operations currently in the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/addoperation(_:)-64o8a)*