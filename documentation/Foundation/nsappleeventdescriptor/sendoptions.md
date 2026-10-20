# NSAppleEventDescriptor.SendOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.11+

## Declaration

```swift
struct SendOptions
```

```c
enum NSAppleEventSendOptions : NSUInteger;
```

## Topics

### Constants
- [static var alwaysInteract: NSAppleEventDescriptor.SendOptions](./sendoptions/alwaysinteract.md)
  Server should always interact with user where appropriate.
- [static var canInteract: NSAppleEventDescriptor.SendOptions](./sendoptions/caninteract.md)
  Server may try to interact with user.
- [static var canSwitchLayer: NSAppleEventDescriptor.SendOptions](./sendoptions/canswitchlayer.md)
  Interaction may switch layer.
- [static var defaultOptions: NSAppleEventDescriptor.SendOptions](./sendoptions/defaultoptions.md)
  The default options: wait for reply and allow interaction.
- [static var dontAnnotate: NSAppleEventDescriptor.SendOptions](./sendoptions/dontannotate.md)
  Don’t automatically add any sandbox or other annotations to the event.
- [static var dontExecute: NSAppleEventDescriptor.SendOptions](./sendoptions/dontexecute.md)
  Don’t execute this event; used for recording.
- [static var dontRecord: NSAppleEventDescriptor.SendOptions](./sendoptions/dontrecord.md)
  Don’t record this event.
- [static var neverInteract: NSAppleEventDescriptor.SendOptions](./sendoptions/neverinteract.md)
  Server should not interact with user.
- [static var noReply: NSAppleEventDescriptor.SendOptions](./sendoptions/noreply.md)
  Sender doesn’t want a reply to event.
- [static var queueReply: NSAppleEventDescriptor.SendOptions](./sendoptions/queuereply.md)
  Sender wants a reply but won’t wait.
- [static var waitForReply: NSAppleEventDescriptor.SendOptions](./sendoptions/waitforreply.md)
  Sender wants a reply and will wait.
### Initializers
- [init(rawValue: UInt)](./sendoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/sendoptions)*