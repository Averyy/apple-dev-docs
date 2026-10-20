# player(_:hasConflictingSavedGames:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Chooses the correct game data from the saved games that contain conflicts.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
optional func player(_ player: GKPlayer, hasConflictingSavedGames savedGames: [GKSavedGame])
```

```objc
- (void) player:(GKPlayer *) player hasConflictingSavedGames:(NSArray<GKSavedGame *> *) savedGames;
```

## Mentions

- [Saving the player’s game data to an iCloud account](../saving-the-player-s-game-data-to-an-icloud-account.md)

#### Discussion

Saved game files conflict when multiple devices write to the same file while one or more of the devices are offline. Implement this method to choose the game data that’s correct and try saving it again using the [`resolveConflictingSavedGames(_:with:completionHandler:)`](../gklocalplayer/resolveconflictingsavedgames%28_,with,completionhandler%29.md) method.

## Parameters

- `player`: The player who saves the game data.
- `savedGames`: The saved games that contain the conflicts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksavedgamelistener/player(_:hasconflictingsavedgames:))*