# addOperation(_:)

**Framework**: Foundation  
**Kind**: method

Wraps the specified block in an operation and adds it to the receiver.

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
func addOperation(_ block: @escaping () -> Void)
```

#### Discussion

This method adds a single block to the receiver by first wrapping it in an operation object. You should not attempt to get a reference to the newly created operation object or determine its type information.

## Parameters

- `block`: The block to execute from the operation. The block takes no parameters and has no return value.

## See Also

- [func cancel()](operation/cancel.md)
  Advises the operation object that it should stop executing its task.
- [var isExecuting: Bool](operation/isexecuting.md)
  A Boolean value indicating whether the operation is currently executing.
- [func addOperation(Operation)](operationqueue/addoperation(_:)-64o8a.md)
  Adds the specified operation to the receiver.
- [func addOperations([Operation], waitUntilFinished: Bool)](operationqueue/addoperations(_:waituntilfinished:).md)
  Adds the specified operations to the queue.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/addoperation(_:)-5s294)*