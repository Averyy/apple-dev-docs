# acceptInvite(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Accepts an invitation for the local player to join a turn-based match.

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
func acceptInvite(completionHandler: (@Sendable (GKTurnBasedMatch?, (any Error)?) -> Void)? = nil)
```

```swift
func acceptInvite() async throws -> GKTurnBasedMatch
```

```objc
- (void) acceptInviteWithCompletionHandler:(void (^)(GKTurnBasedMatch *match, NSError *error)) completionHandler;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

When you provide a custom interface for managing matches, use this method to programmatically accept an invitation on behalf of the local player.

## Parameters

- `completionHandler`: The block that GameKit calls when it completes the request.

  The block receives the following parameters:

  - ***match***: The match for the player to join, or `nil` if an error occurs.
  - ***error***: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Creating a Match
- [class func find(for: GKMatchRequest, withCompletionHandler: (GKTurnBasedMatch?, (any Error)?) -> Void)](./find%28for,withcompletionhandler%29.md)
  Creates a new match or finds an existing match that needs a player.
- [func declineInvite(completionHandler: (((any Error)?) -> Void)?)](./declineinvite%28completionhandler%29.md)
  Declines an invitation for the local player to join a turn-based match.
- [func rematch(completionHandler: ((GKTurnBasedMatch?, (any Error)?) -> Void)?)](./rematch%28completionhandler%29.md)
  Creates a new turn-based match with the same participants from an existing match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/acceptinvite(completionhandler:))*