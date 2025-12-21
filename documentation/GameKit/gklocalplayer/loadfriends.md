# loadFriends(_:)

**Framework**: GameKit  
**Kind**: method

Loads the local player’s friends list if the local player and their friends grant access.

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
func loadFriends() async throws -> [GKPlayer]
```

## Mentions

- [Protecting the player’s privacy using scoped identifiers](protecting-the-player-s-privacy-using-scoped-identifiers.md)
- [Connecting players with their friends in your game](connecting-players-with-their-friends-in-your-game.md)

#### Discussion

If the [`loadFriendsAuthorizationStatus(_:)`](gklocalplayer/loadfriendsauthorizationstatus(_:).md) method returns [`GKFriendsAuthorizationStatus.notDetermined`](gkfriendsauthorizationstatus/notdetermined.md), GameKit presents a prompt to the local player requesting access to their friends that may pause your game. GameKit displays the localized reason that you provide for the [`NSGKFriendListUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSGKFriendListUsageDescription) key in the information property list.

If you loaded friends who no longer appear in the `friends` parameter of the completion handler, remove the data for those friends from your game because they no longer grant your game access to that data.

## Parameters

- `completionHandler`: The local player and their friends must use a version of your game with the same bundle ID.

## See Also

- [func loadFriendsAuthorizationStatus((GKFriendsAuthorizationStatus, (any Error)?) -> Void)](gklocalplayer/loadfriendsauthorizationstatus(_:).md)
  Returns whether the player authorizes your game to access their friends list.
- [enum GKFriendsAuthorizationStatus](gkfriendsauthorizationstatus.md)
  Constants that indicate if the local player grants access to their friends list.
- [func loadFriends(identifiedBy: [String], completionHandler: ([GKPlayer]?, (any Error)?) -> Void)](gklocalplayer/loadfriends(identifiedby:completionhandler:).md)
  Loads the player’s friends list, scoped by the identifiers, if the player and their friends grant access.
- [NSGKFriendListUsageDescription](../BundleResources/Information-Property-List/NSGKFriendListUsageDescription.md)
  A message that tells people why the app needs access to their Game Center friends list.
- [func loadChallengableFriends(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gklocalplayer/loadchallengablefriends(completionhandler:).md)
  Loads players to whom the local player can issue a challenge.
- [func loadRecentPlayers(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gklocalplayer/loadrecentplayers(completionhandler:).md)
  Loads players from the friends list or players that recently participated in a game with the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/loadfriends(_:))*