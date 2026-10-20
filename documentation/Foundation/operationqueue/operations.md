# operations

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The operations currently in the queue.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.5+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: To avoid race conditions while accessing operations, use [`addBarrierBlock(_:)`](./addbarrierblock%28_%29.md) instead.

## Declaration

```swift
var operations: [Operation] { get }
```

```objc
@property (copy, readonly) NSArray<__kindof NSOperation *> * operations;
```

#### Discussion

The array in this property contains zero or more [`Operation`](../operation.md) objects in the order you added them to the queue. This order doesn’t necessarily reflect the order in which the queue invokes those operations.

You can use this property to access the operations queued at any given moment. Operations remain queued until they finish their task. Therefore, the array may contain operations that are currently running or waiting to run. The list may also contain operations that were running when you retrieved the array but have subsequently finished.

You can monitor changes to the value of this property using [Key-value observing](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16) (KVO). Configure an observer to monitor the [`operations`](./operations.md) key path of the operation queue.

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
- [func waitUntilAllOperationsAreFinished()](./waituntilalloperationsarefinished%28%29.md)
  Blocks the current thread until all the receiver’s queued and executing operations finish executing.
- [var operationCount: Int](./operationcount.md)
  The number of operations currently in the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/operations)*