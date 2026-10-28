# GameSaveSyncedDirectory

**Framework**: GameSave  
**Kind**: class  
**Role**: Class

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

## Overview

To get an instance of the directory, call [`openDirectory(containerIdentifier:)`](./gamesavesynceddirectory/opendirectory%28containeridentifier%29.md), which returns the directory for the iCloud container associated with the specified identifier. Calling this method starts syncing the directory in the background on the specified container. When the game needs to access the contents of the directory, show a UI while the directory fully syncs using the [`gameSaveSyncingAlert(directory:finishedLoading:)`](../SwiftUI/view/gamesavesyncingalert%28directory,finishedloading%29.md) view extension if your app uses SwiftUI, the [`finishSyncing(statusDisplay:)`](./gamesavesynceddirectory/finishsyncing%28statusdisplay%29-500el.md) method if your app uses UIKit, or the [`finishSyncing(statusDisplay:)`](./gamesavesynceddirectory/finishsyncing%28statusdisplay%29-309nq.md) method if your app uses AppKit.

If you’re showing your own UI, call the [`finishSyncing()`](./gamesavesynceddirectory/finishsyncing%28%29.md) method to wait for the directory to finish syncing.

After the directory is ready to use, syncing pauses until you close the directory object or the object is deallocated. To resume syncing during the game, close and re-open the directory by calling [`close()`](./gamesavesynceddirectory/close%28%29.md) and then [`openDirectory(containerIdentifier:)`](./gamesavesynceddirectory/opendirectory%28containeridentifier%29.md).

## Topics

### Accessing a directory
- [class func openDirectory(containerIdentifier: String?) -> GameSaveSyncedDirectory](./gamesavesynceddirectory/opendirectory%28containeridentifier%29.md)
  Requests an instance of the game-save directory.
- [GameSaveSyncedDirectory.State](./gamesavesynceddirectory/state-swift.enum.md)
  The state of the directory.
- [var state: GameSaveSyncedDirectory.State](./gamesavesynceddirectory/state-swift.property.md)
  The state that the game-save directory is in.
### Syncing a directory
- [func finishSyncing() async](./gamesavesynceddirectory/finishsyncing%28%29.md)
  Waits for the directory sync to complete, without showing any user interface.
- [func finishSyncing(statusDisplay: NSWindow) async](./gamesavesynceddirectory/finishsyncing%28statusdisplay%29-309nq.md)
  Waits for the directory sync to complete, showing the sync’s progress in a modal alert.
- [func finishSyncing(statusDisplay: UIWindow) async](./gamesavesynceddirectory/finishsyncing%28statusdisplay%29-500el.md)
  Waits for the directory sync to complete, showing the sync’s progress in a modal alert.
### Resolving conflicts
- [GameSaveSyncedDirectory.Version](./gamesavesynceddirectory/version.md)
  A representation of a version of the directory.
- [func resolveConflicts(with: GameSaveSyncedDirectory.Version)](./gamesavesynceddirectory/resolveconflicts%28with%29.md)
  Indicates that you resolved a conflict.
### Finishing with a directory
- [func triggerPendingUpload() async -> Bool](./gamesavesynceddirectory/triggerpendingupload%28%29.md)
  Triggers an upload of the directory for any changes that were pending.
- [func close()](./gamesavesynceddirectory/close%28%29.md)
  Closes the directory, and resumes syncing the directory to the cloud.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Identifiable](../Swift/identifiable.md)
- [Observable](../Observation/observable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory)*