# loadFriends(identifiedBy:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Loads the player’s friends list, scoped by the identifiers, if the player and their friends grant access.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.3+

## Declaration

```swift
func loadFriends(identifiedBy identifiers: [String], completionHandler: @escaping @Sendable ([GKPlayer]?, (any Error)?) -> Void)
```

```swift
func loadFriends(identifiedBy identifiers: [String]) async throws -> [GKPlayer]
```

```objc
- (void) loadFriendsWithIdentifiers:(NSArray<NSString *> *) identifiers completionHandler:(void (^)(NSArray<GKPlayer *> *friends, NSError *error)) completionHandler;
```

## Discussion

If the [`loadFriendsAuthorizationStatus(_:)`](./loadfriendsauthorizationstatus%28_%29.md) method returns [`GKFriendsAuthorizationStatus.notDetermined`](../gkfriendsauthorizationstatus/notdetermined.md), GameKit presents a prompt to the local player requesting access to the friends that may pause your game. GameKit displays the localized reason that you provide for the [`NSGKFriendListUsageDescription`](../../BundleResources/information-property-list/nsgkfriendlistusagedescription.md) key in the information property list.

If you loaded friends who no longer appear in the `friends` parameter of the completion handler, remove the data for those friends from your game because they no longer grant your game access to that data.

## Parameters

- `identifiers`: The game player IDs and team player IDs that GameKit uses to scope the friends that it passes to the completion handler.
- `completionHandler`: The block that GameKit calls when it completes the request.

  The block receives the following parameters:

  - **`friends`**: The player’s friends who also grant your game access to their friends and whose [`gamePlayerID`](../gkplayer/gameplayerid.md) or [`teamPlayerID`](../gkplayer/teamplayerid.md) property appears in the `identifiers` parameter.

  The local player and their friends’ authorization status must be [`GKFriendsAuthorizationStatus.authorized`](../gkfriendsauthorizationstatus/authorized.md).

  The local player and their friends must use a version of the game with the same bundle ID.

  - **`error`**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Accessing Friends and Recents
- [func loadFriendsAuthorizationStatus((GKFriendsAuthorizationStatus, (any Error)?) -> Void)](./loadfriendsauthorizationstatus%28_%29.md)
  Returns whether the player authorizes your game to access their friends list.
- [enum GKFriendsAuthorizationStatus](../gkfriendsauthorizationstatus.md)
  Constants that indicate if the local player grants access to their friends list.
- [func loadFriends(([GKPlayer]?, (any Error)?) -> Void)](./loadfriends%28_%29.md)
  Loads the local player’s friends list if the local player and their friends grant access.
- [NSGKFriendListUsageDescription](../../BundleResources/information-property-list/nsgkfriendlistusagedescription.md)
  A message that tells people why the app needs access to their Game Center friends list.
- [func loadChallengableFriends(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](./loadchallengablefriends%28completionhandler%29.md)
  Loads players to whom the local player can issue a challenge.
- [func loadRecentPlayers(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](./loadrecentplayers%28completionhandler%29.md)
  Loads players from the friends list or players that recently participated in a game with the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/loadfriends(identifiedby:completionhandler:))*