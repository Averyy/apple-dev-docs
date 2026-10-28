# participants

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nullable) NSArray<GKTurnBasedParticipant *> * participants;
```

*macOS*

```objc
@property (atomic, strong, readonly, nullable) NSArray<GKTurnBasedParticipant *> * participants;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

## Discussion

Use the objects in this array to show more information about the participants in your interface, such as their names, avatars, status, and outcomes. The size of the array and order of the participants remains the same throughout the match.

When you end a player’s turn or quit a match, choose the next participant from this array. If a participant represents an unfilled slot, it’s [`status`](../gkturnbasedparticipant/status-swift.property.md) property is [`GKTurnBasedParticipant.Status.matching`](../gkturnbasedparticipant/status-swift.enum/matching.md). Game Center searches for a player to fill that spot only when you choose that participant as the next participant.

## See Also

### Related Documentation
- [func endTurn(withNextParticipants: [GKTurnBasedParticipant], turnTimeout: TimeInterval, match: Data, completionHandler: (((any Error)?) -> Void)?)](./endturn%28withnextparticipants,turntimeout,match,completionhandler%29.md)
  Passes the turn from the current participant to the next participant.
- [func participantQuitInTurn(with: GKTurnBasedMatch.Outcome, nextParticipants: [GKTurnBasedParticipant], turnTimeout: TimeInterval, match: Data, completionHandler: (((any Error)?) -> Void)?)](./participantquitinturn%28with,nextparticipants,turntimeout,match,completionhandler%29.md)
  Forfeits the match on behalf of the local player when it’s their turn.
### Retrieving Match Details
- [var matchID: String](./matchid.md)
  A unique identifier for the turn-based match.
- [var creationDate: Date](./creationdate.md)
  The date that Game Center created the match.
- [var currentParticipant: GKTurnBasedParticipant?](./currentparticipant.md)
  The participant whose turn it is.
- [var status: GKTurnBasedMatch.Status](./status-swift.property.md)
  The state of the match, such as whether the match is open or has ended.
- [GKTurnBasedMatch.Status](./status-swift.enum.md)
  The states of a match from when it’s created to when it ends.
- [var matchData: Data?](./matchdata.md)
  The game-specific data that you store in Game Center and pass between participants through a match object.
- [var matchDataMaximumSize: Int](./matchdatamaximumsize.md)
  The maximum size of the match data.
- [func loadMatchData(completionHandler: ((Data?, (any Error)?) -> Void)?)](./loadmatchdata%28completionhandler%29.md)
  Fetches your game-specific data that you store in Game Center when ending a turn, saving a turn, or leaving a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/participants)*