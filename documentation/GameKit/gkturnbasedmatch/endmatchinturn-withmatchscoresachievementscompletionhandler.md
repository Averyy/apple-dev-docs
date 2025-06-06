# endMatchInTurn(withMatch:scores:achievements:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Ends the match while submitting all of the scores and achievements.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func endMatchInTurn(withMatch matchData: Data, scores: [GKScore]?, achievements: [GKAchievement]?) async throws
```

#### Discussion

When this method is called, it creates a new background task to handle the request. The method then returns control to your game. Later, when the task is complete, Game Kit calls your completion handler. The completion handler is always called on the main thread.

This method ends the current match and submits scores and achievements for all of the participants. The scores can submitted to multiple leaderboards. The `GKTurnBasedMatchOutcome` status must be set for each participant before calling this method.

## Parameters

- `matchData`: A serialized blob of data reflecting the current state for the match. Do not pass   as an argument.
- `scores`: An array of   objects containing the final scores for every participant in the match.
- `achievements`: An array of   objects containing the achievements acquired by each participant in the match.
- `completionHandler`: The block receives the following parameters:

## See Also

- [func participantQuitInTurn(with: GKTurnBasedMatch.Outcome, nextParticipant: GKTurnBasedParticipant, match: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/participantquitinturn(with:nextparticipant:match:completionhandler:).md)
  Resigns the current player from the match without ending the match.
- [func endTurn(withNextParticipant: GKTurnBasedParticipant, match: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/endturn(withnextparticipant:match:completionhandler:).md)
  Updates the data stored on Game Center for the current match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/endmatchinturn(withmatch:scores:achievements:completionhandler:))*