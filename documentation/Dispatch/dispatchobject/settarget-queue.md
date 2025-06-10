# setTarget(queue:)

**Framework**: Dispatch  
**Kind**: method

Specifies the dispatch queue on which to perform work associated with the current object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setTarget(queue: dispatch_queue_t?)
```

#### Discussion

The target queue determines the queue on which the object’s finalizer is invoked. In addition, assigning a target queue affects how you deal with some dispatch objects, as described in the following table.

| Dispatch object | Implications of assigning a target queue |
| --- | --- |
| Dispatch queues | Redirects all blocks from the current dispatch queue to the specified target queue. Use target queues to redirect work from several different queues onto a single queue. You might do this to minimize the total number of threads your app uses, while still preserving the execution semantics you need. The system doesn’t allocate threads to the dispatch queue if it has a target queue, unless that target queue is a global concurrent queue. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The target queue defines where blocks run, but it doesn’t change the semantics of the current queue. Blocks submitted to a serial queue still execute serially, even if the underlying target queue is concurrent. In addition, you can’t create concurrency where none exists. If a queue and its target queue are both serial, submitting blocks to both queues doesn’t cause those blocks to run concurrently. The blocks still run serially in the order the target queue receives them. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) A dispatch queue inherits the minimum quality-of-service level from its target queue. |
| Dispatch sources | Submits event handler and cancellation handler blocks to the specified target queue. |
| Dispatch I/O channels | Executes I/O operations on the specified target queue. The quality of service of the target queue affects the priority of the resulting I/O operations. For example, if the target queue’s quality of service is [`DispatchQoS.QoSClass.background`](dispatchqos/qosclass-swift.enum/background.md), then I/O operations performed by [`read(offset:length:queue:ioHandler:)`](dispatchio/read(offset:length:queue:iohandler:).md) or [`write(offset:data:queue:ioHandler:)`](dispatchio/write(offset:data:queue:iohandler:).md) on that queue are throttled when there is I/O contention. |

> ❗ **Important**:  When setting up target queues, it is a programmer error to create cycles in the dispatch queue hierarchy. In other words, don’t set the target of queue A to queue B and the target of queue B to queue A.

## Parameters

- `queue`: The new target queue for the object. The new queue is retained, and the previous target queue (if any) is released. Specify   if you want the system to provide a queue that is appropriate for the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchobject/settarget(queue:))*