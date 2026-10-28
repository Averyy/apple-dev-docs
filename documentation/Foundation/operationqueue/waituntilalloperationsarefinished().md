# waitUntilAllOperationsAreFinished()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Blocks the current thread until all the receiver’s queued and executing operations finish executing.

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
func waitUntilAllOperationsAreFinished()
```

```objc
- (void) waitUntilAllOperationsAreFinished;
```

## Discussion

When called, this method blocks the current thread and waits for the receiver’s current and queued operations to finish executing. While the current thread is blocked, the receiver continues to launch already queued operations and monitor those that are executing. During this time, the current thread cannot add operations to the queue, but other threads may. Once all of the pending operations are finished, this method returns.

If there are no operations in the queue, this method returns immediately.

## See Also

### Managing Operations in the Queue
- [func addOperation(Operation)](./addoperation%28_%29-64o8a.md)
  Adds the specified operation to the receiver.
- [func addOperations([Operation], waitUntilFinished: Bool)](./addoperations%28_,waituntilfinished%29.md)
  Adds the specified operations to the queue.
- [func addOperation(() -> Void)](./addoperation%28_%29-5s294.md)
  Wraps the specified block in an operation and adds it to the receiver.
- [func addBarrierBlock(() -> Void)](./addbarrierblock%28_%29.md)
  Invokes a block when the queue finishes all enqueued operations, and prevents subsequent operations from starting until the block has completed.
- [func cancelAllOperations()](./cancelalloperations%28%29.md)
  Cancels all queued and executing operations.
- [var operations: [Operation]](./operations.md)
  The operations currently in the queue.
- [var operationCount: Int](./operationcount.md)
  The number of operations currently in the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/waituntilalloperationsarefinished())*