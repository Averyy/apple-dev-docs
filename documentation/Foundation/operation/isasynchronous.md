# isAsynchronous

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isAsynchronous) BOOL asynchronous;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) for operations that run asynchronously with respect to the current thread or [`false`](../../Swift/false.md) for operations that run synchronously on the current thread. The default value of this property is [`false`](../../Swift/false.md).

When implementing an asynchronous operation object, you must implement this property and return [`true`](../../Swift/true.md). For more information about how to implement an asynchronous operation, see [Asynchronous Versus Synchronous Operations](../operation.md#Asynchronous-Versus-Synchronous-Operations).

## See Also

### Getting the Operation Status
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value indicating whether the operation has been cancelled
- [var isExecuting: Bool](./isexecuting.md)
  A Boolean value indicating whether the operation is currently executing.
- [var isFinished: Bool](./isfinished.md)
  A Boolean value indicating whether the operation has finished executing its task.
- [var isConcurrent: Bool](./isconcurrent.md)
  A Boolean value indicating whether the operation executes its task asynchronously.
- [var isReady: Bool](./isready.md)
  A Boolean value indicating whether the operation can be performed now.
- [var name: String?](./name.md)
  The name of the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/isasynchronous)*