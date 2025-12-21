# isCancelled

**Framework**: Foundation  
**Kind**: property

A Boolean value indicating whether the operation has been cancelled

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
var isCancelled: Bool { get }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false). Calling the [`cancel()`](operation/cancel().md) method of this object sets the value of this property to [`true`](https://developer.apple.com/documentation/Swift/true). Once canceled, an operation must move to the finished state.

Canceling an operation does not actively stop the receiver’s code from executing. An operation object is responsible for calling this method periodically and stopping itself if the method returns [`true`](https://developer.apple.com/documentation/Swift/true).

You should always check the value of this property before doing any work towards accomplishing the operation’s task, which typically means checking it at the beginning of your custom [`main()`](operation/main().md) method. It is possible for an operation to be cancelled before it begins executing or at any time while it is executing. Therefore, checking the value at the beginning of your [`main()`](operation/main().md) method (and periodically throughout that method) lets you exit as quickly as possible when an operation is cancelled.

## See Also

- [func cancel()](operation/cancel.md)
  Advises the operation object that it should stop executing its task.
- [var isExecuting: Bool](operation/isexecuting.md)
  A Boolean value indicating whether the operation is currently executing.
- [var isFinished: Bool](operation/isfinished.md)
  A Boolean value indicating whether the operation has finished executing its task.
- [var isConcurrent: Bool](operation/isconcurrent.md)
  A Boolean value indicating whether the operation executes its task asynchronously.
- [var isAsynchronous: Bool](operation/isasynchronous.md)
  A Boolean value indicating whether the operation executes its task asynchronously.
- [var isReady: Bool](operation/isready.md)
  A Boolean value indicating whether the operation can be performed now.
- [var name: String?](operation/name.md)
  The name of the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/iscancelled)*