# loadMatchData(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

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
func loadMatchData(completionHandler: (@Sendable (Data?, (any Error)?) -> Void)? = nil)
```

```swift
func loadMatchData() async throws -> Data?
```

```objc
- (void) loadMatchDataWithCompletionHandler:(void (^)(NSData *matchData, NSError *error)) completionHandler;
```

## Discussion

The [`matchData`](./matchdata.md) property is `nil` until you fetch the data from Game Center using this method.

## Parameters

- `completionHandler`: The block that GameKit calls when it completes the request.

  The block receives the following parameters:

  - ***matchData***: The match data you pass to `GKTurnBasedMatch` methods that GameKit stores in Game Center, or `nil` if an error occurs.
  - ***error***: Describes an error if it occurs, or `nil` if the operation completes.

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
- [var matchDataMaximumSize: Int](./matchdatamaximumsize.md)
  The maximum size of the match data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/loadmatchdata(completionhandler:))*