# isExecuting

**Framework**: Foundation  
**Kind**: property

A Boolean value indicating whether the operation is currently executing.

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
var isExecuting: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the operation is currently executing its main task or [`false`](https://developer.apple.com/documentation/swift/false) if it is not.

When implementing a concurrent operation object, you must override the implementation of this property so that you can return the execution state of your operation. In your custom implementation, you must generate KVO notifications for the `isExecuting` key path whenever the execution state of your operation object changes. For more information about manually generating KVO notifications, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

You do not need to reimplement this property for nonconcurrent operations.

## See Also

- [var isCancelled: Bool](operation/iscancelled.md)
  A Boolean value indicating whether the operation has been cancelled
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/isexecuting)*