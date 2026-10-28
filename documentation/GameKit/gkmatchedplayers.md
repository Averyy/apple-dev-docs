# GKMatchedPlayers

**Framework**: GameKit  
**Kind**: class  
**Role**: Class

An object that represents matchmaking results, including the players that join the match and their properties that matchmaking rules uses.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+

## Declaration

```swift
class GKMatchedPlayers
```

```objc
@interface GKMatchedPlayers : NSObject
```

## Overview

If the [`properties`](./gkmatchedplayers/properties.md) and `playersProperties` properties are `nil`, Game Center didn’t use matchmaking rules to find the players. For more information, see [Matchmaking rules](./matchmaking-rules.md).

## Topics

### Getting players
- [var players: [GKPlayer]](./gkmatchedplayers/players.md)
  The players that join the match.
### Matchmaking using rules
- [var properties: [String : Any]?](./gkmatchedplayers/properties.md)
  The local player’s properties that matchmaking rules uses to find the players, with some additions.
- [var playerProperties: [GKPlayer : [String : Any]]?](./gkmatchedplayers/playerproperties.md)
  The properties for other players that matchmaking rules uses to find players, with some additions.
- [GKMatchProperties](./gkmatchproperties.md)
  A type for game-specific properties that Game Center uses to find players when using matchmaking rules.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Matching players
- [func findMatch(for: GKMatchRequest, withCompletionHandler: ((GKMatch?, (any Error)?) -> Void)?)](./gkmatchmaker/findmatch%28for,withcompletionhandler%29.md)
  Initiates a request to find players for a peer-to-peer match.
- [func findPlayers(forHostedRequest: GKMatchRequest, withCompletionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](./gkmatchmaker/findplayers%28forhostedrequest,withcompletionhandler%29.md)
  Initiates a request to find players for a hosted match.
- [func findMatchedPlayers(GKMatchRequest, withCompletionHandler: (GKMatchedPlayers?, (any Error)?) -> Void)](./gkmatchmaker/findmatchedplayers%28_,withcompletionhandler%29.md)
  Initiates a request to find players for a hosted match that uses matchmaking rules.
- [func addPlayers(to: GKMatch, matchRequest: GKMatchRequest, completionHandler: (((any Error)?) -> Void)?)](./gkmatchmaker/addplayers%28to,matchrequest,completionhandler%29.md)
  Invites additional players to an existing match.
- [func finishMatchmaking(for: GKMatch)](./gkmatchmaker/finishmatchmaking%28for%29.md)
  Informs the server when programmatic matchmaking finishes.
- [func cancel()](./gkmatchmaker/cancel%28%29.md)
  Cancels a matchmaking request.
- [func cancelPendingInvite(to: GKPlayer)](./gkmatchmaker/cancelpendinginvite%28to%29.md)
  Cancels a pending invitation to another player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchedplayers)*