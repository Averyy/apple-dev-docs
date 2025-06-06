# selectChallengeablePlayers(_:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method

Finds the subset of players who can earn an achievement.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func selectChallengeablePlayers(_ players: [GKPlayer]) async throws -> [GKPlayer]
```

## Parameters

- `players`: A list of players that GameKit uses to find players who are eligible to earn the achievement.
- `completionHandler`: The block receives the following parameters:

## See Also

- [func challengeComposeController(withMessage: String?, players: [GKPlayer], completion: GKChallengeComposeHandler?) -> UIViewController](gkachievement/challengecomposecontroller(withmessage:players:completion:).md)
  Provides a view controller that you present to the player to issue an achievement challenge.
- [typealias GKChallengeComposeHandler](gkchallengecomposehandler.md)
  A completion block that provides information about the player who issues a challenge and the players who receive it.
- [func challengeComposeController(withMessage: String?, players: [GKPlayer], completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController](gkachievement/challengecomposecontroller(withmessage:players:completionhandler:).md)
  Provides a view controller that you present to the player to issue an achievement challenge.
- [func challengeComposeController(withPlayers: [String]?, message: String?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController?](gkachievement/challengecomposecontroller(withplayers:message:completionhandler:).md)
  Provides a challenge compose view controller with preselected player identifiers and a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/selectchallengeableplayers(_:withcompletionhandler:))*