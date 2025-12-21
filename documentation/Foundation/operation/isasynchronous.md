# isAsynchronous

**Framework**: Foundation  
**Kind**: property

A Boolean value indicating whether the operation executes its task asynchronously.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isAsynchronous: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) for operations that run asynchronously with respect to the current thread or [`false`](https://developer.apple.com/documentation/Swift/false) for operations that run synchronously on the current thread. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

When implementing an asynchronous operation object, you must implement this property and return [`true`](https://developer.apple.com/documentation/Swift/true). For more information about how to implement an asynchronous operation, see [`Asynchronous Versus Synchronous Operations`](operation#Asynchronous-Versus-Synchronous-Operations.md).

## See Also

- [var isCancelled: Bool](operation/iscancelled.md)
  A Boolean value indicating whether the operation has been cancelled
- [var isExecuting: Bool](operation/isexecuting.md)
  A Boolean value indicating whether the operation is currently executing.
- [var isFinished: Bool](operation/isfinished.md)
  A Boolean value indicating whether the operation has finished executing its task.
- [var isConcurrent: Bool](operation/isconcurrent.md)
  A Boolean value indicating whether the operation executes its task asynchronously.
- [var isReady: Bool](operation/isready.md)
  A Boolean value indicating whether the operation can be performed now.
- [var name: String?](operation/name.md)
  The name of the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/isasynchronous)*