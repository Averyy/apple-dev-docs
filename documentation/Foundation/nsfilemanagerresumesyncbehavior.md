# NSFileManagerResumeSyncBehavior

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

The behaviors the file manager can apply to resolve conflicts when resuming a sync.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum NSFileManagerResumeSyncBehavior
```

```c
enum NSFileManagerResumeSyncBehavior : NSInteger;
```

#### Overview

You use this type when calling [`resumeSyncForUbiquitousItem(at:with:completionHandler:)`](./filemanager/resumesyncforubiquitousitem%28at,with,completionhandler%29.md) to resume synchronizing. In most situations, the [`NSFileManagerResumeSyncBehavior.preserveLocalChanges`](./nsfilemanagerresumesyncbehavior/preservelocalchanges.md) behavior is the best choice to avoid risk of data loss.

## Topics

### Identifying sync behaviors
- [NSFileManagerResumeSyncBehavior.preserveLocalChanges](./nsfilemanagerresumesyncbehavior/preservelocalchanges.md)
  Resumes synchronizing by uploading the local version of the file.
- [NSFileManagerResumeSyncBehavior.afterUploadWithFailOnConflict](./nsfilemanagerresumesyncbehavior/afteruploadwithfailonconflict.md)
  Resumes sync by first uploading the local version of the file, failing if the provider detects a conflict.
- [NSFileManagerResumeSyncBehavior.dropLocalChanges](./nsfilemanagerresumesyncbehavior/droplocalchanges.md)
  Resumes synchronizing by overwriting any local changes with the remote version of the file.
### Working with raw values
- [init?(rawValue: Int)](./nsfilemanagerresumesyncbehavior/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Controlling file provider synchronization
- [struct NSFileManagerSupportedSyncControls](./nsfilemanagersupportedsynccontrols.md)
  An option set of the sync controls available for an item.
- [func pauseSyncForUbiquitousItem(at: URL, completionHandler: ((any Error)?) -> Void)](./filemanager/pausesyncforubiquitousitem%28at,completionhandler%29.md)
  Asynchronously pauses sync of an item at the given URL.
- [func resumeSyncForUbiquitousItem(at: URL, with: NSFileManagerResumeSyncBehavior, completionHandler: ((any Error)?) -> Void)](./filemanager/resumesyncforubiquitousitem%28at,with,completionhandler%29.md)
  Asynchronously resumes the sync on a paused item using the given resume behavior.
- [func fetchLatestRemoteVersionOfItem(at: URL, completionHandler: (NSFileVersion?, (any Error)?) -> Void)](./filemanager/fetchlatestremoteversionofitem%28at,completionhandler%29.md)
  Asynchronously fetches the latest remote version of a given item from the server.
- [class NSFileVersion](./nsfileversion.md)
  A snapshot of a file at a specific point in time.
- [func uploadLocalVersionOfUbiquitousItem(at: URL, withConflictResolutionPolicy: NSFileManagerUploadLocalVersionConflictPolicy, completionHandler: (NSFileVersion?, (any Error)?) -> Void)](./filemanager/uploadlocalversionofubiquitousitem%28at,withconflictresolutionpolicy,completionhandler%29.md)
  Asynchronously uploads the local version of the item using the provided conflict resolution policy.
- [enum NSFileManagerUploadLocalVersionConflictPolicy](./nsfilemanageruploadlocalversionconflictpolicy.md)
  The policies the file manager can apply to resolve conflicts when uploading a local version of a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilemanagerresumesyncbehavior)*