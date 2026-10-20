# DispatchSourceMachReceive

**Framework**: Dispatch  
**Kind**: protocol  
**Role**: Protocol

A dispatch source that monitors a Mach port for pending messages.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
protocol DispatchSourceMachReceive : DispatchSourceProtocol, Sendable
```

#### Overview

You do not adopt this protocol in your objects. Instead, use the [`makeMachReceiveSource(port:queue:)`](./dispatchsource/makemachreceivesource%28port,queue%29.md) method to create an object that adopts this protocol.

## Topics

### Getting the Mach Port Handle
- [var handle: mach_port_t](./dispatchsourcemachreceive/handle.md)

## Relationships

### Inherits From
- [DispatchSourceProtocol](./dispatchsourceprotocol.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [DispatchSource](./dispatchsource.md)

## See Also

### Creating a Mach Port Source
- [class func makeMachReceiveSource(port: mach_port_t, queue: DispatchQueue?) -> any DispatchSourceMachReceive](./dispatchsource/makemachreceivesource%28port,queue%29.md)
  Creates a new dispatch source object for monitoring a Mach port for pending messages.
- [class func makeMachSendSource(port: mach_port_t, eventMask: DispatchSource.MachSendEvent, queue: DispatchQueue?) -> any DispatchSourceMachSend](./dispatchsource/makemachsendsource%28port,eventmask,queue%29.md)
  A dispatch source that monitors a Mach port for dead name notifications.
- [protocol DispatchSourceMachSend](./dispatchsourcemachsend.md)
  A dispatch source that monitors a Mach port for dead name notifications, indicating that a send right no longer has a corresponding receive right.
- [DispatchSource.MachSendEvent](./dispatchsource/machsendevent.md)
  Mach-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourcemachreceive)*