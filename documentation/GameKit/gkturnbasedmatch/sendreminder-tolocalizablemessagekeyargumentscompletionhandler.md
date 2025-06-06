# sendReminder(to:localizableMessageKey:arguments:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Sends a reminder from one participant to a specific set of other participants.

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
func sendReminder(to participants: [GKTurnBasedParticipant], localizableMessageKey key: String, arguments: [String]) async throws
```

## Mentions

- [Sending messages to players in turn-based games](sending-messages-to-players-in-turn-based-games.md)

#### Discussion

Use this method to send a localized message to participants of a turn-based event or exchange request that needs their attention.

If your game isn’t running on recipient devices, the notification containing the localized message appears immediately at the top of the screen. When the participant taps or clicks the notification, GameKit launches your game and invokes the `GKTurnBasedEventListener` [`player(_:receivedTurnEventFor:didBecomeActive:)`](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md) protocol method.

GameKit uses the recipient’s language and region to localize the message. If the recipient doesn’t have the game installed on their device, GameKit uses the sender’s localization settings instead. See [`Sending messages to players in turn-based games`](sending-messages-to-players-in-turn-based-games.md).

## Parameters

- `participants`: The participants who Game Center sends the reminder to.
- `key`: The identifier for looking up the translated string in the default   file. If you use a formatted string with specifiers, provide the arguments.
- `arguments`: A list of arguments to substitute into the localized string if it’s formatted and contains specifiers.
- `completionHandler`: The block receives the following parameter:

## See Also

- [var message: String?](gkturnbasedmatch/message.md)
  A message from the current participant to all other participants when you end a turn, forfeit a match, or end a match.
- [func setLocalizableMessageWithKey(String, arguments: [String]?)](gkturnbasedmatch/setlocalizablemessagewithkey(_:arguments:).md)
  Sends a localized message from the current participant to all other participants when you end a turn, forfeit a match, or end a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/sendreminder(to:localizablemessagekey:arguments:completionhandler:))*