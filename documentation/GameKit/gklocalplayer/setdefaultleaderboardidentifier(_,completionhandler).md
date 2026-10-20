# setDefaultLeaderboardIdentifier(_:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Sets the local player’s default leaderboard.

**Availability**:
- iOS 7.0+ - Deprecated in 26.2
- iPadOS 7.0+ - Deprecated in 26.2
- Mac Catalyst 13.1+ - Deprecated in 26.2
- macOS 10.10+ - Deprecated in 26.2
- tvOS 9.0+ - Deprecated in 26.2
- visionOS 1.0+ - Deprecated in 26.2
- watchOS 3.0+ - Deprecated in 26.2

> **Deprecated**: No longer supported

## Declaration

```swift
func setDefaultLeaderboardIdentifier(_ leaderboardIdentifier: String, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func setDefaultLeaderboardIdentifier(_ leaderboardIdentifier: String) async throws
```

```objc
- (void) setDefaultLeaderboardIdentifier:(NSString *) leaderboardIdentifier completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Mentions

- [Encourage progress and competition with leaderboards](../encourage-progress-and-competition-with-leaderboards.md)

#### Discussion

Until you change the default leaderboard for a player, it is the same as the default leaderboard for your game that you set in App Store Connect.

## Parameters

- `leaderboardIdentifier`: The identifier of the leaderboard.
- `completionHandler`: The block that GameKit calls when it completes the request.

  The block receives the following parameters:

  - **error**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Working with Leaderboards
- [func loadDefaultLeaderboardIdentifier(completionHandler: ((String?, (any Error)?) -> Void)?)](./loaddefaultleaderboardidentifier%28completionhandler%29.md)
  Loads the identifier for the local player’s default leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/setdefaultleaderboardidentifier(_:completionhandler:))*