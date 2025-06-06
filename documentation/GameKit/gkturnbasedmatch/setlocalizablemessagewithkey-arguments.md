# setLocalizableMessageWithKey(_:arguments:)

**Framework**: GameKit  
**Kind**: method

Sends a localized message from the current participant to all other participants when you end a turn, forfeit a match, or end a match.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func setLocalizableMessageWithKey(_ key: String, arguments: [String]?)
```

## Mentions

- [Sending messages to players in turn-based games](sending-messages-to-players-in-turn-based-games.md)

#### Discussion

Invoke this method only when the local player is the current participant and before you invoke a method that generates a turn-based event.

If your game isn’t running or is running in the background on other participant devices, a notification containing the localized message appears immediately at the top of the screen. If the game is in the foreground, use the [`message`](gkturnbasedmatch/message.md) property to get the localized message when handling the turn-based event.

GameKit uses the recipient’s language and region to localize the message. If the recipient doesn’t have the game installed on their device, GameKit uses the sender’s localization settings instead. See [`Sending messages to players in turn-based games`](sending-messages-to-players-in-turn-based-games.md).

## Parameters

- `key`: The identifier for looking up the translated string in the default   file. If you use a formatted string with specifiers, provide the arguments.
- `arguments`: A list of arguments to substitute into the localized string if it’s formatted and contains specifiers.

## See Also

- [var message: String?](gkturnbasedmatch/message.md)
  A message from the current participant to all other participants when you end a turn, forfeit a match, or end a match.
- [func sendReminder(to: [GKTurnBasedParticipant], localizableMessageKey: String, arguments: [String], completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/sendreminder(to:localizablemessagekey:arguments:completionhandler:).md)
  Sends a reminder from one participant to a specific set of other participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/setlocalizablemessagewithkey(_:arguments:))*