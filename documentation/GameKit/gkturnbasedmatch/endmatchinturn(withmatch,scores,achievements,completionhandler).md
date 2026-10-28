# endMatchInTurn(withMatch:scores:achievements:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Ends the match while submitting all of the scores and achievements.

**Availability**:
- iOS 6.0+ - Deprecated in 14.0
- iPadOS 6.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.10+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 7.0

> **Deprecated**: Use the [`endMatchInTurn(withMatch:scores:achievements:completionHandler:)`](./endmatchinturn%28withmatch,scores,achievements,completionhandler%29.md) method instead.

## Declaration

```swift
func endMatchInTurn(withMatch matchData: Data, scores: [GKScore]?, achievements: [GKAchievement]?, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func endMatchInTurn(withMatch matchData: Data, scores: [GKScore]?, achievements: [GKAchievement]?) async throws
```

```objc
- (void) endMatchInTurnWithMatchData:(NSData *) matchData scores:(NSArray<GKScore *> *) scores achievements:(NSArray<GKAchievement *> *) achievements completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

When this method is called, it creates a new background task to handle the request. The method then returns control to your game. Later, when the task is complete, Game Kit calls your completion handler. The completion handler is always called on the main thread.

This method ends the current match and submits scores and achievements for all of the participants. The scores can submitted to multiple leaderboards. The `GKTurnBasedMatchOutcome` status must be set for each participant before calling this method.

## Parameters

- `matchData`: A serialized blob of data reflecting the current state for the match. Do not pass `nil` as an argument.
- `scores`: An array of `GKScore` objects containing the final scores for every participant in the match.
- `achievements`: An array of `GKAchievement` objects containing the achievements acquired by each participant in the match.
- `completionHandler`: A block to be called after the scores are saved to the server.

  The block receives the following parameters:

  - ***error***: If an error occurred, this error object describes the error. If the operation was completed successfully, the value is `nil`.

## See Also

### Deprecated Methods
- [func participantQuitInTurn(with: GKTurnBasedMatch.Outcome, nextParticipant: GKTurnBasedParticipant, match: Data, completionHandler: (((any Error)?) -> Void)?)](./participantquitinturn%28with,nextparticipant,match,completionhandler%29.md)
  Resigns the current player from the match without ending the match.
- [func endTurn(withNextParticipant: GKTurnBasedParticipant, match: Data, completionHandler: (((any Error)?) -> Void)?)](./endturn%28withnextparticipant,match,completionhandler%29.md)
  Updates the data stored on Game Center for the current match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/endmatchinturn(withmatch:scores:achievements:completionhandler:))*