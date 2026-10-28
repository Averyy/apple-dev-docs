# challengeComposeController(withMessage:players:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Provides a view controller that you present to the player to issue an achievement challenge.

**Availability**:
- iOS 8.0+ - Deprecated in 17.0
- iPadOS 8.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.10+ - Deprecated in 14.0
- tvOS 9.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`challengeComposeController(withMessage:players:completion:)`](./challengecomposecontroller%28withmessage,players,completion%29.md) method instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func challengeComposeController(withMessage message: String?, players: [GKPlayer], completionHandler: GKChallengeComposeCompletionBlock? = nil) -> UIViewController
```

*macOS*

```swift
func challengeComposeController(withMessage message: String?, players: [GKPlayer], completionHandler: GKChallengeComposeCompletionBlock? = nil) -> NSViewController
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
- (UIViewController *) challengeComposeControllerWithMessage:(NSString *) message players:(NSArray<GKPlayer *> *) players completionHandler:(GKChallengeComposeCompletionBlock) completionHandler;
```

*macOS*

```objc
- (NSViewController *) challengeComposeControllerWithMessage:(NSString *) message players:(NSArray<GKPlayer *> *) players completionHandler:(GKChallengeComposeCompletionBlock) completionHandler;
```

## Return Value

A view controller that contains the player identifiers and the challenge message.

## Discussion

This method presents the view controller modally from the top view controller. GameKit calls the completion handler block after it displays the view controller and the player sends or cancels the challenge.

## Parameters

- `message`: The challenge message which the player can edit before GameKit sends it to other players.
- `players`: The players that the challenge should be sent to.
- `completionHandler`: A block that GameKit calls after it displays the view controller.

## See Also

### Issuing Achievement Challenges
- [func selectChallengeablePlayers([GKPlayer], withCompletionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](./selectchallengeableplayers%28_,withcompletionhandler%29.md)
  Finds the subset of players who can earn an achievement.
- [func challengeComposeController(withMessage: String?, players: [GKPlayer], completion: GKChallengeComposeHandler?) -> UIViewController](./challengecomposecontroller%28withmessage,players,completion%29.md)
  Provides a view controller that you present to the player to issue an achievement challenge.
- [typealias GKChallengeComposeHandler](../gkchallengecomposehandler.md)
  A completion block that provides information about the player who issues a challenge and the players who receive it.
- [func challengeComposeController(withPlayers: [String]?, message: String?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController?](./challengecomposecontroller%28withplayers,message,completionhandler%29.md)
  Provides a challenge compose view controller with preselected player identifiers and a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/challengecomposecontroller(withmessage:players:completionhandler:))*