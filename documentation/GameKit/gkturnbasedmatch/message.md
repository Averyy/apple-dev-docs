# message

**Framework**: GameKit  
**Kind**: property

A message from the current participant to all other participants when you end a turn, forfeit a match, or end a match.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var message: String? { get set }
```

## Mentions

- [Sending messages to players in turn-based games](sending-messages-to-players-in-turn-based-games.md)

#### Discussion

Set this property only when the local player is the current participant and before you invoke a method that generates a turn-based event.

If your game instance isn’t running or is running in the background on other participant devices, a notification containing the message appears at the top of the screen. If the game is in the foreground, you can get the message from the match object when handling the turn-based event.

## See Also

- [func setLocalizableMessageWithKey(String, arguments: [String]?)](gkturnbasedmatch/setlocalizablemessagewithkey(_:arguments:).md)
  Sends a localized message from the current participant to all other participants when you end a turn, forfeit a match, or end a match.
- [func sendReminder(to: [GKTurnBasedParticipant], localizableMessageKey: String, arguments: [String], completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/sendreminder(to:localizablemessagekey:arguments:completionhandler:).md)
  Sends a reminder from one participant to a specific set of other participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/message)*