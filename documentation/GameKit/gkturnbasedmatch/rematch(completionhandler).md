# rematch(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Creates a new turn-based match with the same participants from an existing match.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func rematch(completionHandler: (@Sendable (GKTurnBasedMatch?, (any Error)?) -> Void)? = nil)
```

```swift
func rematch() async throws -> GKTurnBasedMatch
```

```objc
- (void) rematchWithCompletionHandler:(void (^)(GKTurnBasedMatch *match, NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: The block that GameKit calls when it completes the request.

  The block receives the following parameters:

  - ***match***: A new match, or `nil` if an error occurs.
  - ***error***: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Creating a Match
- [class func find(for: GKMatchRequest, withCompletionHandler: (GKTurnBasedMatch?, (any Error)?) -> Void)](./find%28for,withcompletionhandler%29.md)
  Creates a new match or finds an existing match that needs a player.
- [func acceptInvite(completionHandler: ((GKTurnBasedMatch?, (any Error)?) -> Void)?)](./acceptinvite%28completionhandler%29.md)
  Accepts an invitation for the local player to join a turn-based match.
- [func declineInvite(completionHandler: (((any Error)?) -> Void)?)](./declineinvite%28completionhandler%29.md)
  Declines an invitation for the local player to join a turn-based match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/rematch(completionhandler:))*