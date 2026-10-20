# selectChallengeablePlayers(_:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Finds the subset of players who can earn an achievement.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.10+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
func selectChallengeablePlayers(_ players: [GKPlayer], withCompletionHandler completionHandler: (@Sendable ([GKPlayer]?, (any Error)?) -> Void)? = nil)
```

```swift
func selectChallengeablePlayers(_ players: [GKPlayer]) async throws -> [GKPlayer]
```

```objc
- (void) selectChallengeablePlayers:(NSArray<GKPlayer *> *) players withCompletionHandler:(void (^)(NSArray<GKPlayer *> *challengeablePlayers, NSError *error)) completionHandler;
```

## Parameters

- `players`: A list of players that GameKit uses to find players who are eligible to earn the achievement.
- `completionHandler`: A block that GameKit calls when this method completes.

  The block receives the following parameters:

  - **`challengeablePlayers`**: The players in the `players` parameter who are able to earn the achievement.
  - **`error`**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Issuing Achievement Challenges
- [func challengeComposeController(withMessage: String?, players: [GKPlayer], completion: GKChallengeComposeHandler?) -> UIViewController](./challengecomposecontroller%28withmessage,players,completion%29.md)
  Provides a view controller that you present to the player to issue an achievement challenge.
- [typealias GKChallengeComposeHandler](../gkchallengecomposehandler.md)
  A completion block that provides information about the player who issues a challenge and the players who receive it.
- [func challengeComposeController(withMessage: String?, players: [GKPlayer], completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController](./challengecomposecontroller%28withmessage,players,completionhandler%29.md)
  Provides a view controller that you present to the player to issue an achievement challenge.
- [func challengeComposeController(withPlayers: [String]?, message: String?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController?](./challengecomposecontroller%28withplayers,message,completionhandler%29.md)
  Provides a challenge compose view controller with preselected player identifiers and a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/selectchallengeableplayers(_:withcompletionhandler:))*