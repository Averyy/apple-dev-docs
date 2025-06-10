# openDirectory(containerIdentifier:)

**Framework**: GameSave  
**Kind**: method

Requests an instance of the game-save directory.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class func openDirectory(containerIdentifier: String? = nil) -> GameSyncedDirectory
```

#### Discussion

This method returns immediately, and starts syncing the directory in the background. To wait for syncing to complete, call the [`finishSyncing()`](gamesynceddirectory/finishsyncing().md) method.

## Parameters

- `containerIdentifier`: The identifier of the directory to request.   If you pass  , this method uses the first container identifier   listed in the   entitlements array.

## See Also

- [GameSyncedDirectory.State](gamesynceddirectory/state-swift.enum.md)
  The state of the directory.
- [var state: GameSyncedDirectory.State](gamesynceddirectory/state-swift.property.md)
  The state that the game-save directory is in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesynceddirectory/opendirectory(containeridentifier:))*