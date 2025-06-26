# GKChallengeComposeHandler

**Framework**: GameKit  
**Kind**: typealias

A completion block that provides information about the player who issues a challenge and the players who receive it.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
typealias GKChallengeComposeHandler = (NSViewController, Bool, [GKPlayer]?) -> Void
```

## Parameters

- `composeController`: The view controller for the challenge.
- `didIssueChallenge`: A Boolean value that indicates whether the player issues the challenge.
- `sentPlayers`: The players that receive the challenge.

## See Also

- [func selectChallengeablePlayers([GKPlayer], withCompletionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gkachievement/selectchallengeableplayers(_:withcompletionhandler:).md)
  Finds the subset of players who can earn an achievement.
- [func challengeComposeController(withMessage: String?, players: [GKPlayer], completion: GKChallengeComposeHandler?) -> UIViewController](gkachievement/challengecomposecontroller(withmessage:players:completion:).md)
  Provides a view controller that you present to the player to issue an achievement challenge.
- [func challengeComposeController(withMessage: String?, players: [GKPlayer], completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController](gkachievement/challengecomposecontroller(withmessage:players:completionhandler:).md)
  Provides a view controller that you present to the player to issue an achievement challenge.
- [func challengeComposeController(withPlayers: [String]?, message: String?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController?](gkachievement/challengecomposecontroller(withplayers:message:completionhandler:).md)
  Provides a challenge compose view controller with preselected player identifiers and a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengecomposehandler)*