# report(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Reports the player’s progress to Game Center.

**Availability**:
- iOS 4.1+ - Deprecated in 7.0
- iPadOS 4.1+ - Deprecated in 7.0
- Mac Catalyst 4.1+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

*macOS, visionOS, watchOS*

```swift
func report(completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

*visionOS*

```swift
func report() async throws
```

```objc
- (void) reportAchievementWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

When the player makes progress towards completing an achievement, your game communicates the player’s progress to Game Center by calling this method. An achievement object is implicitly tied to the local player that was initialized when the object was created; your game should only report progress when the same local player is still on the device.

> **Note**:  To avoid using network bandwidth unnecessarily, only report an achievement when the player has made more progress towards completing it.

When the progress is successfully reported, the achievement is made visible if it was previously hidden. The [`percentComplete`](./percentcomplete.md) and [`lastReportedDate`](./lastreporteddate.md) property values stored on Game Center are updated if the new [`percentComplete`](./percentcomplete.md) value is greater than the value previously stored on Game Center. if the value of the [`percentComplete`](./percentcomplete.md) property was equal to `100.0`, then the achievement is marked as completed and a banner may be shown to the player.

When this method is called, it creates a new background task to handle the request. The method then returns control to your game. The background task automatically handles network errors, resending the data until the task completes. When the task is complete, Game Kit calls your completion handler. The completion handler is always called on the main thread.

## Parameters

- `completionHandler`: A block to be called after the operation completes.

  The block takes the following parameter:

  - ***error***: If the operation was successful, this value is `nil`; otherwise, this parameter holds an object that describes the problem that occurred.

## See Also

### Related Documentation
- [var showsCompletionBanner: Bool](./showscompletionbanner.md)
  A Boolean value that indicates whether GameKit displays a banner when the player completes the achievement.
- [var isHidden: Bool](./ishidden.md)
  A Boolean value that indicates whether the system hides this achievement from the player.
- [var isCompleted: Bool](./iscompleted.md)
  A Boolean value that states whether the player has completed the achievement.
### Deprecated Methods
- [func issueChallenge(toPlayers: [String]?, message: String?)](./issuechallenge%28toplayers,message%29.md)
  Issues an achievement challenge to a list of players.
- [func selectChallengeablePlayerIDs([String]?, withCompletionHandler: (([String]?, (any Error)?) -> Void)?)](./selectchallengeableplayerids%28_,withcompletionhandler%29.md)
  Finds the subset of players who can earn an achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/report(completionhandler:))*