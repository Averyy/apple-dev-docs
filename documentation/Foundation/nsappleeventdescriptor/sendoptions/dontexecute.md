# dontExecute

**Framework**: Foundation  
**Kind**: property

Don’t execute this event; used for recording.

**Availability**:
- macOS 10.11+

## Declaration

```swift
static var dontExecute: NSAppleEventDescriptor.SendOptions { get }
```

## See Also

- [static var alwaysInteract: NSAppleEventDescriptor.SendOptions](nsappleeventdescriptor/sendoptions/alwaysinteract.md)
  Server should always interact with user where appropriate.
- [static var canInteract: NSAppleEventDescriptor.SendOptions](nsappleeventdescriptor/sendoptions/caninteract.md)
  Server may try to interact with user.
- [static var canSwitchLayer: NSAppleEventDescriptor.SendOptions](nsappleeventdescriptor/sendoptions/canswitchlayer.md)
  Interaction may switch layer.
- [static var defaultOptions: NSAppleEventDescriptor.SendOptions](nsappleeventdescriptor/sendoptions/defaultoptions.md)
  The default options: wait for reply and allow interaction.
- [static var dontAnnotate: NSAppleEventDescriptor.SendOptions](nsappleeventdescriptor/sendoptions/dontannotate.md)
  Don’t automatically add any sandbox or other annotations to the event.
- [static var dontRecord: NSAppleEventDescriptor.SendOptions](nsappleeventdescriptor/sendoptions/dontrecord.md)
  Don’t record this event.
- [static var neverInteract: NSAppleEventDescriptor.SendOptions](nsappleeventdescriptor/sendoptions/neverinteract.md)
  Server should not interact with user.
- [static var noReply: NSAppleEventDescriptor.SendOptions](nsappleeventdescriptor/sendoptions/noreply.md)
  Sender doesn’t want a reply to event.
- [static var queueReply: NSAppleEventDescriptor.SendOptions](nsappleeventdescriptor/sendoptions/queuereply.md)
  Sender wants a reply but won’t wait.
- [static var waitForReply: NSAppleEventDescriptor.SendOptions](nsappleeventdescriptor/sendoptions/waitforreply.md)
  Sender wants a reply and will wait.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/sendoptions/dontexecute)*