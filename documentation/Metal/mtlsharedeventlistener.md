# MTLSharedEventListener

**Framework**: Metal  
**Kind**: class

A listener for shareable event notifications.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MTLSharedEventListener
```

## Topics

### Initializing a Shareable Event Listener
- [init()](mtlsharedeventlistener/init.md)
  Creates a new shareable event listener.
- [init(dispatchQueue: dispatch_queue_t)](mtlsharedeventlistener/init(dispatchqueue:).md)
  Creates a new shareable event listener with a specific dispatch queue.
### Getting the Dispatch Queue
- [var dispatchQueue: dispatch_queue_t](mtlsharedeventlistener/dispatchqueue.md)
  The dispatch queue used to dispatch any notifications.
### Type Methods
- [class func shared() -> MTLSharedEventListener](mtlsharedeventlistener/shared.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Implementing a Multistage Image Filter Using Heaps and Events](implementing-a-multistage-image-filter-using-heaps-and-events.md)
  Use events to synchronize access to resources allocated on a heap.
- [About Synchronization Events](about-synchronization-events.md)
  Synchronize access to resources in your app by signaling events.
- [Synchronizing Events Within a Single Device](synchronizing-events-within-a-single-device.md)
  Use nonshareable events to synchronize your app’s work within a single device.
- [Synchronizing Events Across Multiple Devices or Processes](synchronizing-events-across-multiple-devices-or-processes.md)
  Use shareable events to synchronize your app’s work across multiple devices or processes.
- [Synchronizing Events Between a GPU and the CPU](synchronizing-events-between-a-gpu-and-the-cpu.md)
  Use shareable events to synchronize your app’s work between a GPU and the CPU.
- [protocol MTLEvent](mtlevent.md)
  A simple semaphore to synchronize access to Metal resources.
- [protocol MTLSharedEvent](mtlsharedevent.md)
  An object you use to synchronize access to Metal resources across multiple CPUs, GPUs, and processes.
- [class MTLSharedEventHandle](mtlsharedeventhandle.md)
  An object you use to recreate a shareable event.
- [typealias MTLSharedEventNotificationBlock](mtlsharedeventnotificationblock.md)
  A block of code invoked after a shareable event’s signal value equals or exceeds a given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsharedeventlistener)*