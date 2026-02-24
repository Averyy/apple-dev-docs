# generateIdentityVerificationSignature(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Generates a signature so that a third-party server can authenticate the local player.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func generateIdentityVerificationSignature() async throws -> (URL, Data, Data, UInt64)
```

#### Discussion

To generate a signature on your server, see the [`fetchItems(forIdentityVerificationSignature:)`](gklocalplayer/fetchitems(foridentityverificationsignature:).md) method.

## Parameters

- `completionHandler`: A block to call when the request completes. The block receives the following parameters: - **publicKeyUrl**: The URL for the public encryption key.
- **signature**: The verification signature data that GameKit generates.
- **salt**: A random `NSString` that GameKit uses to compute the hash and randomize it.
- **timestamp**: The signature’s creation date and time.
- **error**: If an error occurrs, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is `nil`.

## See Also

- [func authenticate(completionHandler: (((any Error)?) -> Void)?)](gklocalplayer/authenticate(completionhandler:).md)
  Initializes the local player on the device.
- [func loadDefaultLeaderboardCategoryID(completionHandler: ((String?, (any Error)?) -> Void)?)](gklocalplayer/loaddefaultleaderboardcategoryid(completionhandler:).md)
  Loads the category identifier for the local player’s default leaderboard.
- [func loadFriendPlayers(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gklocalplayer/loadfriendplayers(completionhandler:).md)
  Retrieves a list of player identifiers for the local player’s friends.
- [func loadFriendsObsoleted(completionHandler: (([String]?, (any Error)?) -> Void)?)](gklocalplayer/loadfriendsobsoleted(completionhandler:).md)
  Retrieves a list of player identifiers for the local player’s friends.
- [func setDefaultLeaderboardCategoryID(String?, completionHandler: (((any Error)?) -> Void)?)](gklocalplayer/setdefaultleaderboardcategoryid(_:completionhandler:).md)
  Sets the category identifier for the local player’s default leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/generateidentityverificationsignature(completionhandler:))*