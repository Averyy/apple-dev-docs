# selectChallengeablePlayerIDs(_:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method

Finds the subset of players who can earn an achievement.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
func selectChallengeablePlayerIDs(_ playerIDs: [String]?) async throws -> [String]
```

#### Discussion

When this method is called, it creates a new background task to handle the request. The method then returns control to your game. Later, when the task is complete, Game Kit calls your completion handler. The completion handler is always called on the main thread.

## Parameters

- `playerIDs`: An array of `NSString` objects containing a list of players. The list of players is used to find those players that are eligible to earn the achievement.
- `completionHandler`: A block to be called when the download is completed. The block receives the following parameters: - ***challengeablePlayerIDs***: An array of player identifiers representing the players in the original array that are able to complete the challenge. If an error occurred, this parameter may be non-`nil`, in which case the array holds whatever achievement information Game Kit was able to fetch.
- ***error***: If an error occurred, this object describes the error. If the operation completed successfully, this value is `nil`.

## See Also

- [func issueChallenge(toPlayers: [String]?, message: String?)](gkachievement/issuechallenge(toplayers:message:).md)
  Issues an achievement challenge to a list of players.
- [func report(completionHandler: (((any Error)?) -> Void)?)](gkachievement/report(completionhandler:).md)
  Reports the player’s progress to Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/selectchallengeableplayerids(_:withcompletionhandler:))*