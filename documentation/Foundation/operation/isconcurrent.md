# isConcurrent

**Framework**: Foundation  
**Kind**: property

A Boolean value indicating whether the operation executes its task asynchronously.

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
var isConcurrent: Bool { get }
```

#### Discussion

Use the [`isAsynchronous`](operation/isasynchronous.md) property instead.

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) for operations that run asynchronously with respect to the current thread or [`false`](https://developer.apple.com/documentation/swift/false) for operations that run synchronously on the current thread. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

In macOS 10.6 and later, operation queues ignore the value in this property and always start operations on a separate thread.

## See Also

- [var isCancelled: Bool](operation/iscancelled.md)
  A Boolean value indicating whether the operation has been cancelled
- [var isExecuting: Bool](operation/isexecuting.md)
  A Boolean value indicating whether the operation is currently executing.
- [var isFinished: Bool](operation/isfinished.md)
  A Boolean value indicating whether the operation has finished executing its task.
- [var isAsynchronous: Bool](operation/isasynchronous.md)
  A Boolean value indicating whether the operation executes its task asynchronously.
- [var isReady: Bool](operation/isready.md)
  A Boolean value indicating whether the operation can be performed now.
- [var name: String?](operation/name.md)
  The name of the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/isconcurrent)*