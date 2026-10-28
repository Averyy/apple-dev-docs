# addOperations(_:waitUntilFinished:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds the specified operations to the queue.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addOperations(_ ops: [Operation], waitUntilFinished wait: Bool)
```

```objc
- (void) addOperations:(NSArray<NSOperation *> *) ops waitUntilFinished:(BOOL) wait;
```

## Discussion

An operation object can be in at most one operation queue at a time and cannot be added if it is currently executing or finished. This method throws an `NSInvalidArgumentException` exception if any of those error conditions are true for any of the operations in the `ops` parameter.

Once added, the specified `operation` remains in the queue until its [`isFinished`](../operation/isfinished.md) method returns [`true`](../../Swift/true.md).

## Parameters

- `ops`: The operations to be added to the queue.
- `wait`: If [`true`](../../Swift/true.md), the current thread is blocked until all of the specified operations finish executing. If [`false`](../../Swift/false.md), the operations are added to the queue and control returns immediately to the caller.

## See Also

### Managing Operations in the Queue
- [func addOperation(Operation)](./addoperation%28_%29-64o8a.md)
  Adds the specified operation to the receiver.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/addoperations(_:waituntilfinished:))*