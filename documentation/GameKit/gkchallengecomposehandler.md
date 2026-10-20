# GKChallengeComposeHandler

**Framework**: GameKit  
**Kind**: typealias  
**Role**: Type Alias

A completion block that provides information about the player who issues a challenge and the players who receive it.

**Availability**:
- iOS 17.0+ - Deprecated in 26.0
- iPadOS 17.0+ - Deprecated in 26.0
- Mac Catalyst 17.0+ - Deprecated in 26.0
- macOS 14.0+ - Deprecated in 26.0
- tvOS 17.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
typealias GKChallengeComposeHandler = (UIViewController, Bool, [GKPlayer]?) -> Void
```

*macOS*

```swift
typealias GKChallengeComposeHandler = (NSViewController, Bool, [GKPlayer]?) -> Void
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```c
typedef void (^)(UIViewController *, _Bool, NSArray<GKPlayer *> *) GKChallengeComposeHandler;
```

*macOS*

```c
typedef void (^)(NSViewController *, _Bool, NSArray<GKPlayer *> *) GKChallengeComposeHandler;
```

## Parameters

- `composeController`: The view controller for the challenge.
- `didIssueChallenge`: A Boolean value that indicates whether the player issues the challenge.
- `sentPlayers`: The players that receive the challenge.

## See Also

### Issuing Achievement Challenges
- [func selectChallengeablePlayers([GKPlayer], withCompletionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](./gkachievement/selectchallengeableplayers%28_,withcompletionhandler%29.md)
  Finds the subset of players who can earn an achievement.
- [func challengeComposeController(withMessage: String?, players: [GKPlayer], completion: GKChallengeComposeHandler?) -> UIViewController](./gkachievement/challengecomposecontroller%28withmessage,players,completion%29.md)
  Provides a view controller that you present to the player to issue an achievement challenge.
- [func challengeComposeController(withMessage: String?, players: [GKPlayer], completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController](./gkachievement/challengecomposecontroller%28withmessage,players,completionhandler%29.md)
  Provides a view controller that you present to the player to issue an achievement challenge.
- [func challengeComposeController(withPlayers: [String]?, message: String?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController?](./gkachievement/challengecomposecontroller%28withplayers,message,completionhandler%29.md)
  Provides a challenge compose view controller with preselected player identifiers and a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengecomposehandler)*