# MPRemoteCommand

**Framework**: Media Player  
**Kind**: class

An object that responds to remote command events.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 7.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class MPRemoteCommand
```

#### Overview

The Media Player framework defines a standard set of remote command objects for handling media-related events. When an accessory or iOS user interface generates a remote control event, the system notifies the corresponding command object on the shared [`MPRemoteCommandCenter`](mpremotecommandcenter.md) instance. That command object executes any attached handlers.

To respond to a particular event, register a handler with the appropriate [`MPRemoteCommand`](mpremotecommand.md) object.

Listing 1. Registering a remote control event handler

If you explicitly don’t want to enable a given command, fetch the command object and set its enabled property to [`false`](https://developer.apple.com/documentation/swift/false). Disabling a remote command lets the system know that it shouldn’t display any related UI for that command when your app is the Now Playing app.

The framework defines many subclasses to handle specific kinds of commands. Sometimes, these subclasses let you specify other information related to the command. For example, feedback commands let you specify a localized string that describes the meaning of the feedback. When supporting a particular command, be sure to look up the specific class used to handle those events.

## Topics

### Handling events
- [func addTarget(handler: (MPRemoteCommandEvent) -> MPRemoteCommandHandlerStatus) -> Any](mpremotecommand/addtarget(handler:).md)
  Adds a block to be called when an event is received.
- [func addTarget(Any, action: Selector)](mpremotecommand/addtarget(_:action:).md)
  Adds a target object to be called when an event is received.
- [func removeTarget(Any?)](mpremotecommand/removetarget(_:).md)
  Removes a target from the remote command object.
- [func removeTarget(Any, action: Selector?)](mpremotecommand/removetarget(_:action:).md)
  Removes a target and action from a remote command object.
- [enum MPRemoteCommandHandlerStatus](mpremotecommandhandlerstatus.md)
  Constants indicating the status of a command.
### Enabling a command object
- [var isEnabled: Bool](mpremotecommand/isenabled.md)
  A Boolean value that indicates whether a user can interact with the displayed element.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MPChangePlaybackPositionCommand](mpchangeplaybackpositioncommand.md)
- [MPChangePlaybackRateCommand](mpchangeplaybackratecommand.md)
- [MPChangeRepeatModeCommand](mpchangerepeatmodecommand.md)
- [MPChangeShuffleModeCommand](mpchangeshufflemodecommand.md)
- [MPFeedbackCommand](mpfeedbackcommand.md)
- [MPRatingCommand](mpratingcommand.md)
- [MPSkipIntervalCommand](mpskipintervalcommand.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Becoming a now playable app](becoming-a-now-playable-app.md)
  Ensure your app is eligible to become the Now Playing app by adopting best practices for providing Now Playing info and registering for remote command center actions.
- [class MPRemoteCommandCenter](mpremotecommandcenter.md)
  An object that responds to remote control events sent by external accessories and system controls.
- [class MPRemoteCommandEvent](mpremotecommandevent.md)
  A description of a command sent by an external media player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommand)*