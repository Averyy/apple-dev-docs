# showExistingMatches

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the view controller shows existing matches.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var showExistingMatches: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL showExistingMatches;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

## Discussion

If the value of this property is [`true`](../../Swift/true.md), the view controller shows matches that are in progress or complete. If the value of this property is [`false`](../../Swift/false.md), the view controller only offers the ability to create new matches. The default value is [`true`](../../Swift/true.md).

## See Also

### Creating and Configuring the View Controller
- [init(matchRequest: GKMatchRequest)](./init%28matchrequest%29.md)
  Creates a matchmaker view controller for the local player to start inviting other players to a turn-based game.
- [var matchmakingMode: GKMatchmakingMode](./matchmakingmode.md)
  The mode that a multiplayer game uses to find players.
- [enum GKMatchmakingMode](../gkmatchmakingmode.md)
  Possible modes that a multiplayer game uses to find matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller/showexistingmatches)*