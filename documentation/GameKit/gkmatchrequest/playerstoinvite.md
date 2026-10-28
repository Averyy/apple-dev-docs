# playersToInvite

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A list of player identifiers for players to invite to the match.

**Availability**:
- iOS 4.1+ - Deprecated in 8.0
- iPadOS 4.1+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`recipients`](./recipients.md) property instead.

## Declaration

```swift
var playersToInvite: [String]? { get set }
```

```objc
@property (retain, nullable) NSArray<NSString *> * playersToInvite;
```

## Discussion

The property holds an array of [`NSString`](../../Foundation/nsstring.md) objects, each of which is an identifier for a player on Game Center. If the value of the property is non-`nil`, when you use the request to create a match, Game Center invites those players to the match. No automatching is done and the [`GKMatchRequest`](../gkmatchrequest.md) `maxPlayers` and `minPlayers` properties are ignored. If `nil` (the default), no players are invited. The exact behavior for matchmaking depends on the kind of match being created and the class used to create the match.

## See Also

### Deprecated methods and properties
- [var inviteeResponseHandler: ((String, GKInviteeResponse) -> Void)?](./inviteeresponsehandler.md)
  Handles when a player responds to an invitation.
- [typealias GKInviteeResponse](../gkinviteeresponse.md)
  Possible responses from an invitation to a remote player.
- [var restrictToAutomatch: Bool](./restricttoautomatch.md)
  A Boolean value that determines whether a game uses automatch to find players or the local player invites players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchrequest/playerstoinvite)*