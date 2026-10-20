# challengeComposeController(withMessage:players:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Provides a challenge compose view controller with preselected player identifiers and a preformatted, player-editable message.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func challengeComposeController(withMessage message: String?, players: [GKPlayer]?, completionHandler: GKChallengeComposeCompletionBlock? = nil) -> UIViewController
```

*macOS*

```swift
func challengeComposeController(withMessage message: String?, players: [GKPlayer]?, completionHandler: GKChallengeComposeCompletionBlock? = nil) -> NSViewController
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
- (UIViewController *) challengeComposeControllerWithMessage:(NSString *) message players:(NSArray<GKPlayer *> *) players completionHandler:(GKChallengeComposeCompletionBlock) completionHandler;
```

*macOS*

```objc
- (NSViewController *) challengeComposeControllerWithMessage:(NSString *) message players:(NSArray<GKPlayer *> *) players completionHandler:(GKChallengeComposeCompletionBlock) completionHandler;
```

#### Return Value

A [`UIViewController`](../../../UIKit/uiviewcontroller.md) containing the player identifiers and a player-editable message.

#### Discussion

GameKit presents the returned view controller modally on the top view controller. After GameKit displays the view controller and the player sends or cancels the challenge, GameKit calls the completion handler block on the main thread.

## Parameters

- `message`: The preformatted, player-editable message that GameKit sends to the players in the challenge.
- `players`: Players to invite to the challenge.
- `completionHandler`: A block that GameKit calls after it displays the view controller.

## See Also

### Presenting Challenges
- [func challengeComposeController(withMessage: String?, players: [GKPlayer]?, completion: GKChallengeComposeHandler?) -> UIViewController](./challengecomposecontroller%28withmessage,players,completion%29.md)
  Provides a challenge compose view controller with preselected player identifiers and a preformatted, player-editable message.
- [typealias GKChallengeComposeHandler](../../gkchallengecomposehandler.md)
  A completion block that provides information about the player who issues a challenge and the players who receive it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/entry/challengecomposecontroller(withmessage:players:completionhandler:))*