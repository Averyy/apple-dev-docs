# challengeComposeController(withMessage:players:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Provides a challenge compose view controller with pre-selected player identifiers and a preformatted, player-editable message.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func challengeComposeController(withMessage message: String?, players: [GKPlayer]?, completionHandler: GKChallengeComposeCompletionBlock? = nil) -> NSViewController
```

#### Return Value

A [`UIViewController`](https://developer.apple.com/documentation/UIKit/UIViewController) view containing the player identifiers and a player-editable message.

#### Discussion

The view controller returned is presented modally from the top view controller. After the view controller is displayed and the player sends or cancels the challenge, the completion handler block is called.

When this method is called, it creates a new background task to handle the request. The method then returns control to your game. Later, when the task is complete, GameKit calls your completion handler. The completion handler is always called on the main thread.

## Parameters

- `message`: The preformatted, player-editable message that is being sent to other players.
- `players`: An array of   objects that contains the player identifiers that the challenge is to be sent to.
- `completionHandler`: A block to be called after the view controller has been displayed. Contains the reason the handler was called and all player identifiers that the challenge was sent to.

## See Also

- [func challengeComposeController(withMessage: String?, players: [GKPlayer]?, completion: GKChallengeComposeHandler?) -> UIViewController](gkscore/challengecomposecontroller(withmessage:players:completion:).md)
  Provides a challenge compose view controller with preselected player identifiers and a preformatted, player-editable message.
- [typealias GKChallengeComposeHandler](gkchallengecomposehandler.md)
  A completion block that provides information about the player who issues a challenge and the players who receive it.
- [func challengeComposeController(withPlayers: [String]?, message: String?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController?](gkscore/challengecomposecontroller(withplayers:message:completionhandler:).md)
  Provides a challenge compose view controller with pre-selected player identifiers and a preformatted, player-editable message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/challengecomposecontroller(withmessage:players:completionhandler:))*