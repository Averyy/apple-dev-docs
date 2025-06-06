# completionBlock

**Framework**: Foundation  
**Kind**: property

The block to execute after the operation’s main task is completed.

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
var completionBlock: (() -> Void)? { get set }
```

#### Discussion

The completion block takes no parameters and has no return value.

The exact execution context for your completion block is not guaranteed but is typically a secondary thread. Therefore, you should not use this block to do any work that requires a very specific execution context. Instead, you should shunt that work to your application’s main thread or to the specific thread that is capable of doing it. For example, if you have a custom thread for coordinating the completion of the operation, you could use the completion block to ping that thread.

The completion block you provide is executed when the value in the [`isFinished`](operation/isfinished.md) property changes to [`true`](https://developer.apple.com/documentation/swift/true). Because the completion block executes after the operation indicates it has finished its task, you must not use a completion block to queue additional work considered to be part of that task. An operation object whose [`isFinished`](operation/isfinished.md) property contains the value [`true`](https://developer.apple.com/documentation/swift/true) must be done with all of its task-related work by definition. The completion block should be used to notify interested objects that the work is complete or perform other tasks that might be related to, but not part of, the operation’s actual task.

A finished operation may finish either because it was cancelled or because it successfully completed its task. You should take that fact into account when writing your block code. Similarly, you should not make any assumptions about the successful completion of dependent operations, which may themselves have been cancelled.

In iOS 8 and later and macOS 10.10 and later, this property is set to `nil` after the completion block begins executing.

## See Also

- [func start()](operation/start.md)
  Begins the execution of the operation.
- [func main()](operation/main.md)
  Performs the receiver’s non-concurrent task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/completionblock)*