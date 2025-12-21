# MTLEvent

**Framework**: Metal  
**Kind**: protocol

A type that synchronizes memory operations to one or more resources within a single Metal device.

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

- [About synchronization events](about-synchronization-events.md)
- [Synchronizing passes with a fence](synchronizing-passes-with-a-fence.md)
- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Overview

Each event represents an unsigned 64-bit integer that starts with a value of `0`, which can only increase over time. Create an [`MTLEvent`](mtlevent.md) by calling the [`makeEvent()`](mtldevice/makeevent().md) method of an [`MTLDevice`](mtldevice.md) instance.

With an event, synchronize commands across a single Metal device by instructing it to wait before starting a workload, such as a compute pass, until another workload finishes. You do this by encoding signal and wait commands:

- Add a signal command after encoding the producing workload that one or more other workloads depend on.
- Add a wait command before encoding each consuming workload that depends on the producing workload.

The Metal device begins running any dependent workloads when the event equals or exceeds the value that the wait command is waiting for.

##### Synchronize One Producing Workload with an Event

When working with Metal 4 types, add wait and signal commands with an [`MTL4CommandQueue`](mtl4commandqueue.md) instance by calling its methods:

- [`waitForEvent(_:value:)`](mtl4commandqueue/waitforevent(_:value:).md)
- [`signalEvent(_:value:)`](mtl4commandqueue/signalevent(_:value:).md)

Similarly for Metal 3 and earlier, add wait and signal commands with an [`MTLCommandBuffer`](mtlcommandbuffer.md) instance by calling its methods:

- [`encodeWaitForEvent(_:value:)`](mtlcommandbuffer/encodewaitforevent(_:value:).md)
- [`encodeSignalEvent(_:value:)`](mtlcommandbuffer/encodesignalevent(_:value:).md)

> ❗ **Important**:  You can signal an event only with a new value that’s greater than its current value.

When a Metal device reaches a wait command, it compares the event’s current value to the command’s target value. The device proceeds to the subsequent commands only when another command updates the event with a value that’s equal to or greater than the target value. For an example that synchronizes workloads on different queues within the same device with a single event instance, see [`Synchronizing events within a single device`](synchronizing-events-within-a-single-device.md).

You can add signal and wait commands to any combination of [`MTL4CommandQueue`](mtl4commandqueue.md) and [`MTLCommandBuffer`](mtlcommandbuffer.md) instances that all belong to the same Metal device. Even though you encode a wait command before the signal command that unblocks it, minimize the time between when they run because wait commands can time out.

> ❗ **Important**:  Wait commands that time out in an [`MTL4CommandQueue`](mtl4commandqueue.md) unblock subsequent work in the queue, and wait commands that time out in an [`MTLCommandBuffer`](mtlcommandbuffer.md) terminate the command buffer with the [`MTLCommandBufferError.Code.timeout`](mtlcommandbuffererror-swift.struct/code/timeout.md) error code.

One event signal can unblock multiple workloads waiting for it. For example, if workload A needs to run before starting workloads B and C, the B and C workloads can wait for one event to reach a specific value, such as `0x42`. When workload A finishes, the next command can unblock workloads B and C by signaling that event with the value `0x42` or greater.

##### Synchronize Multiple Producing Workloads with an Event for Each

Multiple producing workloads can’t combine their signals with one event to unblock any dependent workloads. This is because an event’s signal method can only increase its value to a specific number, unlike a semaphore that can increment or decrement its current value by one. Instead, signal when each producing workload finishes by updating its own separate event. Dependent workloads can wait for the multiple events that correspond to the workloads they depend on.

> 💡 **Tip**: For workloads with complicated dependency chains, consider other access synchronization mechanisms that [`Resource synchronization`](resource-synchronization.md) introduces.

## Topics

### Identifying the event
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
- [protocol MTLSharedEvent](mtlsharedevent.md)
  A type that synchronizes memory operations to one or more resources across multiple CPUs, GPUs, and processes.
- [class MTLSharedEventHandle](mtlsharedeventhandle.md)
  An instance you use to recreate a shareable event.
- [class MTLSharedEventListener](mtlsharedeventlistener.md)
  A listener for shareable event notifications.
- [typealias MTLSharedEventNotificationBlock](mtlsharedeventnotificationblock.md)
  A block of code invoked after a shareable event’s signal value equals or exceeds a given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlevent)*