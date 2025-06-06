# addBarrierBlock(_:)

**Framework**: Foundation  
**Kind**: method

Invokes a block when the queue finishes all enqueued operations, and prevents subsequent operations from starting until the block has completed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func addBarrierBlock(_ barrier: @escaping () -> Void)
```

#### Discussion

This method is similar to [`dispatch_barrier_async`](https://developer.apple.com/documentation/dispatch/1452797-dispatch_barrier_async).

## Parameters

- `barrier`: The block to invoke after all currently enqueued operations have finished. Operations you add after the barrier block don’t start until the block has completed.

## See Also

- [func addOperation(Operation)](operationqueue/addoperation(_:)-64o8a.md)
  Adds the specified operation to the receiver.
- [func addOperations([Operation], waitUntilFinished: Bool)](operationqueue/addoperations(_:waituntilfinished:).md)
  Adds the specified operations to the queue.
- [func addOperation(() -> Void)](operationqueue/addoperation(_:)-5s294.md)
  Wraps the specified block in an operation and adds it to the receiver.
- [func cancelAllOperations()](operationqueue/cancelalloperations.md)
  Cancels all queued and executing operations.
- [func waitUntilAllOperationsAreFinished()](operationqueue/waituntilalloperationsarefinished.md)
  Blocks the current thread until all the receiver’s queued and executing operations finish executing.
- [var operations: [Operation]](operationqueue/operations.md)
  The operations currently in the queue.
- [var operationCount: Int](operationqueue/operationcount.md)
  The number of operations currently in the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/addbarrierblock(_:))*