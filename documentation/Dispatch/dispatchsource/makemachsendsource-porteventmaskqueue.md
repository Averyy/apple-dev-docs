# makeMachSendSource(port:eventMask:queue:)

**Framework**: Dispatch  
**Kind**: method

A dispatch source that monitors a Mach port for dead name notifications.

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
class func makeMachSendSource(port: mach_port_t, eventMask: DispatchSource.MachSendEvent, queue: DispatchQueue? = nil) -> any DispatchSourceMachSend
```

#### Return Value

A dispatch source object that conforms to the [`DispatchSourceMachSend`](dispatchsourcemachsend.md) protocol.

#### Discussion

After creating the dispatch source, use the methods of the [`DispatchSourceProtocol`](dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [`activate()`](dispatchobject/activate().md) method.

## Parameters

- `port`: A Mach port with a send or send-once right.
- `eventMask`: The events you want to monitor. For a list of possible values, see  .
- `queue`: The dispatch queue to use when executing the installed handlers.

## See Also

- [class func makeMachReceiveSource(port: mach_port_t, queue: DispatchQueue?) -> any DispatchSourceMachReceive](dispatchsource/makemachreceivesource(port:queue:).md)
  Creates a new dispatch source object for monitoring a Mach port for pending messages.
- [protocol DispatchSourceMachReceive](dispatchsourcemachreceive.md)
  A dispatch source that monitors a Mach port for pending messages.
- [protocol DispatchSourceMachSend](dispatchsourcemachsend.md)
  A dispatch source that monitors a Mach port for dead name notifications, indicating that a send right no longer has a corresponding receive right.
- [DispatchSource.MachSendEvent](dispatchsource/machsendevent.md)
  Mach-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/makemachsendsource(port:eventmask:queue:))*