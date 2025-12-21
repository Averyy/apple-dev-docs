# Synchronizing events between a GPU and the CPU

**Framework**: Metal

Use shareable events to synchronize your app’s work between a GPU and the CPU.

#### Overview

A shared event has methods and properties that let your app execute code when the event is triggered, or update the event’s value.

Call the [`notify(_:atValue:block:)`](mtlsharedevent/notify(_:atvalue:block:).md) method to register a notification handler that listens for changes to a shared event’s value. When some other action signals the event to give it a new value that is equal or larger than this value, such as when you signal the event from a command you sent to the GPU, the notification handler executes the block of code that you provided.

Set the shared event’s  [`signaledValue`](mtlsharedevent/signaledvalue.md) property to signal the event from the CPU. The value is only updated if you set a value larger than the current value stored in the event. Setting the value unblocks any commands waiting on a value equal to or smaller than the new value, and similarly triggers any CPU-based notifications.

The following figure and code show a shareable event that synchronizes GPU work and CPU work.

![Timeline diagram that shows shareable synchronization events for a GPU and the CPU, and the work that the GPU and CPU do.](https://docs-assets.developer.apple.com/published/982692fdd01837bd9a1ab0ec43a73c87/media-3400866%402x.png)

The setup code creates a shareable event and a listener object. Listener objects are used to dispatch notifications to the app when the event is signaled.

The work for this task is shared between the GPU and the CPU. As you can see in the figure above, the code needs to execute in the following order:

1. GPU work part 1
2. GPU work part 2
3. CPU work
4. GPU part 3

The `setupGPUCPUEvent` function uses signals to enforce this execution order. First, the function registers an event handler to be executed when the event is signaled. When called, this event handler executes the code for step 3 and then signals the event. That completes the CPU portion of the task.

Next, the function encodes the work for the GPU. It encodes the work for part 1, signals the event, and then does the same for part 2, and signals the event again. Part 3 of the GPU code needs to run after the event handler finishes executing, so next the function encodes a command to wait for the CPU to signal the event. After this, the function encodes the commands for part 3 and commits the command buffer for execution.

When the function commits the command buffer, the following actions occur:

1. The GPU executes the first part of the task.
2. The GPU signals the event to a new value of 1.
3. The GPU executes the second part of the task.
4. The GPU signals the event to a new value of 2.
5. The CPU detects the signal value and runs the notification handler.
6. The notification handler signals the event to a new value of 3.
7. The GPU detects the signal value and executes the remaining commands.

## See Also

- [Implementing a multistage image filter using heaps and events](implementing-a-multistage-image-filter-using-heaps-and-events.md)
  Use events to synchronize access to resources allocated on a heap.
- [About synchronization events](about-synchronization-events.md)
  Synchronize access to resources in your app by signaling events.
- [Synchronizing events within a single device](synchronizing-events-within-a-single-device.md)
  Use nonshareable events to synchronize your app’s work within a single device.
- [Synchronizing events across multiple devices or processes](synchronizing-events-across-multiple-devices-or-processes.md)
  Use shareable events to synchronize your app’s work across multiple devices or processes.
- [protocol MTLEvent](mtlevent.md)
  A type that synchronizes memory operations to one or more resources within a single Metal device.
- [protocol MTLSharedEvent](mtlsharedevent.md)
  A type that synchronizes memory operations to one or more resources across multiple CPUs, GPUs, and processes.
- [class MTLSharedEventHandle](mtlsharedeventhandle.md)
  An instance you use to recreate a shareable event.
- [class MTLSharedEventListener](mtlsharedeventlistener.md)
  A listener for shareable event notifications.
- [typealias MTLSharedEventNotificationBlock](mtlsharedeventnotificationblock.md)
  A block of code invoked after a shareable event’s signal value equals or exceeds a given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/synchronizing-events-between-a-gpu-and-the-cpu)*