# isConcurrent

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isConcurrent) BOOL concurrent;
```

#### Discussion

Use the [`isAsynchronous`](./isasynchronous.md) property instead.

The value of this property is [`true`](../../Swift/true.md) for operations that run asynchronously with respect to the current thread or [`false`](../../Swift/false.md) for operations that run synchronously on the current thread. The default value of this property is [`false`](../../Swift/false.md).

In macOS 10.6 and later, operation queues ignore the value in this property and always start operations on a separate thread.

## See Also

### Getting the Operation Status
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value indicating whether the operation has been cancelled
- [var isExecuting: Bool](./isexecuting.md)
  A Boolean value indicating whether the operation is currently executing.
- [var isFinished: Bool](./isfinished.md)
  A Boolean value indicating whether the operation has finished executing its task.
- [var isAsynchronous: Bool](./isasynchronous.md)
  A Boolean value indicating whether the operation executes its task asynchronously.
- [var isReady: Bool](./isready.md)
  A Boolean value indicating whether the operation can be performed now.
- [var name: String?](./name.md)
  The name of the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/isconcurrent)*