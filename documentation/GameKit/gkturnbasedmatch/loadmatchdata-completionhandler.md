# loadMatchData(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Fetches your game-specific data that you store in Game Center when ending a turn, saving a turn, or leaving a match.

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
func loadMatchData() async throws -> Data?
```

#### Discussion

The [`matchData`](gkturnbasedmatch/matchdata.md) property is `nil` until you fetch the data from Game Center using this method.

## Parameters

- `completionHandler`: The block receives the following parameters:

## See Also

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
- [var matchData: Data?](gkturnbasedmatch/matchdata.md)
  The game-specific data that you store in Game Center and pass between participants through a match object.
- [var matchDataMaximumSize: Int](gkturnbasedmatch/matchdatamaximumsize.md)
  The maximum size of the match data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/loadmatchdata(completionhandler:))*