# GKChallengeComposeCompletionBlock

**Framework**: GameKit  
**Kind**: typealias

A completion block that provides information about the player who issues a challenge and the players who receive it.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias GKChallengeComposeCompletionBlock = (NSViewController, Bool, [String]?) -> Void
```

## Parameters

- `composeController`: View controller for the challenge.
- `didIssueChallenge`: A Boolean value that indicates whether the player issues the challenge.
- `sentPlayerIDs`: The identifiers for the players that receive the challenge.

## See Also

- [var issuingPlayerID: String?](gkchallenge/issuingplayerid.md)
  The player who issues the challenge.
- [var receivingPlayerID: String?](gkchallenge/receivingplayerid.md)
  The player who receives the challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengecomposecompletionblock)*