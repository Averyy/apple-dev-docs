# openDirectory(containerIdentifier:)

**Framework**: GameSave  
**Kind**: method

Requests an instance of the game-save directory.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class func openDirectory(containerIdentifier: String? = nil) -> GameSaveSyncedDirectory
```

#### Discussion

This method returns immediately, and starts syncing the directory in the background. To wait for syncing to complete, call the [`finishSyncing()`](gamesavesynceddirectory/finishsyncing().md) method.

## Parameters

- `containerIdentifier`: The identifier of the directory to request.   If you pass  , this method uses the first container identifier   listed in the   entitlements array.

## See Also

- [GameSaveSyncedDirectory.State](gamesavesynceddirectory/state-swift.enum.md)
  The state of the directory.
- [var state: GameSaveSyncedDirectory.State](gamesavesynceddirectory/state-swift.property.md)
  The state that the game-save directory is in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory/opendirectory(containeridentifier:))*