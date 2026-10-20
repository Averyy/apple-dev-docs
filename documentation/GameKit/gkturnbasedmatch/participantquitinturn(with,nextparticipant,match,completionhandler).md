# participantQuitInTurn(with:nextParticipant:match:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Resigns the current player from the match without ending the match.

**Availability**:
- iOS 5.0+ - Deprecated in 6.0
- iPadOS 5.0+ - Deprecated in 6.0
- Mac Catalyst 5.0+ - Deprecated in 6.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use the  [`participantQuitInTurn(with:nextParticipants:turnTimeout:match:completionHandler:)`](./participantquitinturn%28with,nextparticipants,turntimeout,match,completionhandler%29.md) method instead.

## Declaration

*visionOS, watchOS*

```swift
func participantQuitInTurn(with matchOutcome: GKTurnBasedMatch.Outcome, nextParticipant: GKTurnBasedParticipant, match matchData: Data, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

*visionOS*

```swift
func participantQuitInTurn(with matchOutcome: GKTurnBasedMatch.Outcome, nextParticipant: GKTurnBasedParticipant, match matchData: Data) async throws
```

```objc
- (void) participantQuitInTurnWithOutcome:(GKTurnBasedMatchOutcome) matchOutcome nextParticipant:(GKTurnBasedParticipant *) nextParticipant matchData:(NSData *) matchData completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

Your game calls this method on an instance of your game that is processing the current player’s turn, but that player has left the match. For example, the player may have willingly resigned from the match or that player may have been eliminated by the other players (based on your game’s internal logic).

When this method is called, it creates a new background task to handle the request. The method then returns control to your game. Later, when the task is complete, Game Kit calls your completion handler. The completion handler is always called on the main thread.

## Parameters

- `matchOutcome`: The end outcome of the current player in the match. Do not pass `nil` as an argument.
- `nextParticipant`: The next player in the match who needs to take an action. It must be one of the object’s stored in the match’s [`participants`](./participants.md) property.
- `matchData`: A serialized blob of data reflecting the game-specific state for the match.
- `completionHandler`: A block to be called after the data is uploaded to the server.

  The block receives the following parameters:

  - ***error***: If an error occurred, this error object describes the error. If the operation was completed successfully, the value is `nil`.

## See Also

### Deprecated Methods
- [func endMatchInTurn(withMatch: Data, scores: [GKScore]?, achievements: [GKAchievement]?, completionHandler: (((any Error)?) -> Void)?)](./endmatchinturn%28withmatch,scores,achievements,completionhandler%29.md)
  Ends the match while submitting all of the scores and achievements.
- [func endTurn(withNextParticipant: GKTurnBasedParticipant, match: Data, completionHandler: (((any Error)?) -> Void)?)](./endturn%28withnextparticipant,match,completionhandler%29.md)
  Updates the data stored on Game Center for the current match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/participantquitinturn(with:nextparticipant:match:completionhandler:))*