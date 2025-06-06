# challengeComposeController(withPlayers:message:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Provides a challenge compose view controller with preselected player identifiers and a message.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func challengeComposeController(withPlayers playerIDs: [String]?, message: String?, completionHandler: GKChallengeComposeCompletionBlock? = nil) -> UIViewController?
```

#### Return Value

A `UIViewController` view that contains the player identifiers and the challenge message.

#### Discussion

When this method is called, it creates a new background task to handle the request. The method then returns control to your game. Later, when the task is complete, Game Kit calls your completion handler. The completion handler is always called on the main thread.

The view controller returned is presented modally from the top view controller. After the view controller is displayed and the player sends or cancels the challenge, the completion handler block is called.

## Parameters

- `playerIDs`: An array of   objects that contains the player identifiers that the challenge is to be sent to.
- `message`: The message that is sent to other players. This message can be edited by the player.
- `completionHandler`: A block to be called after the view controller has been displayed. Contains the reason the handler was called and all player identifiers that the challenge was sent to.

## See Also

- [func selectChallengeablePlayers([GKPlayer], withCompletionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gkachievement/selectchallengeableplayers(_:withcompletionhandler:).md)
  Finds the subset of players who can earn an achievement.
- [func challengeComposeController(withMessage: String?, players: [GKPlayer], completion: GKChallengeComposeHandler?) -> UIViewController](gkachievement/challengecomposecontroller(withmessage:players:completion:).md)
  Provides a view controller that you present to the player to issue an achievement challenge.
- [typealias GKChallengeComposeHandler](gkchallengecomposehandler.md)
  A completion block that provides information about the player who issues a challenge and the players who receive it.
- [func challengeComposeController(withMessage: String?, players: [GKPlayer], completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController](gkachievement/challengecomposecontroller(withmessage:players:completionhandler:).md)
  Provides a view controller that you present to the player to issue an achievement challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/challengecomposecontroller(withplayers:message:completionhandler:))*