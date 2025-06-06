# participantQuitInTurn(with:nextParticipant:match:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Resigns the current player from the match without ending the match.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func participantQuitInTurn(with matchOutcome: GKTurnBasedMatch.Outcome, nextParticipant: GKTurnBasedParticipant, match matchData: Data) async throws
```

#### Discussion

Your game calls this method on an instance of your game that is processing the current player’s turn, but that player has left the match. For example, the player may have willingly resigned from the match or that player may have been eliminated by the other players (based on your game’s internal logic).

When this method is called, it creates a new background task to handle the request. The method then returns control to your game. Later, when the task is complete, Game Kit calls your completion handler. The completion handler is always called on the main thread.

## Parameters

- `matchOutcome`: The end outcome of the current player in the match. Do not pass   as an argument.
- `nextParticipant`: The next player in the match who needs to take an action. It must be one of the object’s stored in the match’s   property.
- `matchData`: A serialized blob of data reflecting the game-specific state for the match.
- `completionHandler`: The block receives the following parameters:

## See Also

- [func endMatchInTurn(withMatch: Data, scores: [GKScore]?, achievements: [GKAchievement]?, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/endmatchinturn(withmatch:scores:achievements:completionhandler:).md)
  Ends the match while submitting all of the scores and achievements.
- [func endTurn(withNextParticipant: GKTurnBasedParticipant, match: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/endturn(withnextparticipant:match:completionhandler:).md)
  Updates the data stored on Game Center for the current match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/participantquitinturn(with:nextparticipant:match:completionhandler:))*