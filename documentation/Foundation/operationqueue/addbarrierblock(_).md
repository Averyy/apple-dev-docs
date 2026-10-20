# addBarrierBlock(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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
func addBarrierBlock(_ barrier: @escaping @Sendable () -> Void)
```

```objc
- (void) addBarrierBlock:(void (^)()) barrier;
```

#### Discussion

This method is similar to [`dispatch_barrier_async`](../../Dispatch/dispatch_barrier_async.md).

## Parameters

- `barrier`: The block to invoke after all currently enqueued operations have finished. Operations you add after the barrier block don’t start until the block has completed.

## See Also

### Managing Operations in the Queue
- [func addOperation(Operation)](./addoperation%28_%29-64o8a.md)
  Adds the specified operation to the receiver.
- [func addOperations([Operation], waitUntilFinished: Bool)](./addoperations%28_,waituntilfinished%29.md)
  Adds the specified operations to the queue.
- [func addOperation(() -> Void)](./addoperation%28_%29-5s294.md)
  Wraps the specified block in an operation and adds it to the receiver.
- [func cancelAllOperations()](./cancelalloperations%28%29.md)
  Cancels all queued and executing operations.
- [func waitUntilAllOperationsAreFinished()](./waituntilalloperationsarefinished%28%29.md)
  Blocks the current thread until all the receiver’s queued and executing operations finish executing.
- [var operations: [Operation]](./operations.md)
  The operations currently in the queue.
- [var operationCount: Int](./operationcount.md)
  The number of operations currently in the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/addbarrierblock(_:))*