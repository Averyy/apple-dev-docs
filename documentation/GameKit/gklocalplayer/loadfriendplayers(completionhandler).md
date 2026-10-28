# loadFriendPlayers(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Retrieves a list of player identifiers for the local player’s friends.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.10+ - Deprecated in 10.11
- tvOS 9.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use [`loadFriends(_:)`](./loadfriends%28_%29.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS*

```swift
func loadFriendPlayers(completionHandler: (@Sendable ([GKPlayer]?, (any Error)?) -> Void)? = nil)
```

*Mac Catalyst, visionOS*

```swift
func loadFriendPlayers() async throws -> [GKPlayer]
```

```objc
- (void) loadFriendPlayersWithCompletionHandler:(void (^)(NSArray<GKPlayer *> *friendPlayers, NSError *error)) completionHandler;
```

## Discussion

The code below shows an example of how to load a player’s friends. Create your own method to save information about the found players.

```objc
- (void) retrieveFriends
{
   GKLocalPlayer *lp = [GKLocalPlayer localPlayer];
   if (lp.authenticated)
   {
      [lp loadFriendPlayersWithCompletionHandler:^(NSArray *friendPlayers, NSError *error) {
         if (friendPlayers != nil)
         {
            [self loadPlayerData: friendPlayers];
         }
      }];
   }
}
```

## Parameters

- `completionHandler`: A block to call when the request completes.

  The block receives the following parameters:

  - **friendPlayers**: An array of [`GKPlayer`](../gkplayer.md) objects containing the player identifiers for the players who are friends of the local player. If an error occurs, this value can be non-`nil`. In that case, the array contains the data that GameKit downloads before the error occurs.
  - **error**: If an error occurs, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is `nil`.

## See Also

### Deprecated methods
- [func authenticate(completionHandler: (((any Error)?) -> Void)?)](./authenticate%28completionhandler%29.md)
  Initializes the local player on the device.
- [func generateIdentityVerificationSignature(completionHandler: ((URL?, Data?, Data?, UInt64, (any Error)?) -> Void)?)](./generateidentityverificationsignature%28completionhandler%29.md)
  Generates a signature so that a third-party server can authenticate the local player.
- [func loadDefaultLeaderboardCategoryID(completionHandler: ((String?, (any Error)?) -> Void)?)](./loaddefaultleaderboardcategoryid%28completionhandler%29.md)
  Loads the category identifier for the local player’s default leaderboard.
- [func loadFriendsObsoleted(completionHandler: (([String]?, (any Error)?) -> Void)?)](./loadfriendsobsoleted%28completionhandler%29.md)
  Retrieves a list of player identifiers for the local player’s friends.
- [func setDefaultLeaderboardCategoryID(String?, completionHandler: (((any Error)?) -> Void)?)](./setdefaultleaderboardcategoryid%28_,completionhandler%29.md)
  Sets the category identifier for the local player’s default leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/loadfriendplayers(completionhandler:))*