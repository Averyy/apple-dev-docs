# GKChallengeComposeCompletionBlock

**Framework**: GameKit  
**Kind**: typealias  
**Role**: Type Alias

A completion block that provides information about the player who issues a challenge and the players who receive it.

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
typealias GKChallengeComposeCompletionBlock = (UIViewController, Bool, [String]?) -> Void
```

*macOS*

```swift
typealias GKChallengeComposeCompletionBlock = (NSViewController, Bool, [String]?) -> Void
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```c
typedef void (^)(UIViewController *, _Bool, NSArray<NSString *> *) GKChallengeComposeCompletionBlock;
```

*macOS*

```c
typedef void (^)(NSViewController *, _Bool, NSArray<NSString *> *) GKChallengeComposeCompletionBlock;
```

## Parameters

- `composeController`: View controller for the challenge.
- `didIssueChallenge`: A Boolean value that indicates whether the player issues the challenge.
- `sentPlayerIDs`: The identifiers for the players that receive the challenge.

## See Also

### Deprecated symbols
- [var issuingPlayerID: String?](./gkchallenge/issuingplayerid.md)
  The player who issues the challenge.
- [var receivingPlayerID: String?](./gkchallenge/receivingplayerid.md)
  The player who receives the challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengecomposecompletionblock)*