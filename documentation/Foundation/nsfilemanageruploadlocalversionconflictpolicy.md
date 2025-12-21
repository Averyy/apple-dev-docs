# NSFileManagerUploadLocalVersionConflictPolicy

**Framework**: Foundation  
**Kind**: enum

The policies the file manager can apply to resolve conflicts when uploading a local version of a file.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum NSFileManagerUploadLocalVersionConflictPolicy
```

## Topics

### Working with conflict policies
- [NSFileManagerUploadLocalVersionConflictPolicy.conflictPolicyDefault](nsfilemanageruploadlocalversionconflictpolicy/conflictpolicydefault.md)
  Resolves the conflict using the policy defined by the file provider.
- [NSFileManagerUploadLocalVersionConflictPolicy.conflictPolicyFailOnConflict](nsfilemanageruploadlocalversionconflictpolicy/conflictpolicyfailonconflict.md)
  Resolves the conflict by causing the upload to fail.
### Working with raw values
- [init?(rawValue: Int)](nsfilemanageruploadlocalversionconflictpolicy/init(rawvalue:).md)

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
- [enum NSFileManagerResumeSyncBehavior](nsfilemanagerresumesyncbehavior.md)
  The behaviors the file manager can apply to resolve conflicts when resuming a sync.
- [func fetchLatestRemoteVersionOfItem(at: URL, completionHandler: (NSFileVersion?, (any Error)?) -> Void)](filemanager/fetchlatestremoteversionofitem(at:completionhandler:).md)
  Asynchronously fetches the latest remote version of a given item from the server.
- [class NSFileVersion](nsfileversion.md)
  A snapshot of a file at a specific point in time.
- [func uploadLocalVersionOfUbiquitousItem(at: URL, withConflictResolutionPolicy: NSFileManagerUploadLocalVersionConflictPolicy, completionHandler: (NSFileVersion?, (any Error)?) -> Void)](filemanager/uploadlocalversionofubiquitousitem(at:withconflictresolutionpolicy:completionhandler:).md)
  Asynchronously uploads the local version of the item using the provided conflict resolution policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilemanageruploadlocalversionconflictpolicy)*