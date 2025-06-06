# init(matchRequest:)

**Framework**: GameKit  
**Kind**: init

Creates a matchmaker view controller for the local player to start inviting other players to a turn-based game.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
init(matchRequest request: GKMatchRequest)
```

#### Return Value

An initialized matchmaker view controller object or `nil` If an error occurs.

## Parameters

- `request`: A match request that you configure for the characteristics of your game.

## See Also

- [var showExistingMatches: Bool](gkturnbasedmatchmakerviewcontroller/showexistingmatches.md)
  A Boolean value that determines whether the view controller shows existing matches.
- [var matchmakingMode: GKMatchmakingMode](gkturnbasedmatchmakerviewcontroller/matchmakingmode.md)
  The mode that a multiplayer game uses to find players.
- [enum GKMatchmakingMode](gkmatchmakingmode.md)
  Possible modes that a multiplayer game uses to find matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller/init(matchrequest:))*