# MTLEvent

**Framework**: Metal  
**Kind**: protocol

A simple semaphore to synchronize access to Metal resources.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLEvent : NSObjectProtocol, Sendable
```

## Mentions

- [About Synchronization Events](about-synchronization-events.md)
- [Synchronizing resource accesses between multiple passes with a fence](synchronizing-resource-accesses-between-multiple-passes-with-a-fence.md)

#### Overview

You can only get an [`MTLEvent`](mtlevent.md) using the [`makeEvent()`](mtldevice/makeevent().md) method of an [`MTLDevice`](mtldevice.md) instance. Events allow you to synchronize commands executing on a single Metal device.

An event is an unsigned 64-bit integer, starting with an initial value of `0` and can only increase in value afterwards. You signal an event change by calling an [`MTLCommandBuffer`](mtlcommandbuffer.md) instance’s [`encodeSignalEvent(_:value:)`](mtlcommandbuffer/encodesignalevent(_:value:).md) method. The command buffer signals the event after the GPU completes running all previous commands, and updates its value if necessary.

To wait for an event signal, call [`encodeWaitForEvent(_:value:)`](mtlcommandbuffer/encodewaitforevent(_:value:).md) on a command buffer, passing in the value to wait for. When the device executes the command buffer and reaches this wait command, it compares the event’s current value to the provided value. The device only starts new commands when the event reaches a value equal to or greater than the requested value.

You can encode signaling and waiting on events into different command buffers, even command buffers executing on two different command queues for the same device. You can also encode these commands independently of each other, meaning, for example, that you can wait on signals you haven’t encoded yet.

For more information, see [`Synchronizing Events Within a Single Device`](synchronizing-events-within-a-single-device.md).

## Topics

### Identifying the Event
- [var device: (any MTLDevice)?](mtlevent/device.md)
  The device object that created the event.
- [var label: String?](mtlevent/label.md)
  A string that identifies the event.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [MTLSharedEvent](mtlsharedevent.md)

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
- [protocol MTLSharedEvent](mtlsharedevent.md)
  An object you use to synchronize access to Metal resources across multiple CPUs, GPUs, and processes.
- [class MTLSharedEventHandle](mtlsharedeventhandle.md)
  An object you use to recreate a shareable event.
- [class MTLSharedEventListener](mtlsharedeventlistener.md)
  A listener for shareable event notifications.
- [typealias MTLSharedEventNotificationBlock](mtlsharedeventnotificationblock.md)
  A block of code invoked after a shareable event’s signal value equals or exceeds a given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlevent)*