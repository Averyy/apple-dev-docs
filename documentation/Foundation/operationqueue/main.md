# main

**Framework**: Foundation  
**Kind**: property

Returns the operation queue associated with the main thread.

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
class var main: OperationQueue { get }
```

#### Return Value

The default operation queue bound to the main thread.

#### Discussion

The returned queue executes one operation at a time on the app’s main thread. The execution of operations on the main thread is interleaved with the other tasks that must execute on the main thread, such as the servicing of events and the updating of an app’s user interface. The queue executes those operations in the run loop common modes, as represented by the [`common`](runloop/mode/common.md) constant. The value of the [`underlyingQueue`](operationqueue/underlyingqueue.md) property for the queue is the dispatch queue for the main thread; this property cannot be set to another value.

## See Also

- [class var current: OperationQueue?](operationqueue/current.md)
  Returns the operation queue that launched the current operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/main)*