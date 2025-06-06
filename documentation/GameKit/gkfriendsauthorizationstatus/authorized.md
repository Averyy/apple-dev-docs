# GKFriendsAuthorizationStatus.authorized

**Framework**: GameKit  
**Kind**: case

The player authorized your game to access their list of friends.

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
case authorized
```

## Mentions

- [Connecting players with their friends in your game](connecting-players-with-their-friends-in-your-game.md)

#### Discussion

If the [`loadFriendsAuthorizationStatus(_:)`](gklocalplayer/loadfriendsauthorizationstatus(_:).md) method returns `GKFriendsAuthorizationStatus.authorized`, the [`loadFriends(identifiedBy:completionHandler:)`](gklocalplayer/loadfriends(identifiedby:completionhandler:).md) method passes the friends list to the completion handler.

## See Also

- [GKFriendsAuthorizationStatus.denied](gkfriendsauthorizationstatus/denied.md)
  Access to the player’s friends’ data denied.
- [GKFriendsAuthorizationStatus.notDetermined](gkfriendsauthorizationstatus/notdetermined.md)
  The player hasn’t choosen whether your game may access their friends list.
- [GKFriendsAuthorizationStatus.restricted](gkfriendsauthorizationstatus/restricted.md)
  Access to the player’s list of friends restricted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendsauthorizationstatus/authorized)*