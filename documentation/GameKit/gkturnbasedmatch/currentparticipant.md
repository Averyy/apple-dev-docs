# currentParticipant

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The participant whose turn it is.

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
var currentParticipant: GKTurnBasedParticipant? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nullable) GKTurnBasedParticipant * currentParticipant;
```

*macOS*

```objc
@property (atomic, strong, readonly, nullable) GKTurnBasedParticipant * currentParticipant;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

You can only update the match data when the current participant is the local player.

## See Also

### Retrieving Match Details
- [var matchID: String](./matchid.md)
  A unique identifier for the turn-based match.
- [var creationDate: Date](./creationdate.md)
  The date that Game Center created the match.
- [var participants: [GKTurnBasedParticipant]](./participants.md)
  The players that participate in a turn-based match.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/currentparticipant)*