# start()

**Framework**: Foundation  
**Kind**: method

Begins the execution of the operation.

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
func start()
```

#### Discussion

The default implementation of this method updates the execution state of the operation and calls the receiver’s [`main()`](operation/main().md) method. This method also performs several checks to ensure that the operation can actually run. For example, if the receiver was cancelled or is already finished, this method simply returns without calling [`main()`](operation/main().md). (In OS X v10.5, this method throws an exception if the operation is already finished.) If the operation is currently executing or is not ready to execute, this method throws an `NSInvalidArgumentException` exception. In OS X v10.5, this method catches and ignores any exceptions thrown by your [`main()`](operation/main().md) method automatically. In macOS 10.6 and later, exceptions are allowed to propagate beyond this method. You should never allow exceptions to propagate out of your [`main()`](operation/main().md) method.

> **Note**:  An operation is not considered ready to execute if it is still dependent on other operations that have not yet finished.

If you are implementing a concurrent operation, you must override this method and use it to initiate your operation. Your custom implementation must not call `super` at any time. In addition to configuring the execution environment for your task, your implementation of this method must also track the state of the operation and provide appropriate state transitions. When the operation executes and subsequently finishes its work, it should generate KVO notifications for the `isExecuting` and `isFinished` key paths respectively. For more information about manually generating KVO notifications, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

You can call this method explicitly if you want to execute your operations manually. However, it is a programmer error to call this method on an operation object that is already in an operation queue or to queue the operation after calling this method. Once you add an operation object to a queue, the queue assumes all responsibility for it.

## See Also

- [var isReady: Bool](operation/isready.md)
  A Boolean value indicating whether the operation can be performed now.
- [var dependencies: [Operation]](operation/dependencies.md)
  An array of the operation objects that must finish executing before the current object can begin executing.
- [func main()](operation/main.md)
  Performs the receiver’s non-concurrent task.
- [var completionBlock: (() -> Void)?](operation/completionblock.md)
  The block to execute after the operation’s main task is completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/start())*