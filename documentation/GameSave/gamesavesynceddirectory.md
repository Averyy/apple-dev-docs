# GameSaveSyncedDirectory

**Framework**: GameSave  
**Kind**: class

A cloud-synced directory for game-save data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class GameSaveSyncedDirectory
```

#### Overview

To get an instance of the directory, call [`openDirectory(containerIdentifier:)`](gamesavesynceddirectory/opendirectory(containeridentifier:).md), which returns the directory for the iCloud container associated with the specified identifier. Calling this method starts syncing the directory in the background on the specified container. When the game needs to access the contents of the directory, show a UI while the directory fully syncs using the [`gameSaveSyncingAlert(directory:finishedLoading:)`](https://developer.apple.com/documentation/SwiftUI/View/gameSaveSyncingAlert(directory:finishedLoading:)) view extension if your app uses SwiftUI, the [`finishSyncing(statusDisplay:)`](gamesavesynceddirectory/finishsyncing(statusdisplay:)-500el.md) method if your app uses UIKit, or the [`finishSyncing(statusDisplay:)`](gamesavesynceddirectory/finishsyncing(statusdisplay:)-309nq.md) method if your app uses AppKit.

If you’re showing your own UI, call the [`finishSyncing()`](gamesavesynceddirectory/finishsyncing().md) method to wait for the directory to finish syncing.

After the directory is ready to use, syncing pauses until you close the directory object or the object is deallocated. To resume syncing during the game, close and re-open the directory by calling [`close()`](gamesavesynceddirectory/close().md) and then [`openDirectory(containerIdentifier:)`](gamesavesynceddirectory/opendirectory(containeridentifier:).md).

## Topics

### Accessing a directory
- [class func openDirectory(containerIdentifier: String?) -> GameSaveSyncedDirectory](gamesavesynceddirectory/opendirectory(containeridentifier:).md)
  Requests an instance of the game-save directory.
- [GameSaveSyncedDirectory.State](gamesavesynceddirectory/state-swift.enum.md)
  The state of the directory.
- [var state: GameSaveSyncedDirectory.State](gamesavesynceddirectory/state-swift.property.md)
  The state that the game-save directory is in.
### Syncing a directory
- [func finishSyncing() async](gamesavesynceddirectory/finishsyncing.md)
  Waits for the directory sync to complete, without showing any user interface.
- [func finishSyncing(statusDisplay: NSWindow) async](gamesavesynceddirectory/finishsyncing(statusdisplay:)-309nq.md)
  Waits for the directory sync to complete, showing the sync’s progress in a modal alert.
- [func finishSyncing(statusDisplay: UIWindow) async](gamesavesynceddirectory/finishsyncing(statusdisplay:)-500el.md)
  Waits for the directory sync to complete, showing the sync’s progress in a modal alert.
### Resolving conflicts
- [GameSaveSyncedDirectory.Version](gamesavesynceddirectory/version.md)
  A representation of a version of the directory.
- [func resolveConflicts(with: GameSaveSyncedDirectory.Version)](gamesavesynceddirectory/resolveconflicts(with:).md)
  Indicates that you resolved a conflict.
### Finishing with a directory
- [func triggerPendingUpload() async -> Bool](gamesavesynceddirectory/triggerpendingupload.md)
  Triggers an upload of the directory for any changes that were pending.
- [func close()](gamesavesynceddirectory/close.md)
  Closes the directory, and resumes syncing the directory to the cloud.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory)*