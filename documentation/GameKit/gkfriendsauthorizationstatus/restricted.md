# GKFriendsAuthorizationStatus.restricted

**Framework**: GameKit  
**Kind**: case

Access to the player’s list of friends restricted.

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
case restricted
```

## Mentions

- [Connecting players with their friends in your game](connecting-players-with-their-friends-in-your-game.md)

#### Discussion

While GameKit restricts access to a player’s friends’ data, the player can’t change the authorization status. If you previously loaded the player’s friends, delete the friends’ data from your game.

## See Also

- [GKFriendsAuthorizationStatus.authorized](gkfriendsauthorizationstatus/authorized.md)
  The player authorized your game to access their list of friends.
- [GKFriendsAuthorizationStatus.denied](gkfriendsauthorizationstatus/denied.md)
  Access to the player’s friends’ data denied.
- [GKFriendsAuthorizationStatus.notDetermined](gkfriendsauthorizationstatus/notdetermined.md)
  The player hasn’t choosen whether your game may access their friends list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendsauthorizationstatus/restricted)*