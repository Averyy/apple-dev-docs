# DispatchSourceMachSend

**Framework**: Dispatch  
**Kind**: protocol

A dispatch source that monitors a Mach port for dead name notifications, indicating that a send right no longer has a corresponding receive right.

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
protocol DispatchSourceMachSend : DispatchSourceProtocol, Sendable
```

#### Overview

You do not adopt this protocol in your objects. Instead, use the [`makeMachSendSource(port:eventMask:queue:)`](dispatchsource/makemachsendsource(port:eventmask:queue:).md) method to create an object that adopts this protocol.

## Topics

### Getting the Mach Port Handle
- [var handle: mach_port_t](dispatchsourcemachsend/handle.md)
### Getting the Event Data
- [var data: DispatchSource.MachSendEvent](dispatchsourcemachsend/data.md)
- [var mask: DispatchSource.MachSendEvent](dispatchsourcemachsend/mask.md)

## Relationships

### Inherits From
- [DispatchSourceProtocol](dispatchsourceprotocol.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [DispatchSource](dispatchsource.md)

## See Also

- [class func makeMachReceiveSource(port: mach_port_t, queue: DispatchQueue?) -> any DispatchSourceMachReceive](dispatchsource/makemachreceivesource(port:queue:).md)
  Creates a new dispatch source object for monitoring a Mach port for pending messages.
- [class func makeMachSendSource(port: mach_port_t, eventMask: DispatchSource.MachSendEvent, queue: DispatchQueue?) -> any DispatchSourceMachSend](dispatchsource/makemachsendsource(port:eventmask:queue:).md)
  A dispatch source that monitors a Mach port for dead name notifications.
- [protocol DispatchSourceMachReceive](dispatchsourcemachreceive.md)
  A dispatch source that monitors a Mach port for pending messages.
- [DispatchSource.MachSendEvent](dispatchsource/machsendevent.md)
  Mach-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourcemachsend)*