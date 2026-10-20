# matchData

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The game-specific data that you store in Game Center and pass between participants through a match object.

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
var matchData: Data? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nullable) NSData * matchData;
```

*macOS*

```objc
@property (atomic, strong, readonly, nullable) NSData * matchData;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

Use this property to get the game-specific data that you store in Game Center when ending a turn, saving a turn, or leaving a match. This property is `nil` until you fetch the data from Game Center using the [`loadMatchData(completionHandler:)`](./loadmatchdata%28completionhandler%29.md) method.

## See Also

### Related Documentation
- [func endTurn(withNextParticipant: GKTurnBasedParticipant, match: Data, completionHandler: (((any Error)?) -> Void)?)](./endturn%28withnextparticipant,match,completionhandler%29.md)
  Updates the data stored on Game Center for the current match.
- [func saveCurrentTurn(withMatch: Data, completionHandler: (((any Error)?) -> Void)?)](./savecurrentturn%28withmatch,completionhandler%29.md)
  Saves your match data in Game Center without ending the turn.
- [func participantQuitInTurn(with: GKTurnBasedMatch.Outcome, nextParticipant: GKTurnBasedParticipant, match: Data, completionHandler: (((any Error)?) -> Void)?)](./participantquitinturn%28with,nextparticipant,match,completionhandler%29.md)
  Resigns the current player from the match without ending the match.
### Retrieving Match Details
- [var matchID: String](./matchid.md)
  A unique identifier for the turn-based match.
- [var creationDate: Date](./creationdate.md)
  The date that Game Center created the match.
- [var participants: [GKTurnBasedParticipant]](./participants.md)
  The players that participate in a turn-based match.
- [var currentParticipant: GKTurnBasedParticipant?](./currentparticipant.md)
  The participant whose turn it is.
- [var status: GKTurnBasedMatch.Status](./status-swift.property.md)
  The state of the match, such as whether the match is open or has ended.
- [GKTurnBasedMatch.Status](./status-swift.enum.md)
  The states of a match from when it’s created to when it ends.
- [var matchDataMaximumSize: Int](./matchdatamaximumsize.md)
  The maximum size of the match data.
- [func loadMatchData(completionHandler: ((Data?, (any Error)?) -> Void)?)](./loadmatchdata%28completionhandler%29.md)
  Fetches your game-specific data that you store in Game Center when ending a turn, saving a turn, or leaving a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/matchdata)*