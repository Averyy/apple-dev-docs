# isCancelled

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isCancelled) BOOL cancelled;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md). Calling the [`cancel()`](./cancel%28%29.md) method of this object sets the value of this property to [`true`](../../Swift/true.md). Once canceled, an operation must move to the finished state.

Canceling an operation does not actively stop the receiver’s code from executing. An operation object is responsible for calling this method periodically and stopping itself if the method returns [`true`](../../Swift/true.md).

You should always check the value of this property before doing any work towards accomplishing the operation’s task, which typically means checking it at the beginning of your custom [`main()`](./main%28%29.md) method. It is possible for an operation to be cancelled before it begins executing or at any time while it is executing. Therefore, checking the value at the beginning of your [`main()`](./main%28%29.md) method (and periodically throughout that method) lets you exit as quickly as possible when an operation is cancelled.

## See Also

### Related Documentation
- [func cancel()](./cancel%28%29.md)
  Advises the operation object that it should stop executing its task.
### Getting the Operation Status
- [var isExecuting: Bool](./isexecuting.md)
  A Boolean value indicating whether the operation is currently executing.
- [var isFinished: Bool](./isfinished.md)
  A Boolean value indicating whether the operation has finished executing its task.
- [var isConcurrent: Bool](./isconcurrent.md)
  A Boolean value indicating whether the operation executes its task asynchronously.
- [var isAsynchronous: Bool](./isasynchronous.md)
  A Boolean value indicating whether the operation executes its task asynchronously.
- [var isReady: Bool](./isready.md)
  A Boolean value indicating whether the operation can be performed now.
- [var name: String?](./name.md)
  The name of the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/iscancelled)*