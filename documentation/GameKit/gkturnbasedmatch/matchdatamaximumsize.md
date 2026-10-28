# matchDataMaximumSize

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The maximum size of the match data.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var matchDataMaximumSize: Int { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) NSUInteger matchDataMaximumSize;
```

*macOS*

```objc
@property (atomic, readonly) NSUInteger matchDataMaximumSize;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

## Discussion

An error occurs if your game sends match data that exceeds this limit.

## See Also

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
- [var matchData: Data?](./matchdata.md)
  The game-specific data that you store in Game Center and pass between participants through a match object.
- [func loadMatchData(completionHandler: ((Data?, (any Error)?) -> Void)?)](./loadmatchdata%28completionhandler%29.md)
  Fetches your game-specific data that you store in Game Center when ending a turn, saving a turn, or leaving a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/matchdatamaximumsize)*