# challengeComposeController(withMessage:players:completion:)

**Framework**: GameKit  
**Kind**: method

Provides a view controller that you present to the player to issue an achievement challenge.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func challengeComposeController(withMessage message: String?, players: [GKPlayer], completion completionHandler: GKChallengeComposeHandler? = nil) -> UIViewController
```

#### Discussion

This method presents the view controller modally from the top view controller. GameKit calls the completion handler block after it displays the view controller and the player sends or cancels the challenge.

## Parameters

- `message`: The challenge message, which the player can edit before GameKit sends it to other players.
- `players`: The players to invite to the challenge.
- `completionHandler`: A block that GameKit calls after it displays the view controller.

## See Also

- [func selectChallengeablePlayers([GKPlayer], withCompletionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gkachievement/selectchallengeableplayers(_:withcompletionhandler:).md)
  Finds the subset of players who can earn an achievement.
- [typealias GKChallengeComposeHandler](gkchallengecomposehandler.md)
  A completion block that provides information about the player who issues a challenge and the players who receive it.
- [func challengeComposeController(withMessage: String?, players: [GKPlayer], completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController](gkachievement/challengecomposecontroller(withmessage:players:completionhandler:).md)
  Provides a view controller that you present to the player to issue an achievement challenge.
- [func challengeComposeController(withPlayers: [String]?, message: String?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController?](gkachievement/challengecomposecontroller(withplayers:message:completionhandler:).md)
  Provides a challenge compose view controller with preselected player identifiers and a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/challengecomposecontroller(withmessage:players:completion:))*