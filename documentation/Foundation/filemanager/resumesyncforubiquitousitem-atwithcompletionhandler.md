# resumeSyncForUbiquitousItem(at:with:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Asynchronously resumes the sync on a paused item using the given resume behavior.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func resumeSyncForUbiquitousItem(at url: URL, with behavior: NSFileManagerResumeSyncBehavior) async throws
```

#### Discussion

Always call this method when your app closes an item to allow the file provider to sync local changes back to the server.

In most situations, the [`NSFileManagerResumeSyncBehavior.preserveLocalChanges`](nsfilemanagerresumesyncbehavior/preservelocalchanges.md) behavior is the best choice to avoid any risk of data loss.

The resume call fails with [`featureUnsupported`](cocoaerror/featureunsupported.md) if `url` isn’t currently paused. If the device isn’t connected to the network, the call may fail with [`NSFileWriteUnknownError`](nsfilewriteunknownerror-c.enum.case.md), with the underlying error of [`serverUnreachable`](https://developer.apple.com/documentation/FileProvider/NSFileProviderError/serverUnreachable).

## Parameters

- `url`: The URL of the item for which to resume sync.
- `behavior`: A   value that tells the file manager how to handle conflicts between local and remote versions of files.
- `completionHandler`: A closure or block that the framework calls when the resume action completes. It receives a single   parameter to indicate an error that prevented the resume action; the value is   if the resume succeeded. In Swift, you can omit the completion handler and catch the thrown error instead.

## See Also

- [struct NSFileManagerSupportedSyncControls](nsfilemanagersupportedsynccontrols.md)
  An option set of the sync controls available for an item.
- [func pauseSyncForUbiquitousItem(at: URL, completionHandler: ((any Error)?) -> Void)](filemanager/pausesyncforubiquitousitem(at:completionhandler:).md)
  Asynchronously pauses sync of an item at the given URL.
- [enum NSFileManagerResumeSyncBehavior](nsfilemanagerresumesyncbehavior.md)
  The behaviors the file manager can apply to resolve conflicts when resuming a sync.
- [func fetchLatestRemoteVersionOfItem(at: URL, completionHandler: (NSFileVersion?, (any Error)?) -> Void)](filemanager/fetchlatestremoteversionofitem(at:completionhandler:).md)
  Asynchronously fetches the latest remote version of a given item from the server.
- [class NSFileVersion](nsfileversion.md)
  A snapshot of a file at a specific point in time.
- [func uploadLocalVersionOfUbiquitousItem(at: URL, withConflictResolutionPolicy: NSFileManagerUploadLocalVersionConflictPolicy, completionHandler: (NSFileVersion?, (any Error)?) -> Void)](filemanager/uploadlocalversionofubiquitousitem(at:withconflictresolutionpolicy:completionhandler:).md)
  Asynchronously uploads the local version of the item using the provided conflict resolution policy.
- [enum NSFileManagerUploadLocalVersionConflictPolicy](nsfilemanageruploadlocalversionconflictpolicy.md)
  The policies the file manager can apply to resolve conflicts when uploading a local version of a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/resumesyncforubiquitousitem(at:with:completionhandler:))*