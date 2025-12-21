# MTLSharedEventNotificationBlock

**Framework**: Metal  
**Kind**: typealias

A block of code invoked after a shareable event’s signal value equals or exceeds a given value.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias MTLSharedEventNotificationBlock = (any MTLSharedEvent, UInt64) -> Void
```

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
- [class MTLSharedEventListener](mtlsharedeventlistener.md)
  A listener for shareable event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsharedeventnotificationblock)*