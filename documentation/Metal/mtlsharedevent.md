# MTLSharedEvent

**Framework**: Metal  
**Kind**: protocol

An object you use to synchronize access to Metal resources across multiple CPUs, GPUs, and processes.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLSharedEvent : MTLEvent
```

## Mentions

- [About Synchronization Events](about-synchronization-events.md)
- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)
- [Synchronizing Events Across Multiple Devices or Processes](synchronizing-events-across-multiple-devices-or-processes.md)
- [Synchronizing resource accesses between multiple passes with a fence](synchronizing-resource-accesses-between-multiple-passes-with-a-fence.md)

#### Overview

The [`MTLSharedEvent`](mtlsharedevent.md) protocol inherits from and adds additional behaviors to [`MTLEvent`](mtlevent.md). Use shared events only when you need to synchronize changes to resources across multiple Metal device objects, across processes, or between a device object and CPU access to resources. Otherwise, use nonshared events.

Don’t implement this protocol yourself; instead, to create a [`MTLSharedEvent`](mtlsharedevent.md) object, call the [`makeSharedEvent()`](mtldevice/makesharedevent().md) method of a [`MTLDevice`](mtldevice.md) object.

To pass this event to another process, first create a handle to the shared event by calling its [`makeSharedEventHandle()`](mtlsharedevent/makesharedeventhandle().md) method. Then, transfer the handle to another process with XPC, and from that process, call the [`makeSharedEvent(handle:)`](mtldevice/makesharedevent(handle:).md) of a [`MTLDevice`](mtldevice.md) object.

For more information, see [`Synchronizing Events Across Multiple Devices or Processes`](synchronizing-events-across-multiple-devices-or-processes.md) and [`Synchronizing Events Between a GPU and the CPU`](synchronizing-events-between-a-gpu-and-the-cpu.md).

## Topics

### Synchronizing a Shareable Event
- [var signaledValue: UInt64](mtlsharedevent/signaledvalue.md)
  The current signal value for the shareable event.
- [func notify(MTLSharedEventListener, atValue: UInt64, block: MTLSharedEventNotificationBlock)](mtlsharedevent/notify(_:atvalue:block:).md)
  Schedules a notification handler to be called after the shareable event’s signal value equals or exceeds a given value.
### Creating a Shared Event Handle
- [func makeSharedEventHandle() -> MTLSharedEventHandle](mtlsharedevent/makesharedeventhandle.md)
  Creates a new shareable event handle.
### Instance Methods
- [func valueSignaled(UInt64) async](mtlsharedevent/valuesignaled(_:).md)
- [func wait(untilSignaledValue: UInt64, timeoutMS: UInt64) -> Bool](mtlsharedevent/wait(untilsignaledvalue:timeoutms:).md)

## Relationships

### Inherits From
- [MTLEvent](mtlevent.md)
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
- [class MTLSharedEventHandle](mtlsharedeventhandle.md)
  An object you use to recreate a shareable event.
- [class MTLSharedEventListener](mtlsharedeventlistener.md)
  A listener for shareable event notifications.
- [typealias MTLSharedEventNotificationBlock](mtlsharedeventnotificationblock.md)
  A block of code invoked after a shareable event’s signal value equals or exceeds a given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsharedevent)*