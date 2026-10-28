# declineInvite(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Declines an invitation for the local player to join a turn-based match.

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
func declineInvite(completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func declineInvite() async throws
```

```objc
- (void) declineInviteWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

## Discussion

When you provide a custom interface for managing matches, use this method to programmatically decline an invitation on behalf of the local player.

## Parameters

- `completionHandler`: The block that GameKit calls when it completes the request.

  The block receives the following parameter:

  - ***error***: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Creating a Match
- [class func find(for: GKMatchRequest, withCompletionHandler: (GKTurnBasedMatch?, (any Error)?) -> Void)](./find%28for,withcompletionhandler%29.md)
  Creates a new match or finds an existing match that needs a player.
- [func acceptInvite(completionHandler: ((GKTurnBasedMatch?, (any Error)?) -> Void)?)](./acceptinvite%28completionhandler%29.md)
  Accepts an invitation for the local player to join a turn-based match.
- [func rematch(completionHandler: ((GKTurnBasedMatch?, (any Error)?) -> Void)?)](./rematch%28completionhandler%29.md)
  Creates a new turn-based match with the same participants from an existing match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/declineinvite(completionhandler:))*