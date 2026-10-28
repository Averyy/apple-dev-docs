# endTurn(withNextParticipant:match:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Updates the data stored on Game Center for the current match.

**Availability**:
- iOS 5.0+ - Deprecated in 6.0
- iPadOS 5.0+ - Deprecated in 6.0
- Mac Catalyst 5.0+ - Deprecated in 6.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use the [`endTurn(withNextParticipants:turnTimeout:match:completionHandler:)`](./endturn%28withnextparticipants,turntimeout,match,completionhandler%29.md) method instead.

## Declaration

*visionOS, watchOS*

```swift
func endTurn(withNextParticipant nextParticipant: GKTurnBasedParticipant, match matchData: Data, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

*visionOS*

```swift
func endTurn(withNextParticipant nextParticipant: GKTurnBasedParticipant, match matchData: Data) async throws
```

```objc
- (void) endTurnWithNextParticipant:(GKTurnBasedParticipant *) nextParticipant matchData:(NSData *) matchData completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

When this method is called, it creates a new background task to handle the request. The method then returns control to your game. Later, when the task is complete, Game Kit calls your completion handler. The completion handler is always called on the main thread.

## Parameters

- `nextParticipant`: The next player in the match who needs to take an action. It must be one of the object’s stored in the match’s [`participants`](./participants.md) property.
- `matchData`: A serialized blob of data reflecting the game-specific state for the match. Do not pass `nil` as an argument.
- `completionHandler`: A block to be called after the data is uploaded to Game Center.

  The block receives the following parameters:

  - ***error***: If an error occurred, this error object describes the error. If the operation was completed successfully, the value is `nil`.

## See Also

### Deprecated Methods
- [func participantQuitInTurn(with: GKTurnBasedMatch.Outcome, nextParticipant: GKTurnBasedParticipant, match: Data, completionHandler: (((any Error)?) -> Void)?)](./participantquitinturn%28with,nextparticipant,match,completionhandler%29.md)
  Resigns the current player from the match without ending the match.
- [func endMatchInTurn(withMatch: Data, scores: [GKScore]?, achievements: [GKAchievement]?, completionHandler: (((any Error)?) -> Void)?)](./endmatchinturn%28withmatch,scores,achievements,completionhandler%29.md)
  Ends the match while submitting all of the scores and achievements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/endturn(withnextparticipant:match:completionhandler:))*