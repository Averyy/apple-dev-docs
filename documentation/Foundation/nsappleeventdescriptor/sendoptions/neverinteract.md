# neverInteract

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Server should not interact with user.

**Availability**:
- macOS 10.11+

## Declaration

```swift
static var neverInteract: NSAppleEventDescriptor.SendOptions { get }
```

```c
NSAppleEventSendNeverInteract
```

## See Also

### Constants
- [static var alwaysInteract: NSAppleEventDescriptor.SendOptions](./alwaysinteract.md)
  Server should always interact with user where appropriate.
- [static var canInteract: NSAppleEventDescriptor.SendOptions](./caninteract.md)
  Server may try to interact with user.
- [static var canSwitchLayer: NSAppleEventDescriptor.SendOptions](./canswitchlayer.md)
  Interaction may switch layer.
- [static var defaultOptions: NSAppleEventDescriptor.SendOptions](./defaultoptions.md)
  The default options: wait for reply and allow interaction.
- [static var dontAnnotate: NSAppleEventDescriptor.SendOptions](./dontannotate.md)
  Don’t automatically add any sandbox or other annotations to the event.
- [static var dontExecute: NSAppleEventDescriptor.SendOptions](./dontexecute.md)
  Don’t execute this event; used for recording.
- [static var dontRecord: NSAppleEventDescriptor.SendOptions](./dontrecord.md)
  Don’t record this event.
- [static var noReply: NSAppleEventDescriptor.SendOptions](./noreply.md)
  Sender doesn’t want a reply to event.
- [static var queueReply: NSAppleEventDescriptor.SendOptions](./queuereply.md)
  Sender wants a reply but won’t wait.
- [static var waitForReply: NSAppleEventDescriptor.SendOptions](./waitforreply.md)
  Sender wants a reply and will wait.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/sendoptions/neverinteract)*