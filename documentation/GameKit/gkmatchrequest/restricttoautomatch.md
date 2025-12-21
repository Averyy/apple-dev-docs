# restrictToAutomatch

**Framework**: GameKit  
**Kind**: property

A Boolean value that determines whether a game uses automatch to find players or the local player invites players.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var restrictToAutomatch: Bool { get set }
```

#### Discussion

Use this property to match the local player only with players who are also actively looking for a match. If [`true`](https://developer.apple.com/documentation/Swift/true), the local player can’t invite contacts, friends, or nearby players. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var inviteeResponseHandler: ((String, GKInviteeResponse) -> Void)?](gkmatchrequest/inviteeresponsehandler.md)
  Handles when a player responds to an invitation.
- [typealias GKInviteeResponse](gkinviteeresponse.md)
  Possible responses from an invitation to a remote player.
- [var playersToInvite: [String]?](gkmatchrequest/playerstoinvite.md)
  A list of player identifiers for players to invite to the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchrequest/restricttoautomatch)*