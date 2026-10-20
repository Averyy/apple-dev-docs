# MPRemoteCommand

**Framework**: Media Player  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPRemoteCommand : NSObject
```

#### Overview

The Media Player framework defines a standard set of remote command objects for handling media-related events. When an accessory or iOS user interface generates a remote control event, the system notifies the corresponding command object on the shared [`MPRemoteCommandCenter`](./mpremotecommandcenter.md) instance. That command object executes any attached handlers.

To respond to a particular event, register a handler with the appropriate [`MPRemoteCommand`](./mpremotecommand.md) object.

Listing 1. Registering a remote control event handler

**Swift**:

```swift
// Get the shared command center.
let commandCenter = MPRemoteCommandCenter.shared()

// Add a handler for the play command.
commandCenter.playCommand.addTarget { [unowned self] event in
    if self.player.rate == 0.0 {
        self.player.play()
        return .success
    }
    return .commandFailed
}
```

**Objective-C**:

```objc
// Get the shared command center.
MPRemoteCommandCenter *commandCenter = [MPRemoteCommandCenter sharedCommandCenter];

// Add a handler for the play command.
[commandCenter.playCommand addTargetWithHandler:^MPRemoteCommandHandlerStatus(MPRemoteCommandEvent * _Nonnull event) {
    if (self.player.rate == 0.0) {
        [self.player play];
        return MPRemoteCommandHandlerStatusSuccess;
    }
    return MPRemoteCommandHandlerStatusCommandFailed;
}];
```

If you explicitly don’t want to enable a given command, fetch the command object and set its enabled property to [`false`](../Swift/false.md). Disabling a remote command lets the system know that it shouldn’t display any related UI for that command when your app is the Now Playing app.

The framework defines many subclasses to handle specific kinds of commands. Sometimes, these subclasses let you specify other information related to the command. For example, feedback commands let you specify a localized string that describes the meaning of the feedback. When supporting a particular command, be sure to look up the specific class used to handle those events.

## Topics

### Handling events
- [func addTarget(handler: (MPRemoteCommandEvent) -> MPRemoteCommandHandlerStatus) -> Any](./mpremotecommand/addtarget%28handler%29.md)
  Adds a block to be called when an event is received.
- [func addTarget(Any, action: Selector)](./mpremotecommand/addtarget%28_,action%29.md)
  Adds a target object to be called when an event is received.
- [func removeTarget(Any?)](./mpremotecommand/removetarget%28_%29.md)
  Removes a target from the remote command object.
- [func removeTarget(Any, action: Selector?)](./mpremotecommand/removetarget%28_,action%29.md)
  Removes a target and action from a remote command object.
- [enum MPRemoteCommandHandlerStatus](./mpremotecommandhandlerstatus.md)
  Constants indicating the status of a command.
### Enabling a command object
- [var isEnabled: Bool](./mpremotecommand/isenabled.md)
  A Boolean value that indicates whether a user can interact with the displayed element.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [MPChangePlaybackPositionCommand](./mpchangeplaybackpositioncommand.md)
- [MPChangePlaybackRateCommand](./mpchangeplaybackratecommand.md)
- [MPChangeRepeatModeCommand](./mpchangerepeatmodecommand.md)
- [MPChangeShuffleModeCommand](./mpchangeshufflemodecommand.md)
- [MPFeedbackCommand](./mpfeedbackcommand.md)
- [MPRatingCommand](./mpratingcommand.md)
- [MPSkipIntervalCommand](./mpskipintervalcommand.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Setting up the remote event handler
- [Becoming a now playable app](./becoming-a-now-playable-app.md)
  Ensure your app is eligible to become the Now Playing app by adopting best practices for providing Now Playing info and registering for remote command center actions.
- [class MPRemoteCommandCenter](./mpremotecommandcenter.md)
  An object that responds to remote control events sent by external accessories and system controls.
- [class MPRemoteCommandEvent](./mpremotecommandevent.md)
  A description of a command sent by an external media player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommand)*