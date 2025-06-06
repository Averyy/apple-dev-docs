# player(_:didModifySavedGame:)

**Framework**: GameKit  
**Kind**: method

Handles when data changes in a saved game file.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
optional func player(_ player: GKPlayer, didModifySavedGame savedGame: GKSavedGame)
```

#### Discussion

GameKit invokes this method when you save game data on a device that isn’t the user’s current device.

## Parameters

- `player`: The player who saves the game data.
- `savedGame`: The game the player saves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksavedgamelistener/player(_:didmodifysavedgame:))*