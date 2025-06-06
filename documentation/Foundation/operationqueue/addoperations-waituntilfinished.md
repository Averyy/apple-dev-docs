# addOperations(_:waitUntilFinished:)

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

An operation object can be in at most one operation queue at a time and cannot be added if it is currently executing or finished. This method throws an `NSInvalidArgumentException` exception if any of those error conditions are true for any of the operations in the `ops` parameter.

Once added, the specified `operation` remains in the queue until its [`isFinished`](operation/isfinished.md) method returns [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `ops`: The operations to be added to the queue.
- `wait`: If  , the current thread is blocked until all of the specified operations finish executing. If  , the operations are added to the queue and control returns immediately to the caller.

## See Also

- [func addOperation(Operation)](operationqueue/addoperation(_:)-64o8a.md)
  Adds the specified operation to the receiver.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/addoperations(_:waituntilfinished:))*