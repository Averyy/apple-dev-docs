# report(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Reports the player’s progress to Game Center.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func report() async throws
```

#### Discussion

When the player makes progress towards completing an achievement, your game communicates the player’s progress to Game Center by calling this method. An achievement object is implicitly tied to the local player that was authenticated when the object was created; your game should only report progress when the same local player is still authenticated on the device.

> **Note**:  To avoid using network bandwidth unnecessarily, only report an achievement when the player has made more progress towards completing it.

 To avoid using network bandwidth unnecessarily, only report an achievement when the player has made more progress towards completing it.

When the progress is successfully reported, the achievement is made visible if it was previously hidden. The [`percentComplete`](gkachievement/percentcomplete.md) and [`lastReportedDate`](gkachievement/lastreporteddate.md) property values stored on Game Center are updated if the new [`percentComplete`](gkachievement/percentcomplete.md) value is greater than the value previously stored on Game Center. if the value of the [`percentComplete`](gkachievement/percentcomplete.md) property was equal to `100.0`, then the achievement is marked as completed and a banner may be shown to the player.

When this method is called, it creates a new background task to handle the request. The method then returns control to your game. The background task automatically handles network errors, resending the data until the task completes. When the task is complete, Game Kit calls your completion handler. The completion handler is always called on the main thread.

## Parameters

- `completionHandler`: The block takes the following parameter:

## See Also

- [var showsCompletionBanner: Bool](gkachievement/showscompletionbanner.md)
  A Boolean value that indicates whether GameKit displays a banner when the player completes the achievement.
- [var isHidden: Bool](gkachievement/ishidden.md)
  A Boolean value that indicates whether the system hides this achievement from the player.
- [var isCompleted: Bool](gkachievement/iscompleted.md)
  A Boolean value that states whether the player has completed the achievement.
- [func issueChallenge(toPlayers: [String]?, message: String?)](gkachievement/issuechallenge(toplayers:message:).md)
  Issues an achievement challenge to a list of players.
- [func selectChallengeablePlayerIDs([String]?, withCompletionHandler: (([String]?, (any Error)?) -> Void)?)](gkachievement/selectchallengeableplayerids(_:withcompletionhandler:).md)
  Finds the subset of players who can earn an achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/report(completionhandler:))*