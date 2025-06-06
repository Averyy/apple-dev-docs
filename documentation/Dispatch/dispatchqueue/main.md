# main

**Framework**: Dispatch  
**Kind**: property

The dispatch queue associated with the main thread of the current process.

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
class var main: DispatchQueue { get }
```

#### Discussion

The system automatically creates the main queue and associates it with your application’s main thread. Your app uses one (and only one) of the following three approaches to execute blocks submitted to the main queue:

- Calling [`dispatchMain()`](dispatchmain().md)
- Starting your app with a call to [`UIApplicationMain(_:_:_:_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationMain(_:_:_:_:)-1yub7) (iOS) or [`NSApplicationMain(_:_:)`](https://developer.apple.com/documentation/AppKit/NSApplicationMain(_:_:)) (macOS)
- Using a [`CFRunLoop`](https://developer.apple.com/documentation/CoreFoundation/CFRunLoop) on the main thread

As with the global concurrent queues, calls to [`suspend()`](dispatchobject/suspend().md), [`resume()`](dispatchobject/resume().md), [`dispatch_set_context`](dispatch_set_context.md), and the like have no effect when used on the queue in this property.

> ❗ **Important**:  If the main thread is unresponsive for too long, it can lead to a `0x8badf00d` exception with the main thread at `mach_msg_trap`. On iOS, this exception may be raised if the watchdog mechanism detects that your app failed to respond to certain user interface events in time. The iOS watchdog exists in order to keep the user interface responsive.

 If the main thread is unresponsive for too long, it can lead to a `0x8badf00d` exception with the main thread at `mach_msg_trap`. On iOS, this exception may be raised if the watchdog mechanism detects that your app failed to respond to certain user interface events in time. The iOS watchdog exists in order to keep the user interface responsive.

If your app has a long running task, such as making network call, run it on a global system queue, or on another background dispatch queue. Alternatively, use asynchronous versions of the call, if available.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/main)*