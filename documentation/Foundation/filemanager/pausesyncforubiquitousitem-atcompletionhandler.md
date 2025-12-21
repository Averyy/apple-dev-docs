# pauseSyncForUbiquitousItem(at:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Asynchronously pauses sync of an item at the given URL.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func pauseSyncForUbiquitousItem(at url: URL) async throws
```

#### Discussion

Call this when opening an item to prevent sync from altering the contents of the URL. Once paused, the file provider will not upload local changes nor download remote changes.

While paused, call [`uploadLocalVersionOfUbiquitousItem(at:withConflictResolutionPolicy:completionHandler:)`](filemanager/uploadlocalversionofubiquitousitem(at:withconflictresolutionpolicy:completionhandler:).md) when the document is in a stable state. This action keeps the server version as up-to-date as possible.

If the item is already paused, a second call to this method reports success. If the file provider is already applying changes to the item, the pause fails with an [`NSFileWriteUnknownError`](nsfilewriteunknownerror-c.enum.case.md), with an underlying error that has domain [`NSPOSIXErrorDomain`](nsposixerrordomain.md) and code [`EBUSY`](posixerror/ebusy.md). If the pause fails, wait for the state to stabilize before retrying. Pausing also fails with [`featureUnsupported`](cocoaerror/featureunsupported.md) if `url` refers to a regular (non-package) directory.

Pausing sync is independent of the calling app’s lifecycle; sync doesn’t automatically resume if the app closes or crashes and relaunches later. To resume syncing, explicitly call [`resumeSyncForUbiquitousItem(at:with:completionHandler:)`](filemanager/resumesyncforubiquitousitem(at:with:completionhandler:).md). Always be sure to resume syncing before you close the item.

## Parameters

- `url`: The URL of the item for which to pause sync.
- `completionHandler`: A closure or block that the framework calls when the pause action completes. It receives a single   parameter to indicate an error that prevented pausing; this value is   if the pause succeeded. In Swift, you can omit the completion handler and catch the thrown error instead.

## See Also

- [struct NSFileManagerSupportedSyncControls](nsfilemanagersupportedsynccontrols.md)
  An option set of the sync controls available for an item.
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
- [enum NSFileManagerUploadLocalVersionConflictPolicy](nsfilemanageruploadlocalversionconflictpolicy.md)
  The policies the file manager can apply to resolve conflicts when uploading a local version of a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/pausesyncforubiquitousitem(at:completionhandler:))*