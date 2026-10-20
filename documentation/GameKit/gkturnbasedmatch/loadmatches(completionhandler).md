# loadMatches(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

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
class func loadMatches(completionHandler: (@Sendable ([GKTurnBasedMatch]?, (any Error)?) -> Void)? = nil)
```

```swift
class func loadMatches() async throws -> [GKTurnBasedMatch]
```

```objc
+ (void) loadMatchesWithCompletionHandler:(void (^)(NSArray<GKTurnBasedMatch *> *matches, NSError *error)) completionHandler;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

The [`matchData`](./matchdata.md) properties of the match objects are `nil` until you fetch the data from Game Center using the [`loadMatchData(completionHandler:)`](./loadmatchdata%28completionhandler%29.md) method.

## Parameters

- `completionHandler`: The block that GameKit calls when it completes the request.

  The block receives the following parameters:

  - ***matches***: The local player’s matches, or `nil` if there are none. If an error occurs, this parameter may be non-`nil`, containing a subset of the matches that GameKit loads before the error occurs.
  - ***error***: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Loading Existing Matches
- [class func load(withID: String, withCompletionHandler: ((GKTurnBasedMatch?, (any Error)?) -> Void)?)](./load%28withid,withcompletionhandler%29.md)
  Loads a specific match with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/loadmatches(completionhandler:))*