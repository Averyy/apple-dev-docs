# fetchLatestRemoteVersionOfItem(at:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Asynchronously fetches the latest remote version of a given item from the server.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func fetchLatestRemoteVersionOfItem(at url: URL) async throws -> NSFileVersion
```

#### Discussion

Use this method if uploading fails due to a version conflict and sync is paused. In this case, fetching the latest remote version allows you to inspect the newer item from the server, resolve the conflict, and resume uploading.

The version provided by this call depends on several factors:

- If there is no newer version of the file on the server, the caller receives the current version of the file.
- If the server has a newer version and sync isn’t paused, this call replaces the local item and provides the version of the new item.
- If the server has a newer version but sync is paused, the returned version points to a side location. In this case, call [`replaceItem(at:options:)`](nsfileversion/replaceitem(at:options:).md) on the provided version object to replace the local item with the newer item from the server.

If the device isn’t connected to the network, the call may fail with [`NSFileReadUnknownError`](nsfilereadunknownerror-c.enum.case.md), with the underlying error of [`serverUnreachable`](https://developer.apple.com/documentation/FileProvider/NSFileProviderError/serverUnreachable).

## Parameters

- `url`: The URL of the item for which to check the version.
- `completionHandler`: A closure or block that the framework calls when the fetch action completes. It receives parameters of types   and  . The error is   if fetching the remote version succeeded; otherwise it indicates the error that caused the call to fail. In Swift, you can omit the completion handler, catching any error in a  -  block and receiving the version as the return value.

## See Also

- [struct NSFileManagerSupportedSyncControls](nsfilemanagersupportedsynccontrols.md)
  An option set of the sync controls available for an item.
- [func pauseSyncForUbiquitousItem(at: URL, completionHandler: ((any Error)?) -> Void)](filemanager/pausesyncforubiquitousitem(at:completionhandler:).md)
  Asynchronously pauses sync of an item at the given URL.
- [func resumeSyncForUbiquitousItem(at: URL, with: NSFileManagerResumeSyncBehavior, completionHandler: ((any Error)?) -> Void)](filemanager/resumesyncforubiquitousitem(at:with:completionhandler:).md)
  Asynchronously resumes the sync on a paused item using the given resume behavior.
- [enum NSFileManagerResumeSyncBehavior](nsfilemanagerresumesyncbehavior.md)
  The behaviors the file manager can apply to resolve conflicts when resuming a sync.
- [class NSFileVersion](nsfileversion.md)
  A snapshot of a file at a specific point in time.
- [func uploadLocalVersionOfUbiquitousItem(at: URL, withConflictResolutionPolicy: NSFileManagerUploadLocalVersionConflictPolicy, completionHandler: (NSFileVersion?, (any Error)?) -> Void)](filemanager/uploadlocalversionofubiquitousitem(at:withconflictresolutionpolicy:completionhandler:).md)
  Asynchronously uploads the local version of the item using the provided conflict resolution policy.
- [enum NSFileManagerUploadLocalVersionConflictPolicy](nsfilemanageruploadlocalversionconflictpolicy.md)
  The policies the file manager can apply to resolve conflicts when uploading a local version of a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/fetchlatestremoteversionofitem(at:completionhandler:))*