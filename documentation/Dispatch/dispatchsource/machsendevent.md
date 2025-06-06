# DispatchSource.MachSendEvent

**Framework**: Dispatch  
**Kind**: struct

Mach-related events.

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
struct MachSendEvent
```

## Topics

### Mach Event Flags
- [static let dead: DispatchSource.MachSendEvent](dispatchsource/machsendevent/dead.md)
  The receive right corresponding to the given send right was destroyed.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class func makeMachReceiveSource(port: mach_port_t, queue: DispatchQueue?) -> any DispatchSourceMachReceive](dispatchsource/makemachreceivesource(port:queue:).md)
  Creates a new dispatch source object for monitoring a Mach port for pending messages.
- [class func makeMachSendSource(port: mach_port_t, eventMask: DispatchSource.MachSendEvent, queue: DispatchQueue?) -> any DispatchSourceMachSend](dispatchsource/makemachsendsource(port:eventmask:queue:).md)
  A dispatch source that monitors a Mach port for dead name notifications.
- [protocol DispatchSourceMachReceive](dispatchsourcemachreceive.md)
  A dispatch source that monitors a Mach port for pending messages.
- [protocol DispatchSourceMachSend](dispatchsourcemachsend.md)
  A dispatch source that monitors a Mach port for dead name notifications, indicating that a send right no longer has a corresponding receive right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/machsendevent)*