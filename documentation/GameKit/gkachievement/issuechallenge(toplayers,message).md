# issueChallenge(toPlayers:message:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Issues an achievement challenge to a list of players.

**Availability**:
- iOS 6.0+ - Deprecated in 7.0
- iPadOS 6.0+ - Deprecated in 7.0
- Mac Catalyst 6.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
func issueChallenge(toPlayers playerIDs: [String]?, message: String?)
```

```objc
- (void) issueChallengeToPlayers:(NSArray<NSString *> *) playerIDs message:(NSString *) message;
```

#### Discussion

Set up your game to issue a challenge request only in direct response to a player action.

If you mark the achievement as hidden, or if the challenged player already earned the achievement and you don’t mark the achievement as replayable in App Store Connect, the local player can’t issue the challenge.

## Parameters

- `playerIDs`: The identifiers for the players to challenge. Because Game Center limits the number of players in a challenge request to 10, the maximum size of this array is 10.
- `message`: A text message to display to the challenged players.

## See Also

### Deprecated Methods
- [func report(completionHandler: (((any Error)?) -> Void)?)](./report%28completionhandler%29.md)
  Reports the player’s progress to Game Center.
- [func selectChallengeablePlayerIDs([String]?, withCompletionHandler: (([String]?, (any Error)?) -> Void)?)](./selectchallengeableplayerids%28_,withcompletionhandler%29.md)
  Finds the subset of players who can earn an achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/issuechallenge(toplayers:message:))*