# DispatchQueue.AutoreleaseFrequency

**Framework**: Dispatch  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the frequency with which a dispatch queue autoreleases objects.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum AutoreleaseFrequency
```

## Topics

### Autorelease Frequencies
- [DispatchQueue.AutoreleaseFrequency.inherit](./autoreleasefrequency/inherit.md)
  The queue inherits its autorelease frequency from its target queue.
- [DispatchQueue.AutoreleaseFrequency.workItem](./autoreleasefrequency/workitem.md)
  The queue configures an autorelease pool before the execution of a block, and releases the objects in that pool after the block finishes executing.
- [DispatchQueue.AutoreleaseFrequency.never](./autoreleasefrequency/never.md)
  The queue does not set up an autorelease pool around executed blocks.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a Dispatch Queue
- [class var main: DispatchQueue](./main.md)
  The dispatch queue associated with the main thread of the current process.
- [class func global(qos: DispatchQoS.QoSClass) -> DispatchQueue](./global%28qos%29.md)
  Returns the global system queue with the specified quality-of-service class.
- [convenience init(label: String, qos: DispatchQoS, attributes: DispatchQueue.Attributes, autoreleaseFrequency: DispatchQueue.AutoreleaseFrequency, target: DispatchQueue?)](./init%28label,qos,attributes,autoreleasefrequency,target%29.md)
  Creates a new dispatch queue to which you can submit blocks.
- [DispatchQoS.QoSClass](../dispatchqos/qosclass-swift.enum.md)
  Quality-of-service classes that specify the priorities for executing tasks.
- [DispatchQueue.Attributes](./attributes.md)
  Attributes that define the behavior of a dispatch queue.
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

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/autoreleasefrequency)*