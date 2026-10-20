# isFinished

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the operation has finished executing its task.

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
var isFinished: Bool { get }
```

```objc
@property (readonly, getter=isFinished) BOOL finished;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the operation has finished its main task or [`false`](../../Swift/false.md) if it is executing that task or has not yet started it.

When implementing a concurrent operation object, you must override the implementation of this property so that you can return the finished state of your operation. In your custom implementation, you must generate KVO notifications for the `isFinished` key path whenever the finished state of your operation object changes. For more information about manually generating KVO notifications, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

You do not need to reimplement this property for nonconcurrent operations.

## See Also

### Getting the Operation Status
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value indicating whether the operation has been cancelled
- [var isExecuting: Bool](./isexecuting.md)
  A Boolean value indicating whether the operation is currently executing.
- [var isConcurrent: Bool](./isconcurrent.md)
  A Boolean value indicating whether the operation executes its task asynchronously.
- [var isAsynchronous: Bool](./isasynchronous.md)
  A Boolean value indicating whether the operation executes its task asynchronously.
- [var isReady: Bool](./isready.md)
  A Boolean value indicating whether the operation can be performed now.
- [var name: String?](./name.md)
  The name of the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/isfinished)*