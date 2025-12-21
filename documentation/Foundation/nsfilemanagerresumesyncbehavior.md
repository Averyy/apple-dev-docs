# NSFileManagerResumeSyncBehavior

**Framework**: Foundation  
**Kind**: enum

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

#### Overview

You use this type when calling [`resumeSyncForUbiquitousItem(at:with:completionHandler:)`](filemanager/resumesyncforubiquitousitem(at:with:completionhandler:).md) to resume synchronizing. In most situations, the [`NSFileManagerResumeSyncBehavior.preserveLocalChanges`](nsfilemanagerresumesyncbehavior/preservelocalchanges.md) behavior is the best choice to avoid risk of data loss.

## Topics

### Identifying sync behaviors
- [NSFileManagerResumeSyncBehavior.preserveLocalChanges](nsfilemanagerresumesyncbehavior/preservelocalchanges.md)
  Resumes synchronizing by uploading the local version of the file.
- [NSFileManagerResumeSyncBehavior.afterUploadWithFailOnConflict](nsfilemanagerresumesyncbehavior/afteruploadwithfailonconflict.md)
  Resumes sync by first uploading the local version of the file, failing if the provider detects a conflict.
- [NSFileManagerResumeSyncBehavior.dropLocalChanges](nsfilemanagerresumesyncbehavior/droplocalchanges.md)
  Resumes synchronizing by overwriting any local changes with the remote version of the file.
### Working with raw values
- [init?(rawValue: Int)](nsfilemanagerresumesyncbehavior/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct NSFileManagerSupportedSyncControls](nsfilemanagersupportedsynccontrols.md)
  An option set of the sync controls available for an item.
- [func pauseSyncForUbiquitousItem(at: URL, completionHandler: ((any Error)?) -> Void)](filemanager/pausesyncforubiquitousitem(at:completionhandler:).md)
  Asynchronously pauses sync of an item at the given URL.
- [func resumeSyncForUbiquitousItem(at: URL, with: NSFileManagerResumeSyncBehavior, completionHandler: ((any Error)?) -> Void)](filemanager/resumesyncforubiquitousitem(at:with:completionhandler:).md)
  Asynchronously resumes the sync on a paused item using the given resume behavior.
- [func fetchLatestRemoteVersionOfItem(at: URL, completionHandler: (NSFileVersion?, (any Error)?) -> Void)](filemanager/fetchlatestremoteversionofitem(at:completionhandler:).md)
  Asynchronously fetches the latest remote version of a given item from the server.
- [class NSFileVersion](nsfileversion.md)
  A snapshot of a file at a specific point in time.
- [func uploadLocalVersionOfUbiquitousItem(at: URL, withConflictResolutionPolicy: NSFileManagerUploadLocalVersionConflictPolicy, completionHandler: (NSFileVersion?, (any Error)?) -> Void)](filemanager/uploadlocalversionofubiquitousitem(at:withconflictresolutionpolicy:completionhandler:).md)
  Asynchronously uploads the local version of the item using the provided conflict resolution policy.
- [enum NSFileManagerUploadLocalVersionConflictPolicy](nsfilemanageruploadlocalversionconflictpolicy.md)
  The policies the file manager can apply to resolve conflicts when uploading a local version of a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilemanagerresumesyncbehavior)*