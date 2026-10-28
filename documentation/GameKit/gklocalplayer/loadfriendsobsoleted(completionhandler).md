# loadFriendsObsoleted(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Retrieves a list of player identifiers for the local player’s friends.

**Availability**:
- iOS 4.1+ - Deprecated in 8.0
- iPadOS 4.1+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use [`loadFriends(_:)`](./loadfriends%28_%29.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS*

```swift
func loadFriendsObsoleted(completionHandler: (@Sendable ([String]?, (any Error)?) -> Void)? = nil)
```

*Mac Catalyst, visionOS*

```swift
func loadFriendsObsoleted() async throws -> [String]
```

```objc
- (void) loadFriendsWithCompletionHandler:(void (^)(NSArray<NSString *> *friendIDs, NSError *error)) completionHandler;
```

## Discussion

After this call completes, the [`friends`](./friends.md) property of the shared local player object is the same list of players that the completion handler returns.

## Parameters

- `completionHandler`: A block to call when the request completes.

  The block receives the following parameters:

  - **friendIDs**: An array of `NSString` objects containing the player identifiers for the players who are friends of the local player. If an error occurs, this value can be non-`nil`. In that case, the array contains the data that GameKit downloads before the error occurs.
  - **error**: If an error occurs, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is `nil`.

## See Also

### Related Documentation
- [var friends: [String]?](./friends.md)
  The player identifiers for the local player’s friends.
### Deprecated methods
- [func authenticate(completionHandler: (((any Error)?) -> Void)?)](./authenticate%28completionhandler%29.md)
  Initializes the local player on the device.
- [func generateIdentityVerificationSignature(completionHandler: ((URL?, Data?, Data?, UInt64, (any Error)?) -> Void)?)](./generateidentityverificationsignature%28completionhandler%29.md)
  Generates a signature so that a third-party server can authenticate the local player.
- [func loadDefaultLeaderboardCategoryID(completionHandler: ((String?, (any Error)?) -> Void)?)](./loaddefaultleaderboardcategoryid%28completionhandler%29.md)
  Loads the category identifier for the local player’s default leaderboard.
- [func loadFriendPlayers(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](./loadfriendplayers%28completionhandler%29.md)
  Retrieves a list of player identifiers for the local player’s friends.
- [func setDefaultLeaderboardCategoryID(String?, completionHandler: (((any Error)?) -> Void)?)](./setdefaultleaderboardcategoryid%28_,completionhandler%29.md)
  Sets the category identifier for the local player’s default leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/loadfriendsobsoleted(completionhandler:))*