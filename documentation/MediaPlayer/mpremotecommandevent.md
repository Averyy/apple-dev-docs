# MPRemoteCommandEvent

**Framework**: Media Player  
**Kind**: class  
**Role**: Class

A description of a command sent by an external media player.

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
class MPRemoteCommandEvent
```

```objc
@interface MPRemoteCommandEvent : NSObject
```

## Topics

### Retrieving command information
- [var command: MPRemoteCommand](./mpremotecommandevent/command.md)
  The command that sent the event.
- [var timestamp: TimeInterval](./mpremotecommandevent/timestamp.md)
  The time the event occurred.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [MPChangeLanguageOptionCommandEvent](./mpchangelanguageoptioncommandevent.md)
- [MPChangePlaybackPositionCommandEvent](./mpchangeplaybackpositioncommandevent.md)
- [MPChangePlaybackRateCommandEvent](./mpchangeplaybackratecommandevent.md)
- [MPChangeRepeatModeCommandEvent](./mpchangerepeatmodecommandevent.md)
- [MPChangeShuffleModeCommandEvent](./mpchangeshufflemodecommandevent.md)
- [MPFeedbackCommandEvent](./mpfeedbackcommandevent.md)
- [MPRatingCommandEvent](./mpratingcommandevent.md)
- [MPSeekCommandEvent](./mpseekcommandevent.md)
- [MPSkipIntervalCommandEvent](./mpskipintervalcommandevent.md)
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
- [class MPRemoteCommand](./mpremotecommand.md)
  An object that responds to remote command events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommandevent)*