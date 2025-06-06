# addPlayers(to:)

**Framework**: GameKit  
**Kind**: method

Invites additional players to join an existing match.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addPlayers(to match: GKMatch)
```

#### Discussion

Call this method prior to presenting the view controller to the player. This method updates the view controller’s interface to show the players already connected to the match.

> ❗ **Important**:  Invoke this method from the game instance of only one player connected to the match. Don’t add the same players from multiple game instances.

 Invoke this method from the game instance of only one player connected to the match. Don’t add the same players from multiple game instances.

## Parameters

- `match`: The match to which you want to add players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/addplayers(to:))*