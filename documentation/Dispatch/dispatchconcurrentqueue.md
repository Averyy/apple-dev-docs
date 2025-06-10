# DispatchConcurrentQueue

**Framework**: Dispatch  
**Kind**: class

A custom dispatch queue that schedules tasks for concurrent execution.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class DispatchConcurrentQueue
```

#### Overview

You do not create objects of this type directly. You receive a queue of the appropriate type when you create a new [`DispatchQueue`](dispatchqueue.md) object.

## Topics

### Structures
- [DispatchConcurrentQueue.Attributes](dispatchconcurrentqueue/attributes.md)
### Initializers
- [convenience init(label: String, qos: DispatchQoS, attributes: DispatchConcurrentQueue.Attributes, autoreleaseFrequency: DispatchQueue.AutoreleaseFrequency, target: DispatchQueue?)](dispatchconcurrentqueue/init(label:qos:attributes:autoreleasefrequency:target:).md)

## Relationships

### Inherits From
- [DispatchQueue](dispatchqueue.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Equatable](../Swift/Equatable.md)
- [Executor](../Swift/Executor.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Scheduler](../Combine/Scheduler.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TaskExecutor](../Swift/TaskExecutor.md)

## See Also

- [class var main: DispatchQueue](dispatchqueue/main.md)
  The dispatch queue associated with the main thread of the current process.
- [class func global(qos: DispatchQoS.QoSClass) -> DispatchQueue](dispatchqueue/global(qos:).md)
  Returns the global system queue with the specified quality-of-service class.
- [convenience init(label: String, qos: DispatchQoS, attributes: DispatchQueue.Attributes, autoreleaseFrequency: DispatchQueue.AutoreleaseFrequency, target: DispatchQueue?)](dispatchqueue/init(label:qos:attributes:autoreleasefrequency:target:).md)
  Creates a new dispatch queue to which you can submit blocks.
- [DispatchQoS.QoSClass](dispatchqos/qosclass-swift.enum.md)
  Quality-of-service classes that specify the priorities for executing tasks.
- [DispatchQueue.Attributes](dispatchqueue/attributes.md)
  Attributes that define the behavior of a dispatch queue.
- [DispatchQueue.AutoreleaseFrequency](dispatchqueue/autoreleasefrequency.md)
  Constants indicating the frequency with which a dispatch queue autoreleases objects.
- [class OS_dispatch_queue_main](os_dispatch_queue_main-swift.class.md)
  A system-provided dispatch queue that schedules tasks for serial execution on the app’s main thread.
- [class OS_dispatch_queue_global](os_dispatch_queue_global-swift.class.md)
  A system-provided dispatch queue that schedules tasks for concurrent execution.
- [class DispatchSerialQueue](dispatchserialqueue.md)
  A custom dispatch queue that schedules tasks for serial execution on an arbitrary thread.
- [typealias dispatch_queue_main_t](dispatch_queue_main_t.md)
  A dispatch queue that is bound to the app’s main thread and executes tasks serially on that thread.
- [typealias dispatch_queue_global_t](dispatch_queue_global_t.md)
  A dispatch queue that executes tasks concurrently using threads from the global thread pool.
- [typealias dispatch_queue_serial_t](dispatch_queue_serial_t.md)
  A dispatch queue that executes tasks serially in first-in, first-out (FIFO) order.
- [typealias dispatch_queue_concurrent_t](dispatch_queue_concurrent_t.md)
  A dispatch queue that executes tasks concurrently and in any order, respecting any barriers that may be in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchconcurrentqueue)*