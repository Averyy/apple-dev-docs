# GKFriendsAuthorizationStatus

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate if the local player grants access to their friends list.

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
enum GKFriendsAuthorizationStatus
```

```c
enum GKFriendsAuthorizationStatus : NSInteger;
```

## Topics

### Authorization Statuses
- [GKFriendsAuthorizationStatus.authorized](./gkfriendsauthorizationstatus/authorized.md)
  The player authorized your game to access their list of friends.
- [GKFriendsAuthorizationStatus.denied](./gkfriendsauthorizationstatus/denied.md)
  Access to the player’s friends’ data denied.
- [GKFriendsAuthorizationStatus.notDetermined](./gkfriendsauthorizationstatus/notdetermined.md)
  The player hasn’t choosen whether your game may access their friends list.
- [GKFriendsAuthorizationStatus.restricted](./gkfriendsauthorizationstatus/restricted.md)
  Access to the player’s list of friends restricted.
### Initializers
- [init?(rawValue: Int)](./gkfriendsauthorizationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing Friends and Recents
- [func loadFriendsAuthorizationStatus((GKFriendsAuthorizationStatus, (any Error)?) -> Void)](./gklocalplayer/loadfriendsauthorizationstatus%28_%29.md)
  Returns whether the player authorizes your game to access their friends list.
- [func loadFriends(([GKPlayer]?, (any Error)?) -> Void)](./gklocalplayer/loadfriends%28_%29.md)
  Loads the local player’s friends list if the local player and their friends grant access.
- [func loadFriends(identifiedBy: [String], completionHandler: ([GKPlayer]?, (any Error)?) -> Void)](./gklocalplayer/loadfriends%28identifiedby,completionhandler%29.md)
  Loads the player’s friends list, scoped by the identifiers, if the player and their friends grant access.
- [NSGKFriendListUsageDescription](../BundleResources/information-property-list/nsgkfriendlistusagedescription.md)
  A message that tells people why the app needs access to their Game Center friends list.
- [func loadChallengableFriends(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](./gklocalplayer/loadchallengablefriends%28completionhandler%29.md)
  Loads players to whom the local player can issue a challenge.
- [func loadRecentPlayers(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](./gklocalplayer/loadrecentplayers%28completionhandler%29.md)
  Loads players from the friends list or players that recently participated in a game with the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendsauthorizationstatus)*