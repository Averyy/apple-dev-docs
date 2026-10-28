# generateIdentityVerificationSignature(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Generates a signature so that a third-party server can authenticate the local player.

**Availability**:
- iOS 7.0+ - Deprecated in 13.5
- iPadOS 7.0+ - Deprecated in 13.5
- Mac Catalyst 13.1+ - Deprecated in 13.5
- macOS 10.10+ - Deprecated in 10.15.5
- tvOS 9.0+ - Deprecated in 13.4.8
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 6.5

> **Deprecated**: Use [`fetchItems(forIdentityVerificationSignature:)`](./fetchitems%28foridentityverificationsignature%29.md) instead.

## Declaration

```swift
func generateIdentityVerificationSignature(completionHandler: (@Sendable (URL?, Data?, Data?, UInt64, (any Error)?) -> Void)? = nil)
```

```swift
func generateIdentityVerificationSignature() async throws -> (URL, Data, Data, UInt64)
```

```objc
- (void) generateIdentityVerificationSignatureWithCompletionHandler:(void (^)(NSURL *publicKeyUrl, NSData *signature, NSData *salt, uint64_t timestamp, NSError *error)) completionHandler;
```

## Discussion

To generate a signature on your server, see the [`fetchItems(forIdentityVerificationSignature:)`](./fetchitems%28foridentityverificationsignature%29.md) method.

## Parameters

- `completionHandler`: A block to call when the request completes.

  The block receives the following parameters:

  - **publicKeyUrl**: The URL for the public encryption key.
  - **signature**: The verification signature data that GameKit generates.
  - **salt**: A random `NSString` that GameKit uses to compute the hash and randomize it.
  - **timestamp**: The signature’s creation date and time.
  - **error**: If an error occurrs, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is `nil`.

## See Also

### Deprecated methods
- [func authenticate(completionHandler: (((any Error)?) -> Void)?)](./authenticate%28completionhandler%29.md)
  Initializes the local player on the device.
- [func loadDefaultLeaderboardCategoryID(completionHandler: ((String?, (any Error)?) -> Void)?)](./loaddefaultleaderboardcategoryid%28completionhandler%29.md)
  Loads the category identifier for the local player’s default leaderboard.
- [func loadFriendPlayers(completionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](./loadfriendplayers%28completionhandler%29.md)
  Retrieves a list of player identifiers for the local player’s friends.
- [func loadFriendsObsoleted(completionHandler: (([String]?, (any Error)?) -> Void)?)](./loadfriendsobsoleted%28completionhandler%29.md)
  Retrieves a list of player identifiers for the local player’s friends.
- [func setDefaultLeaderboardCategoryID(String?, completionHandler: (((any Error)?) -> Void)?)](./setdefaultleaderboardcategoryid%28_,completionhandler%29.md)
  Sets the category identifier for the local player’s default leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/generateidentityverificationsignature(completionhandler:))*