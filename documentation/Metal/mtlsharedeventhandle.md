# MTLSharedEventHandle

**Framework**: Metal  
**Kind**: class  
**Role**: Class

An instance you use to recreate a shareable event.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MTLSharedEventHandle
```

```objc
@interface MTLSharedEventHandle : NSObject
```

## Overview

To create a `MTLSharedEventHandle` instance, call the [`makeSharedEventHandle()`](./mtlsharedevent/makesharedeventhandle%28%29.md) method on an [`MTLSharedEvent`](./mtlsharedevent.md) instance. Use an XPC conection to pass a `MTLSharedEventHandle` instance to another process. To recreate the event, call the [`makeSharedEvent(handle:)`](./mtldevice/makesharedevent%28handle%29.md) on an [`MTLDevice`](./mtldevice.md) instance.

## Topics

### Identifying the shareable event handle
- [var label: String?](./mtlsharedeventhandle/label.md)
  A string that identifies the shareable event.
### Initializers
- [init?(coder: NSCoder)](./mtlsharedeventhandle/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Synchronizing with events
- [Implementing a multistage image filter using heaps and events](./implementing-a-multistage-image-filter-using-heaps-and-events.md)
  Use events to synchronize access to resources allocated on a heap.
- [About synchronization events](./about-synchronization-events.md)
  Synchronize access to resources in your app by signaling events.
- [Synchronizing events within a single device](./synchronizing-events-within-a-single-device.md)
  Use nonshareable events to synchronize your app’s work within a single device.
- [Synchronizing events across multiple devices or processes](./synchronizing-events-across-multiple-devices-or-processes.md)
  Use shareable events to synchronize your app’s work across multiple devices or processes.
- [Synchronizing events between a GPU and the CPU](./synchronizing-events-between-a-gpu-and-the-cpu.md)
  Use shareable events to synchronize your app’s work between a GPU and the CPU.
- [protocol MTLEvent](./mtlevent.md)
  A type that synchronizes memory operations to one or more resources within a single Metal device.
- [protocol MTLSharedEvent](./mtlsharedevent.md)
  A type that synchronizes memory operations to one or more resources across multiple CPUs, GPUs, and processes.
- [class MTLSharedEventListener](./mtlsharedeventlistener.md)
  A listener for shareable event notifications.
- [typealias MTLSharedEventNotificationBlock](./mtlsharedeventnotificationblock.md)
  A block of code invoked after a shareable event’s signal value equals or exceeds a given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsharedeventhandle)*