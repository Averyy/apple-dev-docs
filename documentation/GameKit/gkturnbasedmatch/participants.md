# participants

**Framework**: GameKit  
**Kind**: property

The players that participate in a turn-based match.

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
var participants: [GKTurnBasedParticipant] { get }
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

Use the objects in this array to show more information about the participants in your interface, such as their names, avatars, status, and outcomes. The size of the array and order of the participants remains the same throughout the match.

When you end a player’s turn or quit a match, choose the next participant from this array. If a participant represents an unfilled slot, it’s [`status`](gkturnbasedparticipant/status-swift.property.md) property is [`GKTurnBasedParticipant.Status.matching`](gkturnbasedparticipant/status-swift.enum/matching.md). Game Center searches for a player to fill that spot only when you choose that participant as the next participant.

## See Also

- [func endTurn(withNextParticipants: [GKTurnBasedParticipant], turnTimeout: TimeInterval, match: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/endturn(withnextparticipants:turntimeout:match:completionhandler:).md)
  Passes the turn from the current participant to the next participant.
- [func participantQuitInTurn(with: GKTurnBasedMatch.Outcome, nextParticipants: [GKTurnBasedParticipant], turnTimeout: TimeInterval, match: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/participantquitinturn(with:nextparticipants:turntimeout:match:completionhandler:).md)
  Forfeits the match on behalf of the local player when it’s their turn.
- [var matchID: String](gkturnbasedmatch/matchid.md)
  A unique identifier for the turn-based match.
- [var creationDate: Date](gkturnbasedmatch/creationdate.md)
  The date that Game Center created the match.
- [var currentParticipant: GKTurnBasedParticipant?](gkturnbasedmatch/currentparticipant.md)
  The participant whose turn it is.
- [var status: GKTurnBasedMatch.Status](gkturnbasedmatch/status-swift.property.md)
  The state of the match, such as whether the match is open or has ended.
- [GKTurnBasedMatch.Status](gkturnbasedmatch/status-swift.enum.md)
  The states of a match from when it’s created to when it ends.
- [var matchData: Data?](gkturnbasedmatch/matchdata.md)
  The game-specific data that you store in Game Center and pass between participants through a match object.
- [var matchDataMaximumSize: Int](gkturnbasedmatch/matchdatamaximumsize.md)
  The maximum size of the match data.
- [func loadMatchData(completionHandler: ((Data?, (any Error)?) -> Void)?)](gkturnbasedmatch/loadmatchdata(completionhandler:).md)
  Fetches your game-specific data that you store in Game Center when ending a turn, saving a turn, or leaving a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/participants)*