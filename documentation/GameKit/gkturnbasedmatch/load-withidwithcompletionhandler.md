# load(withID:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method

Loads a specific match with the specified identifier.

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
class func load(withID matchID: String) async throws -> GKTurnBasedMatch
```

#### Discussion

The [`matchData`](gkturnbasedmatch/matchdata.md) property of the match object is `nil` until you fetch the data from Game Center using the [`loadMatchData(completionHandler:)`](gkturnbasedmatch/loadmatchdata(completionhandler:).md) method.

## Parameters

- `matchID`: The identifier for the turn-based match.
- `completionHandler`: The block receives the following parameters:

## See Also

- [class func loadMatches(completionHandler: (([GKTurnBasedMatch]?, (any Error)?) -> Void)?)](gkturnbasedmatch/loadmatches(completionhandler:).md)
  Fetches the turn-based matches from Game Center that the local player participates in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/load(withid:withcompletionhandler:))*