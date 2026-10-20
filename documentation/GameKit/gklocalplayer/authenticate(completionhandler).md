# authenticate(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Initializes the local player on the device.

**Availability**:
- iOS 4.1+ - Deprecated in 6.0
- iPadOS 4.1+ - Deprecated in 6.0
- Mac Catalyst 4.1+ - Deprecated in 6.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`authenticateHandler`](./authenticatehandler.md) instead.

## Declaration

*visionOS, watchOS*

```swift
func authenticate(completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

*visionOS*

```swift
func authenticate() async throws
```

```objc
- (void) authenticateWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

For more information, see [Authenticating a player](../authenticating-a-player.md).

## Parameters

- `completionHandler`: A block to call when the player initializes or when an error occurs.

  The block takes the following parameter:

  - **error**: This parameter is `nil` if the player successfully initializes. Otherwise, it contains an error object that describes the error that occurrs.

## See Also

### Deprecated methods
- [func generateIdentityVerificationSignature(completionHandler: ((URL?, Data?, Data?, UInt64, (any Error)?) -> Void)?)](./generateidentityverificationsignature%28completionhandler%29.md)
  Generates a signature so that a third-party server can authenticate the local player.
- [func loadDefaultLeaderboardCategoryID(completionHandler: ((String?, (any Error)?) -> Void)?)](./loaddefaultleaderboardcategoryid%28completionhandler%29.md)
  Loads the category identifier for the local player’s default leaderboard.
- [func loadFriendPlayers(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](./loadfriendplayers%28completionhandler%29.md)
  Retrieves a list of player identifiers for the local player’s friends.
- [func loadFriendsObsoleted(completionHandler: (([String]?, (any Error)?) -> Void)?)](./loadfriendsobsoleted%28completionhandler%29.md)
  Retrieves a list of player identifiers for the local player’s friends.
- [func setDefaultLeaderboardCategoryID(String?, completionHandler: (((any Error)?) -> Void)?)](./setdefaultleaderboardcategoryid%28_,completionhandler%29.md)
  Sets the category identifier for the local player’s default leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/authenticate(completionhandler:))*