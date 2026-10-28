# challengeComposeController(withMessage:players:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Provides a challenge compose view controller with pre-selected player identifiers and a preformatted, player-editable message.

**Availability**:
- iOS 8.0+ - Deprecated in 17.0
- iPadOS 8.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.10+ - Deprecated in 14.0
- tvOS 9.0+ - Deprecated in 17.0
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

## Return Value

A [`UIViewController`](../../UIKit/uiviewcontroller.md) view containing the player identifiers and a player-editable message.

## Discussion

The view controller returned is presented modally from the top view controller. After the view controller is displayed and the player sends or cancels the challenge, the completion handler block is called.

When this method is called, it creates a new background task to handle the request. The method then returns control to your game. Later, when the task is complete, GameKit calls your completion handler. The completion handler is always called on the main thread.

## Parameters

- `message`: The preformatted, player-editable message that is being sent to other players.
- `players`: An array of [`GKPlayer`](../gkplayer.md) objects that contains the player identifiers that the challenge is to be sent to.
- `completionHandler`: A block to be called after the view controller has been displayed. Contains the reason the handler was called and all player identifiers that the challenge was sent to.

## See Also

### Issuing a Score Challenge
- [func challengeComposeController(withMessage: String?, players: [GKPlayer]?, completion: GKChallengeComposeHandler?) -> UIViewController](./challengecomposecontroller%28withmessage,players,completion%29.md)
  Provides a challenge compose view controller with preselected player identifiers and a preformatted, player-editable message.
- [typealias GKChallengeComposeHandler](../gkchallengecomposehandler.md)
  A completion block that provides information about the player who issues a challenge and the players who receive it.
- [func challengeComposeController(withPlayers: [String]?, message: String?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController?](./challengecomposecontroller%28withplayers,message,completionhandler%29.md)
  Provides a challenge compose view controller with pre-selected player identifiers and a preformatted, player-editable message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/challengecomposecontroller(withmessage:players:completionhandler:))*