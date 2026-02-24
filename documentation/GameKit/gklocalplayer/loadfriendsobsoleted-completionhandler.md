# loadFriendsObsoleted(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Retrieves a list of player identifiers for the local player’s friends.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func loadFriendsObsoleted() async throws -> [String]
```

#### Discussion

After this call completes, the [`friends`](gklocalplayer/friends.md) property of the shared local player object is the same list of players that the completion handler returns.

## Parameters

- `completionHandler`: A block to call when the request completes. The block receives the following parameters: - **friendIDs**: An array of `NSString` objects containing the player identifiers for the players who are friends of the local player. If an error occurs, this value can be non-`nil`. In that case, the array contains the data that GameKit downloads before the error occurs.
- **error**: If an error occurs, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is `nil`.

## See Also

- [var friends: [String]?](gklocalplayer/friends.md)
  The player identifiers for the local player’s friends.
- [func authenticate(completionHandler: (((any Error)?) -> Void)?)](gklocalplayer/authenticate(completionhandler:).md)
  Initializes the local player on the device.
- [func generateIdentityVerificationSignature(completionHandler: ((URL?, Data?, Data?, UInt64, (any Error)?) -> Void)?)](gklocalplayer/generateidentityverificationsignature(completionhandler:).md)
  Generates a signature so that a third-party server can authenticate the local player.
- [func loadDefaultLeaderboardCategoryID(completionHandler: ((String?, (any Error)?) -> Void)?)](gklocalplayer/loaddefaultleaderboardcategoryid(completionhandler:).md)
  Loads the category identifier for the local player’s default leaderboard.
- [func loadFriendPlayers(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gklocalplayer/loadfriendplayers(completionhandler:).md)
  Retrieves a list of player identifiers for the local player’s friends.
- [func setDefaultLeaderboardCategoryID(String?, completionHandler: (((any Error)?) -> Void)?)](gklocalplayer/setdefaultleaderboardcategoryid(_:completionhandler:).md)
  Sets the category identifier for the local player’s default leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/loadfriendsobsoleted(completionhandler:))*