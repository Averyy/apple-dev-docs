# DispatchQueue.Attributes

**Framework**: Dispatch  
**Kind**: struct

Attributes that define the behavior of a dispatch queue.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct Attributes
```

## Topics

### Attributes
- [static let concurrent: DispatchQueue.Attributes](dispatchqueue/attributes/concurrent.md)
  The queue schedules tasks concurrently.
- [static let initiallyInactive: DispatchQueue.Attributes](dispatchqueue/attributes/initiallyinactive.md)
  The newly created queue is inactive.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class var main: DispatchQueue](dispatchqueue/main.md)
  The dispatch queue associated with the main thread of the current process.
- [class func global(qos: DispatchQoS.QoSClass) -> DispatchQueue](dispatchqueue/global(qos:).md)
  Returns the global system queue with the specified quality-of-service class.
- [convenience init(label: String, qos: DispatchQoS, attributes: DispatchQueue.Attributes, autoreleaseFrequency: DispatchQueue.AutoreleaseFrequency, target: DispatchQueue?)](dispatchqueue/init(label:qos:attributes:autoreleasefrequency:target:).md)
  Creates a new dispatch queue to which you can submit blocks.
- [DispatchQoS.QoSClass](dispatchqos/qosclass-swift.enum.md)
  Quality-of-service classes that specify the priorities for executing tasks.
- [DispatchQueue.AutoreleaseFrequency](dispatchqueue/autoreleasefrequency.md)
  Constants indicating the frequency with which a dispatch queue autoreleases objects.
- [class OS_dispatch_queue_main](os_dispatch_queue_main-swift.class.md)
  A system-provided dispatch queue that schedules tasks for serial execution on the app’s main thread.
- [class OS_dispatch_queue_global](os_dispatch_queue_global-swift.class.md)
  A system-provided dispatch queue that schedules tasks for concurrent execution.
- [class DispatchSerialQueue](dispatchserialqueue.md)
  A custom dispatch queue that schedules tasks for serial execution on an arbitrary thread.
- [class DispatchConcurrentQueue](dispatchconcurrentqueue.md)
  A custom dispatch queue that schedules tasks for concurrent execution.
- [typealias dispatch_queue_main_t](dispatch_queue_main_t.md)
  A dispatch queue that is bound to the app’s main thread and executes tasks serially on that thread.
- [typealias dispatch_queue_global_t](dispatch_queue_global_t.md)
  A dispatch queue that executes tasks concurrently using threads from the global thread pool.
- [typealias dispatch_queue_serial_t](dispatch_queue_serial_t.md)
  A dispatch queue that executes tasks serially in first-in, first-out (FIFO) order.
- [typealias dispatch_queue_concurrent_t](dispatch_queue_concurrent_t.md)
  A dispatch queue that executes tasks concurrently and in any order, respecting any barriers that may be in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/attributes)*