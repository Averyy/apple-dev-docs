# GameSyncedDirectory

**Framework**: GameSave  
**Kind**: class

A cloud-synced directory for game-save data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class GameSyncedDirectory
```

#### Overview

To get an instance of the directory, call [`openDirectory(containerIdentifier:)`](gamesynceddirectory/opendirectory(containeridentifier:).md), which returns the directory for the iCloud container associated with the specified identifier. Calling this method starts syncing the directory in the background on the specified container. When the game needs to access the contents of the directory, show a UI while the directory fully syncs using the [`gameSyncedDirectoryLoadingView(directory:finishedLoading:)`](https://developer.apple.com/documentation/SwiftUI/View/gameSyncedDirectoryLoadingView(directory:finishedLoading:)) view extension if your app uses SwiftUI, the [`finishSyncing(statusDisplay:)`](gamesynceddirectory/finishsyncing(statusdisplay:)-6v7lz.md) method if your app uses UIKit, or the [`finishSyncing(statusDisplay:)`](gamesynceddirectory/finishsyncing(statusdisplay:)-2uvh2.md) method if your app uses AppKit.

If you’re showing your own UI, call the [`finishSyncing()`](gamesynceddirectory/finishsyncing().md) method to wait for the directory to finish syncing.

After the directory is ready to use, syncing pauses until you close the directory object or the object is deallocated. To resume syncing during the game, close and re-open the directory by calling [`close()`](gamesynceddirectory/close().md) and then [`openDirectory(containerIdentifier:)`](gamesynceddirectory/opendirectory(containeridentifier:).md).

## Topics

### Accessing a directory
- [class func openDirectory(containerIdentifier: String?) -> GameSyncedDirectory](gamesynceddirectory/opendirectory(containeridentifier:).md)
  Requests an instance of the game-save directory.
- [GameSyncedDirectory.State](gamesynceddirectory/state-swift.enum.md)
  The state of the directory.
- [var state: GameSyncedDirectory.State](gamesynceddirectory/state-swift.property.md)
  The state that the game-save directory is in.
### Syncing a directory
- [func finishSyncing() async](gamesynceddirectory/finishsyncing.md)
  Waits for the directory sync to complete, without showing any user interface.
- [func finishSyncing(statusDisplay: NSWindow) async](gamesynceddirectory/finishsyncing(statusdisplay:)-2uvh2.md)
  Waits for the directory sync to complete, showing the sync’s progress in a modal alert.
- [func finishSyncing(statusDisplay: UIWindow) async](gamesynceddirectory/finishsyncing(statusdisplay:)-6v7lz.md)
  Waits for the directory sync to complete, showing the sync’s progress in a modal alert.
### Resolving conflicts
- [GameSyncedDirectory.Version](gamesynceddirectory/version.md)
  A representation of a version of the directory.
- [func resolveConflicts(with: GameSyncedDirectory.Version)](gamesynceddirectory/resolveconflicts(with:).md)
  Indicates that you resolved a conflict.
### Finishing with a directory
- [func triggerPendingUpload() async -> Bool](gamesynceddirectory/triggerpendingupload.md)
  Triggers an upload of the directory for any changes that were pending.
- [func close()](gamesynceddirectory/close.md)
  Closes the directory, and resumes syncing the directory to the cloud.
### Comparing directories
- [GameSyncedDirectory.ID](gamesynceddirectory/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
- [var id: String](gamesynceddirectory/id-swift.property.md)
  The stable identity of the entity associated with this instance.
- [static func == (GameSyncedDirectory, GameSyncedDirectory) -> Bool](gamesynceddirectory/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](gamesynceddirectory/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesynceddirectory)*