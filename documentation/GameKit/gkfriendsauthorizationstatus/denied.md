# GKFriendsAuthorizationStatus.denied

**Framework**: GameKit  
**Kind**: case  
**Role**: Case

Access to the player’s friends’ data denied.

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
case denied
```

```c
GKFriendsAuthorizationStatusDenied
```

## Mentions

- [Connecting players with their friends in your game](../connecting-players-with-their-friends-in-your-game.md)

#### Discussion

The local player can deny access to the friends list by disabling friends in the Game Center settings.

## See Also

### Authorization Statuses
- [GKFriendsAuthorizationStatus.authorized](./authorized.md)
  The player authorized your game to access their list of friends.
- [GKFriendsAuthorizationStatus.notDetermined](./notdetermined.md)
  The player hasn’t choosen whether your game may access their friends list.
- [GKFriendsAuthorizationStatus.restricted](./restricted.md)
  Access to the player’s list of friends restricted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendsauthorizationstatus/denied)*