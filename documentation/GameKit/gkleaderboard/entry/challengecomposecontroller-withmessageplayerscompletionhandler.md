# challengeComposeController(withMessage:players:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Provides a challenge compose view controller with preselected player identifiers and a preformatted, player-editable message.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func challengeComposeController(withMessage message: String?, players: [GKPlayer]?, completionHandler: GKChallengeComposeCompletionBlock? = nil) -> NSViewController
```

#### Return Value

A [`UIViewController`](https://developer.apple.com/documentation/UIKit/UIViewController) containing the player identifiers and a player-editable message.

#### Discussion

GameKit presents the returned view controller modally on the top view controller. After GameKit displays the view controller and the player sends or cancels the challenge, GameKit calls the completion handler block on the main thread.

## Parameters

- `message`: The preformatted, player-editable message that GameKit sends to the players in the challenge.
- `players`: Players to invite to the challenge.
- `completionHandler`: A block that GameKit calls after it displays the view controller.

## See Also

- [func challengeComposeController(withMessage: String?, players: [GKPlayer]?, completion: GKChallengeComposeHandler?) -> UIViewController](gkleaderboard/entry/challengecomposecontroller(withmessage:players:completion:).md)
  Provides a challenge compose view controller with preselected player identifiers and a preformatted, player-editable message.
- [typealias GKChallengeComposeHandler](gkchallengecomposehandler.md)
  A completion block that provides information about the player who issues a challenge and the players who receive it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/entry/challengecomposecontroller(withmessage:players:completionhandler:))*