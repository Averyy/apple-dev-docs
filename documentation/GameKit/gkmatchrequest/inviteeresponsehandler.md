# inviteeResponseHandler

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

Handles when a player responds to an invitation.

**Availability**:
- iOS 6.0+ - Deprecated in 8.0
- iPadOS 6.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`recipientResponseHandler`](./recipientresponsehandler.md) property instead.

## Declaration

```swift
var inviteeResponseHandler: ((String, GKInviteeResponse) -> Void)? { get set }
```

```objc
@property (copy, nullable) void (^)(NSString *, enum GKInviteRecipientResponse) inviteeResponseHandler;
```

#### Discussion

The block takes the following parameters:

- ***playerID***: The identifier for the player.
- ***GKInviteeResponse***: The nature of the response. See [`GKInviteeResponse`](../gkinviteeresponse.md).

An invitee response handler is called whenever you programmatically invite specific players to join a match. It is called once for each player invited to the match. Typically, your game uses the responses to update the custom user interface. For example, you want the player to be able to perform any of the following tasks:

- Start the match.
- Invite an additional set of specific players.
- Use matchmaking to fill the remaining match slots.

## See Also

### Deprecated methods and properties
- [typealias GKInviteeResponse](../gkinviteeresponse.md)
  Possible responses from an invitation to a remote player.
- [var playersToInvite: [String]?](./playerstoinvite.md)
  A list of player identifiers for players to invite to the match.
- [var restrictToAutomatch: Bool](./restricttoautomatch.md)
  A Boolean value that determines whether a game uses automatch to find players or the local player invites players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchrequest/inviteeresponsehandler)*