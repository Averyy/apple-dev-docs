# global(qos:)

**Framework**: Dispatch  
**Kind**: method  
**Role**: Type Method

Returns the global system queue with the specified quality-of-service class.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class func global(qos: DispatchQoS.QoSClass = .default) -> DispatchQueue
```

## Discussion

This method returns a queue suitable for executing tasks with the specified quality-of-service level. Calls to the [`suspend()`](../dispatchobject/suspend%28%29.md), [`resume()`](../dispatchobject/resume%28%29.md), and [`dispatch_set_context`](../dispatch_set_context.md) functions have no effect on the returned queues.

Tasks submitted to the returned queue are scheduled concurrently with respect to one another.

## Parameters

- `qos`: The quality-of-service level to associate with the queue. This value determines the priority at which the system schedules tasks for execution. For a list of possible values, see [`DispatchQoS.QoSClass`](../dispatchqos/qosclass-swift.enum.md).

## See Also

### Creating a Dispatch Queue
- [class var main: DispatchQueue](./main.md)
  The dispatch queue associated with the main thread of the current process.
- [convenience init(label: String, qos: DispatchQoS, attributes: DispatchQueue.Attributes, autoreleaseFrequency: DispatchQueue.AutoreleaseFrequency, target: DispatchQueue?)](./init%28label,qos,attributes,autoreleasefrequency,target%29.md)
  Creates a new dispatch queue to which you can submit blocks.
- [DispatchQoS.QoSClass](../dispatchqos/qosclass-swift.enum.md)
  Quality-of-service classes that specify the priorities for executing tasks.
- [DispatchQueue.Attributes](./attributes.md)
  Attributes that define the behavior of a dispatch queue.
- [DispatchQueue.AutoreleaseFrequency](./autoreleasefrequency.md)
  Constants indicating the frequency with which a dispatch queue autoreleases objects.
- [class OS_dispatch_queue_main](../os_dispatch_queue_main-swift.class.md)
  A system-provided dispatch queue that schedules tasks for serial execution on the app’s main thread.
- [class OS_dispatch_queue_global](../os_dispatch_queue_global-swift.class.md)
  A system-provided dispatch queue that schedules tasks for concurrent execution.
- [class DispatchSerialQueue](../dispatchserialqueue.md)
  A custom dispatch queue that schedules tasks for serial execution on an arbitrary thread.
- [class DispatchConcurrentQueue](../dispatchconcurrentqueue.md)
  A custom dispatch queue that schedules tasks for concurrent execution.
- [typealias dispatch_queue_main_t](../dispatch_queue_main_t.md)
  A dispatch queue that is bound to the app’s main thread and executes tasks serially on that thread.
- [typealias dispatch_queue_global_t](../dispatch_queue_global_t.md)
  A dispatch queue that executes tasks concurrently using threads from the global thread pool.
- [typealias dispatch_queue_serial_t](../dispatch_queue_serial_t.md)
  A dispatch queue that executes tasks serially in first-in, first-out (FIFO) order.
- [typealias dispatch_queue_concurrent_t](../dispatch_queue_concurrent_t.md)
  A dispatch queue that executes tasks concurrently and in any order, respecting any barriers that may be in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/global(qos:))*