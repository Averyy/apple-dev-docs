# setDefaultLeaderboardCategoryID(_:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Sets the category identifier for the local player’s default leaderboard.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setDefaultLeaderboardCategoryID(_ categoryID: String?) async throws
```

#### Discussion

You set the default leaderboard in App Store Connect when you configure your game’s leaderboards. All players normally start with this leaderboard as the default leaderboard. Calling this method changes the default leaderboard only for the local player.

## Parameters

- `categoryID`: The category ID string for one of your game’s leaderboards.
- `completionHandler`: The block receives the following parameter:

## See Also

- [func authenticate(completionHandler: (((any Error)?) -> Void)?)](gklocalplayer/authenticate(completionhandler:).md)
  Initializes the local player on the device.
- [func generateIdentityVerificationSignature(completionHandler: ((URL?, Data?, Data?, UInt64, (any Error)?) -> Void)?)](gklocalplayer/generateidentityverificationsignature(completionhandler:).md)
  Generates a signature so that a third-party server can authenticate the local player.
- [func loadDefaultLeaderboardCategoryID(completionHandler: ((String?, (any Error)?) -> Void)?)](gklocalplayer/loaddefaultleaderboardcategoryid(completionhandler:).md)
  Loads the category identifier for the local player’s default leaderboard.
- [func loadFriendPlayers(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gklocalplayer/loadfriendplayers(completionhandler:).md)
  Retrieves a list of player identifiers for the local player’s friends.
- [func loadFriendsObsoleted(completionHandler: (([String]?, (any Error)?) -> Void)?)](gklocalplayer/loadfriendsobsoleted(completionhandler:).md)
  Retrieves a list of player identifiers for the local player’s friends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/setdefaultleaderboardcategoryid(_:completionhandler:))*