# makeMachReceiveSource(port:queue:)

**Framework**: Dispatch  
**Kind**: method

Creates a new dispatch source object for monitoring a Mach port for pending messages.

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
class func makeMachReceiveSource(port: mach_port_t, queue: DispatchQueue? = nil) -> any DispatchSourceMachReceive
```

#### Return Value

A dispatch source object that conforms to the [`DispatchSourceMachReceive`](dispatchsourcemachreceive.md) protocol.

#### Discussion

After creating the dispatch source, use the methods of the [`DispatchSourceProtocol`](dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [`activate()`](dispatchobject/activate().md) method.

## Parameters

- `port`: A Mach port with a receive right.
- `queue`: The dispatch queue to use when executing the installed handlers.

## See Also

- [class func makeMachSendSource(port: mach_port_t, eventMask: DispatchSource.MachSendEvent, queue: DispatchQueue?) -> any DispatchSourceMachSend](dispatchsource/makemachsendsource(port:eventmask:queue:).md)
  A dispatch source that monitors a Mach port for dead name notifications.
- [protocol DispatchSourceMachReceive](dispatchsourcemachreceive.md)
  A dispatch source that monitors a Mach port for pending messages.
- [protocol DispatchSourceMachSend](dispatchsourcemachsend.md)
  A dispatch source that monitors a Mach port for dead name notifications, indicating that a send right no longer has a corresponding receive right.
- [DispatchSource.MachSendEvent](dispatchsource/machsendevent.md)
  Mach-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/makemachreceivesource(port:queue:))*