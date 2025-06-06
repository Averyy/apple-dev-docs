# isReady

**Framework**: Foundation  
**Kind**: property

A Boolean value indicating whether the operation can be performed now.

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
var isReady: Bool { get }
```

#### Discussion

The readiness of operations is determined by their dependencies on other operations and potentially by custom conditions that you define. The `NSOperation` class manages dependencies on other operations and reports the readiness of the receiver based on those dependencies.

If you want to use custom conditions to define the readiness of your operation object, reimplement this property and return a value that accurately reflects the readiness of the receiver. If you do so, your custom implementation must get the default property value from `super` and incorporate that readiness value into the new value of the property. In your custom implementation, you must generate KVO notifications for the `isReady` key path whenever the ready state of your operation object changes. For more information about generating KVO notifications, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

- [var dependencies: [Operation]](operation/dependencies.md)
  An array of the operation objects that must finish executing before the current object can begin executing.
- [var isCancelled: Bool](operation/iscancelled.md)
  A Boolean value indicating whether the operation has been cancelled
- [var isExecuting: Bool](operation/isexecuting.md)
  A Boolean value indicating whether the operation is currently executing.
- [var isFinished: Bool](operation/isfinished.md)
  A Boolean value indicating whether the operation has finished executing its task.
- [var isConcurrent: Bool](operation/isconcurrent.md)
  A Boolean value indicating whether the operation executes its task asynchronously.
- [var isAsynchronous: Bool](operation/isasynchronous.md)
  A Boolean value indicating whether the operation executes its task asynchronously.
- [var name: String?](operation/name.md)
  The name of the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/isready)*