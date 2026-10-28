# NSFileManagerResumeSyncBehavior.afterUploadWithFailOnConflict

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

Resumes sync by first uploading the local version of the file, failing if the provider detects a conflict.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case afterUploadWithFailOnConflict
```

```c
NSFileManagerResumeSyncBehaviorAfterUploadWithFailOnConflict
```

## Discussion

If the upload succeeds, the sync resumes with the [`NSFileManagerResumeSyncBehavior.preserveLocalChanges`](./preservelocalchanges.md) behavior.

If the provider detects a conflict, the upload fails with an  [`NSFileWriteUnknownError`](../nsfilewriteunknownerror-c.enum.case.md), with the underlying error of [`localVersionConflictingWithServer`](../../FileProvider/nsfileprovidererror/localversionconflictingwithserver.md). In this case, the app needs to call [`fetchLatestRemoteVersionOfItem(at:completionHandler:)`](../filemanager/fetchlatestremoteversionofitem%28at,completionhandler%29.md), rebase local changes on top of the newly fetched version to resolve the conflict, and try again to resume sync. This scenario is only available on paused items for which the file provider supports the fail-on-conflict behavior. To check that the file provider supports the behavior, get the [`ubiquitousItemSupportedSyncControlsKey`](../urlresourcekey/ubiquitousitemsupportedsynccontrolskey.md) URL resource and verify that [`failUploadOnConflict`](../nsfilemanagersupportedsynccontrols/failuploadonconflict.md) is `true`.

## See Also

### Identifying sync behaviors
- [NSFileManagerResumeSyncBehavior.preserveLocalChanges](./preservelocalchanges.md)
  Resumes synchronizing by uploading the local version of the file.
- [NSFileManagerResumeSyncBehavior.dropLocalChanges](./droplocalchanges.md)
  Resumes synchronizing by overwriting any local changes with the remote version of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilemanagerresumesyncbehavior/afteruploadwithfailonconflict)*