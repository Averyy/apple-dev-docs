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

### Initializing a shareable event listener
- [init()](mtlsharedeventlistener/init.md)
  Creates a new shareable event listener.
- [init(dispatchQueue: dispatch_queue_t)](mtlsharedeventlistener/init(dispatchqueue:).md)
  Creates a new shareable event listener with a specific dispatch queue.
### Getting the dispatch queue
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

- [Implementing a multistage image filter using heaps and events](implementing-a-multistage-image-filter-using-heaps-and-events.md)
  Use events to synchronize access to resources allocated on a heap.
- [About synchronization events](about-synchronization-events.md)
  Synchronize access to resources in your app by signaling events.
- [Synchronizing events within a single device](synchronizing-events-within-a-single-device.md)
  Use nonshareable events to synchronize your app’s work within a single device.
- [Synchronizing events across multiple devices or processes](synchronizing-events-across-multiple-devices-or-processes.md)
  Use shareable events to synchronize your app’s work across multiple devices or processes.
- [Synchronizing events between a GPU and the CPU](synchronizing-events-between-a-gpu-and-the-cpu.md)
  Use shareable events to synchronize your app’s work between a GPU and the CPU.
- [protocol MTLEvent](mtlevent.md)
  A type that synchronizes memory operations to one or more resources within a single Metal device.
- [protocol MTLSharedEvent](mtlsharedevent.md)
  A type that synchronizes memory operations to one or more resources across multiple CPUs, GPUs, and processes.
- [class MTLSharedEventHandle](mtlsharedeventhandle.md)
  An instance you use to recreate a shareable event.
- [typealias MTLSharedEventNotificationBlock](mtlsharedeventnotificationblock.md)
  A block of code invoked after a shareable event’s signal value equals or exceeds a given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsharedeventlistener)*