# loadDefaultLeaderboardIdentifier(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Loads the identifier for the local player’s default leaderboard.

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
func loadDefaultLeaderboardIdentifier(completionHandler: (@Sendable (String?, (any Error)?) -> Void)? = nil)
```

```swift
func loadDefaultLeaderboardIdentifier() async throws -> String
```

```objc
- (void) loadDefaultLeaderboardIdentifierWithCompletionHandler:(void (^)(NSString *leaderboardIdentifier, NSError *error)) completionHandler;
```

## Mentions

- [Encourage progress and competition with leaderboards](../encourage-progress-and-competition-with-leaderboards.md)

## Parameters

- `completionHandler`: The block that GameKit calls when it completes the request.

  The block receives the following parameters:

  - **categoryID**: The leaderboard ID for the local player’s default leaderboard that you set in App Store Connect.
  - **error**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Working with Leaderboards
- [func setDefaultLeaderboardIdentifier(String, completionHandler: (((any Error)?) -> Void)?)](./setdefaultleaderboardidentifier%28_,completionhandler%29.md)
  Sets the local player’s default leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/loaddefaultleaderboardidentifier(completionhandler:))*