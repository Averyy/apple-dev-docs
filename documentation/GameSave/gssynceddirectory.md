# GSSyncedDirectory

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
class GSSyncedDirectory
```

#### Overview

To get an instance of the directory, call [`open(forContainerIdentifier:)`](gssynceddirectory/open(forcontaineridentifier:).md), which returns the directory for the iCloud container associated with the specified identifier. Calling this method starts syncing the directory in the background on the specified container. When the game needs to access the contents of the directory, show a UI while the directory fully syncs using the [`finishSyncing(_:completionHandler:)`](gssynceddirectory/finishsyncing(_:completionhandler:).md) method. If you’re showing your own UI, call the [`finishSyncing(completionHandler:)`](gssynceddirectory/finishsyncing(completionhandler:).md) method to wait for the directory to finish syncing.

After the directory is ready to use, syncing pauses until you close the directory object or the object is deallocated. To resume syncing during the game, close and re-open the directory by calling [`close()`](gssynceddirectory/close().md) and then [`open(forContainerIdentifier:)`](gssynceddirectory/open(forcontaineridentifier:).md).

## Topics

### Accessing a directory
- [class func open(forContainerIdentifier: String?) -> GSSyncedDirectory](gssynceddirectory/open(forcontaineridentifier:).md)
  Requests an instance of the game-save directory.
- [var directoryState: GSSyncedDirectoryState](gssynceddirectory/directorystate.md)
  The state of the directory.
- [class GSSyncedDirectoryState](gssynceddirectorystate.md)
  Represents the state and its associated properties of the directory
### Syncing a directory
- [func finishSyncing(UIWindow, completionHandler: () -> Void)](gssynceddirectory/finishsyncing(_:completionhandler:).md)
  Waits for the directory sync to complete, showing the sync’s progress in a modal alert.
- [func finishSyncing(completionHandler: () -> Void)](gssynceddirectory/finishsyncing(completionhandler:).md)
  Waits for the directory sync to complete, without showing any user interface.
### Resolving conflicts
- [class GSSyncedDirectoryVersion](gssynceddirectoryversion.md)
- [func resolveConflicts(with: GSSyncedDirectoryVersion)](gssynceddirectory/resolveconflicts(with:).md)
  Indicates that you resolved a conflict.
### Finishing with a directory
- [func triggerPendingUpload(completionHandler: (Bool) -> Void)](gssynceddirectory/triggerpendingupload(completionhandler:).md)
  Triggers an upload of the directory for any changes that were pending.
- [func close()](gssynceddirectory/close.md)
  Closes the directory, and resumes syncing the directory to the cloud.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectory)*