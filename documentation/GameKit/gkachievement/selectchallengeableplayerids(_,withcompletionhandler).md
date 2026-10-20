# selectChallengeablePlayerIDs(_:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Finds the subset of players who can earn an achievement.

**Availability**:
- iOS 6.0+ - Deprecated in 8.0
- iPadOS 6.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This method is obsolete.

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, visionOS*

```swift
func selectChallengeablePlayerIDs(_ playerIDs: [String]?, withCompletionHandler completionHandler: (@Sendable ([String]?, (any Error)?) -> Void)? = nil)
```

*Mac Catalyst, visionOS*

```swift
func selectChallengeablePlayerIDs(_ playerIDs: [String]?) async throws -> [String]
```

```objc
- (void) selectChallengeablePlayerIDs:(NSArray<NSString *> *) playerIDs withCompletionHandler:(void (^)(NSArray<NSString *> *challengeablePlayerIDs, NSError *error)) completionHandler;
```

#### Discussion

When this method is called, it creates a new background task to handle the request. The method then returns control to your game. Later, when the task is complete, Game Kit calls your completion handler. The completion handler is always called on the main thread.

## Parameters

- `playerIDs`: An array of `NSString` objects containing a list of players. The list of players is used to find those players that are eligible to earn the achievement.
- `completionHandler`: A block to be called when the download is completed.

  The block receives the following parameters:

  - ***challengeablePlayerIDs***: An array of player identifiers representing the players in the original array that are able to complete the challenge. If an error occurred, this parameter may be non-`nil`, in which case the array holds whatever achievement information Game Kit was able to fetch.
  - ***error***: If an error occurred, this object describes the error. If the operation completed successfully, this value is `nil`.

## See Also

### Deprecated Methods
- [func issueChallenge(toPlayers: [String]?, message: String?)](./issuechallenge%28toplayers,message%29.md)
  Issues an achievement challenge to a list of players.
- [func report(completionHandler: (((any Error)?) -> Void)?)](./report%28completionhandler%29.md)
  Reports the player’s progress to Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/selectchallengeableplayerids(_:withcompletionhandler:))*