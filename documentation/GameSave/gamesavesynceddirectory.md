# GameSaveSyncedDirectory

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
class GameSaveSyncedDirectory
```

#### Overview

To get an instance of the directory, call [`openDirectory(containerIdentifier:)`](gamesavesynceddirectory/opendirectory(containeridentifier:).md), which returns the directory for the iCloud container associated with the specified identifier. Calling this method starts syncing the directory in the background on the specified container. When the game needs to access the contents of the directory, show a UI while the directory fully syncs using the doc://com.apple.documentation/documentation/swiftui/view/gamesavesyncingview(directory:finishedloading:) view extension if your app uses SwiftUI, the [`finishSyncing(statusDisplay:)`](gamesavesynceddirectory/finishsyncing(statusdisplay:)-500el.md) method if your app uses UIKit, or the [`finishSyncing(statusDisplay:)`](gamesavesynceddirectory/finishsyncing(statusdisplay:)-309nq.md) method if your app uses AppKit.

If you’re showing your own UI, call the [`finishSyncing()`](gamesavesynceddirectory/finishsyncing().md) method to wait for the directory to finish syncing.

After the directory is ready to use, syncing pauses until you close the directory object or the object is deallocated. To resume syncing during the game, close and re-open the directory by calling [`close()`](gamesavesynceddirectory/close().md) and then [`openDirectory(containerIdentifier:)`](gamesavesynceddirectory/opendirectory(containeridentifier:).md).

## Topics

### Classes
- [GameSaveSyncedDirectory.Version](gamesavesynceddirectory/version.md)
  A representation of a version of the directory.
### Operators
- [static func == (GameSaveSyncedDirectory, GameSaveSyncedDirectory) -> Bool](gamesavesynceddirectory/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var id: String](gamesavesynceddirectory/id-swift.property.md)
  The stable identity of the entity associated with this instance.
- [var state: GameSaveSyncedDirectory.State](gamesavesynceddirectory/state-swift.property.md)
  The state that the game-save directory is in.
### Instance Methods
- [func close()](gamesavesynceddirectory/close.md)
  Closes the directory, and resumes syncing the directory to the cloud.
- [func finishSyncing() async](gamesavesynceddirectory/finishsyncing.md)
  Waits for the directory sync to complete, without showing any user interface.
- [func finishSyncing(statusDisplay: NSWindow) async](gamesavesynceddirectory/finishsyncing(statusdisplay:)-309nq.md)
  Waits for the directory sync to complete, showing the sync’s progress in a modal alert.
- [func finishSyncing(statusDisplay: UIWindow) async](gamesavesynceddirectory/finishsyncing(statusdisplay:)-500el.md)
  Waits for the directory sync to complete, showing the sync’s progress in a modal alert.
- [func resolveConflicts(with: GameSaveSyncedDirectory.Version)](gamesavesynceddirectory/resolveconflicts(with:).md)
  Indicates that you resolved a conflict.
- [func triggerPendingUpload() async -> Bool](gamesavesynceddirectory/triggerpendingupload.md)
  Triggers an upload of the directory for any changes that were pending.
### Type Aliases
- [GameSaveSyncedDirectory.ID](gamesavesynceddirectory/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Type Methods
- [class func openDirectory(containerIdentifier: String?) -> GameSaveSyncedDirectory](gamesavesynceddirectory/opendirectory(containeridentifier:).md)
  Requests an instance of the game-save directory.
### Enumerations
- [GameSaveSyncedDirectory.State](gamesavesynceddirectory/state-swift.enum.md)
  The state of the directory.
### Default Implementations
- [Equatable Implementations](gamesavesynceddirectory/equatable-implementations.md)

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