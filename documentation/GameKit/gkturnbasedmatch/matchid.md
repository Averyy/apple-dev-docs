# matchID

**Framework**: GameKit  
**Kind**: property

A unique identifier for the turn-based match.

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
var matchID: String { get }
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

To get the current match object during gameplay, save the match ID and pass it to the [`load(withID:withCompletionHandler:)`](gkturnbasedmatch/load(withid:withcompletionhandler:).md) method.

## See Also

- [var creationDate: Date](gkturnbasedmatch/creationdate.md)
  The date that Game Center created the match.
- [var participants: [GKTurnBasedParticipant]](gkturnbasedmatch/participants.md)
  The players that participate in a turn-based match.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/matchid)*