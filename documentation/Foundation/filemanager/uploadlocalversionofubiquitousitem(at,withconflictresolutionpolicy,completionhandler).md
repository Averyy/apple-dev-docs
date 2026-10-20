# uploadLocalVersionOfUbiquitousItem(at:withConflictResolutionPolicy:completionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Asynchronously uploads the local version of the item using the provided conflict resolution policy.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func uploadLocalVersionOfUbiquitousItem(at url: URL, withConflictResolutionPolicy conflictResolutionPolicy: NSFileManagerUploadLocalVersionConflictPolicy, completionHandler: @escaping @Sendable (NSFileVersion?, (any Error)?) -> Void)
```

```swift
func uploadLocalVersionOfUbiquitousItem(at url: URL, withConflictResolutionPolicy conflictResolutionPolicy: NSFileManagerUploadLocalVersionConflictPolicy) async throws -> NSFileVersion
```

```objc
- (void) uploadLocalVersionOfUbiquitousItemAtURL:(NSURL *) url withConflictResolutionPolicy:(NSFileManagerUploadLocalVersionConflictPolicy) conflictResolutionPolicy completionHandler:(void (^)(NSFileVersion *uploadedVersion, NSError *error)) completionHandler;
```

#### Discussion

Once your app pauses a sync for an item, call this method every time your document is in a stable state. This action keeps the server version as up-to-date as possible.

If the server has a newer version than the one to which the app made changes, uploading fails with [`NSFileWriteUnknownError`](../nsfilewriteunknownerror-c.enum.case.md), with an underlying error of [`localVersionConflictingWithServer`](../../FileProvider/nsfileprovidererror/localversionconflictingwithserver.md). In this case, call [`fetchLatestRemoteVersionOfItem(at:completionHandler:)`](./fetchlatestremoteversionofitem%28at,completionhandler%29.md), rebase local changes on top of that version, and retry the upload.

If the device isn’t connected to the network, the call may fail with [`NSFileWriteUnknownError`](../nsfilewriteunknownerror-c.enum.case.md), with the underlying error of [`serverUnreachable`](../../FileProvider/nsfileprovidererror/serverunreachable.md).

## Parameters

- `url`: The URL of the item for which to check the version.
- `conflictResolutionPolicy`: The policy the file manager applies if the local and server versions conflict.
- `completionHandler`: A closure or block that the framework calls when the upload completes. It receives parameters of types [`NSFileVersion`](../nsfileversion.md) and [`NSError`](../nserror.md). The error is `nil` if fetching the remote version succeeded; otherwise it indicates the error that caused the call to fail. In Swift, you can omit the completion handler, catching any error in a `do`-`catch` block and receiving the version as the return value.

## See Also

### Controlling file provider synchronization
- [struct NSFileManagerSupportedSyncControls](../nsfilemanagersupportedsynccontrols.md)
  An option set of the sync controls available for an item.
- [func pauseSyncForUbiquitousItem(at: URL, completionHandler: ((any Error)?) -> Void)](./pausesyncforubiquitousitem%28at,completionhandler%29.md)
  Asynchronously pauses sync of an item at the given URL.
- [func resumeSyncForUbiquitousItem(at: URL, with: NSFileManagerResumeSyncBehavior, completionHandler: ((any Error)?) -> Void)](./resumesyncforubiquitousitem%28at,with,completionhandler%29.md)
  Asynchronously resumes the sync on a paused item using the given resume behavior.
- [enum NSFileManagerResumeSyncBehavior](../nsfilemanagerresumesyncbehavior.md)
  The behaviors the file manager can apply to resolve conflicts when resuming a sync.
- [func fetchLatestRemoteVersionOfItem(at: URL, completionHandler: (NSFileVersion?, (any Error)?) -> Void)](./fetchlatestremoteversionofitem%28at,completionhandler%29.md)
  Asynchronously fetches the latest remote version of a given item from the server.
- [class NSFileVersion](../nsfileversion.md)
  A snapshot of a file at a specific point in time.
- [enum NSFileManagerUploadLocalVersionConflictPolicy](../nsfilemanageruploadlocalversionconflictpolicy.md)
  The policies the file manager can apply to resolve conflicts when uploading a local version of a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/uploadlocalversionofubiquitousitem(at:withconflictresolutionpolicy:completionhandler:))*