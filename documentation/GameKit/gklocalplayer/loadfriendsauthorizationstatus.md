# loadFriendsAuthorizationStatus(_:)

**Framework**: GameKit  
**Kind**: method

Returns whether the player authorizes your game to access their friends list.

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
func loadFriendsAuthorizationStatus() async throws -> GKFriendsAuthorizationStatus
```

## Mentions

- [Connecting players with their friends in your game](connecting-players-with-their-friends-in-your-game.md)

## Parameters

- `completionHandler`: The block that GameKit calls when it completes the request. The block receives the following parameters: - **`authorizationStatus`**: A status that indicates if the player authorized or denied your game access to their friends list.
- **`error`**: Describes an error if it occurs, or `nil` if the operation completes. An error occurs if you don’t add the [`NSGKFriendListUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsgkfriendlistusagedescription) key to the information property list file.

## See Also

- [enum GKFriendsAuthorizationStatus](gkfriendsauthorizationstatus.md)
  Constants that indicate if the local player grants access to their friends list.
- [func loadFriends(([GKPlayer]?, (any Error)?) -> Void)](gklocalplayer/loadfriends(_:).md)
  Loads the local player’s friends list if the local player and their friends grant access.
- [func loadFriends(identifiedBy: [String], completionHandler: ([GKPlayer]?, (any Error)?) -> Void)](gklocalplayer/loadfriends(identifiedby:completionhandler:).md)
  Loads the player’s friends list, scoped by the identifiers, if the player and their friends grant access.
- [NSGKFriendListUsageDescription](../bundleresources/information-property-list/nsgkfriendlistusagedescription.md)
  A message that tells people why the app needs access to their Game Center friends list.
- [func loadChallengableFriends(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gklocalplayer/loadchallengablefriends(completionhandler:).md)
  Loads players to whom the local player can issue a challenge.
- [func loadRecentPlayers(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gklocalplayer/loadrecentplayers(completionhandler:).md)
  Loads players from the friends list or players that recently participated in a game with the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/loadfriendsauthorizationstatus(_:))*