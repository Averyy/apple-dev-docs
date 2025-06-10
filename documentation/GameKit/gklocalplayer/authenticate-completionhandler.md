# authenticate(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Initializes the local player on the device.

**Availability**:
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func authenticate() async throws
```

#### Discussion

For more information, see [`Authenticating a player`](authenticating-a-player.md).

## Parameters

- `completionHandler`: The block takes the following parameter:

## See Also

- [func generateIdentityVerificationSignature(completionHandler: ((URL?, Data?, Data?, UInt64, (any Error)?) -> Void)?)](gklocalplayer/generateidentityverificationsignature(completionhandler:).md)
  Generates a signature so that a third-party server can authenticate the local player.
- [func loadDefaultLeaderboardCategoryID(completionHandler: ((String?, (any Error)?) -> Void)?)](gklocalplayer/loaddefaultleaderboardcategoryid(completionhandler:).md)
  Loads the category identifier for the local player’s default leaderboard.
- [func loadFriendPlayers(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gklocalplayer/loadfriendplayers(completionhandler:).md)
  Retrieves a list of player identifiers for the local player’s friends.
- [func loadFriendsObsoleted(completionHandler: (([String]?, (any Error)?) -> Void)?)](gklocalplayer/loadfriendsobsoleted(completionhandler:).md)
  Retrieves a list of player identifiers for the local player’s friends.
- [func setDefaultLeaderboardCategoryID(String?, completionHandler: (((any Error)?) -> Void)?)](gklocalplayer/setdefaultleaderboardcategoryid(_:completionhandler:).md)
  Sets the category identifier for the local player’s default leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/authenticate(completionhandler:))*