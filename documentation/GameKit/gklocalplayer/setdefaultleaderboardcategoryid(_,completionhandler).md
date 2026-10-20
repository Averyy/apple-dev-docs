# setDefaultLeaderboardCategoryID(_:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Sets the category identifier for the local player’s default leaderboard.

**Availability**:
- iOS 6.0+ - Deprecated in 7.0
- iPadOS 6.0+ - Deprecated in 7.0
- Mac Catalyst 6.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`setDefaultLeaderboardIdentifier(_:completionHandler:)`](./setdefaultleaderboardidentifier%28_,completionhandler%29.md) instead.

## Declaration

*macOS, visionOS, watchOS*

```swift
func setDefaultLeaderboardCategoryID(_ categoryID: String?, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

*visionOS*

```swift
func setDefaultLeaderboardCategoryID(_ categoryID: String?) async throws
```

```objc
- (void) setDefaultLeaderboardCategoryID:(NSString *) categoryID completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

You set the default leaderboard in App Store Connect when you configure your game’s leaderboards. All players normally start with this leaderboard as the default leaderboard. Calling this method changes the default leaderboard only for the local player.

## Parameters

- `categoryID`: The category ID string for one of your game’s leaderboards.
- `completionHandler`: A block to call when the request completes.

  The block receives the following parameter:

  - **error**: If an error occurs, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is `nil`.

## See Also

### Deprecated methods
- [func authenticate(completionHandler: (((any Error)?) -> Void)?)](./authenticate%28completionhandler%29.md)
  Initializes the local player on the device.
- [func generateIdentityVerificationSignature(completionHandler: ((URL?, Data?, Data?, UInt64, (any Error)?) -> Void)?)](./generateidentityverificationsignature%28completionhandler%29.md)
  Generates a signature so that a third-party server can authenticate the local player.
- [func loadDefaultLeaderboardCategoryID(completionHandler: ((String?, (any Error)?) -> Void)?)](./loaddefaultleaderboardcategoryid%28completionhandler%29.md)
  Loads the category identifier for the local player’s default leaderboard.
- [func loadFriendPlayers(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](./loadfriendplayers%28completionhandler%29.md)
  Retrieves a list of player identifiers for the local player’s friends.
- [func loadFriendsObsoleted(completionHandler: (([String]?, (any Error)?) -> Void)?)](./loadfriendsobsoleted%28completionhandler%29.md)
  Retrieves a list of player identifiers for the local player’s friends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/setdefaultleaderboardcategoryid(_:completionhandler:))*