# restrictToAutomatch

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether a game uses automatch to find players or the local player invites players.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0
- iPadOS 13.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.15+ - Deprecated in 11.0
- tvOS 13.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 7.0

> **Deprecated**: Use the [`matchmakingMode`](../gkmatchmakerviewcontroller/matchmakingmode.md) property instead.

## Declaration

```swift
var restrictToAutomatch: Bool { get set }
```

```objc
@property (assign) BOOL restrictToAutomatch;
```

## Discussion

Use this property to match the local player only with players who are also actively looking for a match. If [`true`](../../Swift/true.md), the local player can’t invite contacts, friends, or nearby players. The default value is [`false`](../../Swift/false.md).

## See Also

### Deprecated methods and properties
- [var inviteeResponseHandler: ((String, GKInviteeResponse) -> Void)?](./inviteeresponsehandler.md)
  Handles when a player responds to an invitation.
- [typealias GKInviteeResponse](../gkinviteeresponse.md)
  Possible responses from an invitation to a remote player.
- [var playersToInvite: [String]?](./playerstoinvite.md)
  A list of player identifiers for players to invite to the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchrequest/restricttoautomatch)*