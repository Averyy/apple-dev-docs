# loadMatches(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Fetches the turn-based matches from Game Center that the local player participates in.

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
class func loadMatches() async throws -> [GKTurnBasedMatch]
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

The [`matchData`](gkturnbasedmatch/matchdata.md) properties of the match objects are `nil` until you fetch the data from Game Center using the [`loadMatchData(completionHandler:)`](gkturnbasedmatch/loadmatchdata(completionhandler:).md) method.

## Parameters

- `completionHandler`: The block receives the following parameters:

## See Also

- [class func load(withID: String, withCompletionHandler: ((GKTurnBasedMatch?, (any Error)?) -> Void)?)](gkturnbasedmatch/load(withid:withcompletionhandler:).md)
  Loads a specific match with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/loadmatches(completionhandler:))*