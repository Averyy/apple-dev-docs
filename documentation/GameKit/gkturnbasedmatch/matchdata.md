# matchData

**Framework**: GameKit  
**Kind**: property

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

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

Use this property to get the game-specific data that you store in Game Center when ending a turn, saving a turn, or leaving a match. This property is `nil` until you fetch the data from Game Center using the [`loadMatchData(completionHandler:)`](gkturnbasedmatch/loadmatchdata(completionhandler:).md) method.

## See Also

- [func endTurn(withNextParticipant: GKTurnBasedParticipant, match: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/endturn(withnextparticipant:match:completionhandler:).md)
  Updates the data stored on Game Center for the current match.
- [func saveCurrentTurn(withMatch: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/savecurrentturn(withmatch:completionhandler:).md)
  Saves your match data in Game Center without ending the turn.
- [func participantQuitInTurn(with: GKTurnBasedMatch.Outcome, nextParticipant: GKTurnBasedParticipant, match: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/participantquitinturn(with:nextparticipant:match:completionhandler:).md)
  Resigns the current player from the match without ending the match.
- [var matchID: String](gkturnbasedmatch/matchid.md)
  A unique identifier for the turn-based match.
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
- [var matchDataMaximumSize: Int](gkturnbasedmatch/matchdatamaximumsize.md)
  The maximum size of the match data.
- [func loadMatchData(completionHandler: ((Data?, (any Error)?) -> Void)?)](gkturnbasedmatch/loadmatchdata(completionhandler:).md)
  Fetches your game-specific data that you store in Game Center when ending a turn, saving a turn, or leaving a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/matchdata)*