# loadDefaultLeaderboardCategoryID(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Loads the category identifier for the local player’s default leaderboard.

**Availability**:
- iOS 6.0+ - Deprecated in 7.0
- iPadOS 6.0+ - Deprecated in 7.0
- Mac Catalyst 6.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`loadDefaultLeaderboardIdentifier(completionHandler:)`](./loaddefaultleaderboardidentifier%28completionhandler%29.md) instead.

## Declaration

*macOS, visionOS, watchOS*

```swift
func loadDefaultLeaderboardCategoryID(completionHandler: (@Sendable (String?, (any Error)?) -> Void)? = nil)
```

*visionOS*

```swift
func loadDefaultLeaderboardCategoryID() async throws -> String
```

```objc
- (void) loadDefaultLeaderboardCategoryIDWithCompletionHandler:(void (^)(NSString *categoryID, NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: A block to call when the request completes.

  The block receives the following parameters:

  - **categoryID**: The category ID string for the local player’s default leaderboard.
  - **error**: If an error occurrs, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is `nil`.

## See Also

### Deprecated methods
- [func authenticate(completionHandler: (((any Error)?) -> Void)?)](./authenticate%28completionhandler%29.md)
  Initializes the local player on the device.
- [func generateIdentityVerificationSignature(completionHandler: ((URL?, Data?, Data?, UInt64, (any Error)?) -> Void)?)](./generateidentityverificationsignature%28completionhandler%29.md)
  Generates a signature so that a third-party server can authenticate the local player.
- [func loadFriendPlayers(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](./loadfriendplayers%28completionhandler%29.md)
  Retrieves a list of player identifiers for the local player’s friends.
- [func loadFriendsObsoleted(completionHandler: (([String]?, (any Error)?) -> Void)?)](./loadfriendsobsoleted%28completionhandler%29.md)
  Retrieves a list of player identifiers for the local player’s friends.
- [func setDefaultLeaderboardCategoryID(String?, completionHandler: (((any Error)?) -> Void)?)](./setdefaultleaderboardcategoryid%28_,completionhandler%29.md)
  Sets the category identifier for the local player’s default leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/loaddefaultleaderboardcategoryid(completionhandler:))*