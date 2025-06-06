# endTurn(withNextParticipant:match:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Updates the data stored on Game Center for the current match.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func endTurn(withNextParticipant nextParticipant: GKTurnBasedParticipant, match matchData: Data) async throws
```

#### Discussion

When this method is called, it creates a new background task to handle the request. The method then returns control to your game. Later, when the task is complete, Game Kit calls your completion handler. The completion handler is always called on the main thread.

## Parameters

- `nextParticipant`: The next player in the match who needs to take an action. It must be one of the object’s stored in the match’s   property.
- `matchData`: A serialized blob of data reflecting the game-specific state for the match. Do not pass   as an argument.
- `completionHandler`: The block receives the following parameters:

## See Also

- [func participantQuitInTurn(with: GKTurnBasedMatch.Outcome, nextParticipant: GKTurnBasedParticipant, match: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/participantquitinturn(with:nextparticipant:match:completionhandler:).md)
  Resigns the current player from the match without ending the match.
- [func endMatchInTurn(withMatch: Data, scores: [GKScore]?, achievements: [GKAchievement]?, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/endmatchinturn(withmatch:scores:achievements:completionhandler:).md)
  Ends the match while submitting all of the scores and achievements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/endturn(withnextparticipant:match:completionhandler:))*