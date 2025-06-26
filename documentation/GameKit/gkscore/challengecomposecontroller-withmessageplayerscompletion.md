# challengeComposeController(withMessage:players:completion:)

**Framework**: GameKit  
**Kind**: method

Provides a challenge compose view controller with preselected player identifiers and a preformatted, player-editable message.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func challengeComposeController(withMessage message: String?, players: [GKPlayer]?, completion completionHandler: GKChallengeComposeHandler? = nil) -> NSViewController
```

## Parameters

- `message`: The challenge that GameKit sends to other players.
- `players`: The players to invite to the challenge.
- `completionHandler`: A block that GameKit calls after it displays the view controller.

## See Also

- [typealias GKChallengeComposeHandler](gkchallengecomposehandler.md)
  A completion block that provides information about the player who issues a challenge and the players who receive it.
- [func challengeComposeController(withMessage: String?, players: [GKPlayer]?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController](gkscore/challengecomposecontroller(withmessage:players:completionhandler:).md)
  Provides a challenge compose view controller with pre-selected player identifiers and a preformatted, player-editable message.
- [func challengeComposeController(withPlayers: [String]?, message: String?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController?](gkscore/challengecomposecontroller(withplayers:message:completionhandler:).md)
  Provides a challenge compose view controller with pre-selected player identifiers and a preformatted, player-editable message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/challengecomposecontroller(withmessage:players:completion:))*