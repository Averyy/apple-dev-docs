# NSFileManagerResumeSyncBehavior.afterUploadWithFailOnConflict

**Framework**: Foundation  
**Kind**: case

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

#### Discussion

If the upload succeeds, the sync resumes with the [`NSFileManagerResumeSyncBehavior.preserveLocalChanges`](nsfilemanagerresumesyncbehavior/preservelocalchanges.md) behavior.

If the provider detects a conflict, the upload fails with an  [`NSFileWriteUnknownError`](nsfilewriteunknownerror-c.enum.case.md), with the underlying error of [`localVersionConflictingWithServer`](https://developer.apple.com/documentation/FileProvider/NSFileProviderError/localVersionConflictingWithServer). In this case, the app needs to call [`fetchLatestRemoteVersionOfItem(at:completionHandler:)`](filemanager/fetchlatestremoteversionofitem(at:completionhandler:).md), rebase local changes on top of the newly fetched version to resolve the conflict, and try again to resume sync. This scenario is only available on paused items for which the file provider supports the fail-on-conflict behavior. To check that the file provider supports the behavior, get the [`ubiquitousItemSupportedSyncControlsKey`](urlresourcekey/ubiquitousitemsupportedsynccontrolskey.md) URL resource and verify that [`failUploadOnConflict`](nsfilemanagersupportedsynccontrols/failuploadonconflict.md) is `true`.

## See Also

- [NSFileManagerResumeSyncBehavior.preserveLocalChanges](nsfilemanagerresumesyncbehavior/preservelocalchanges.md)
  Resumes synchronizing by uploading the local version of the file.
- [NSFileManagerResumeSyncBehavior.dropLocalChanges](nsfilemanagerresumesyncbehavior/droplocalchanges.md)
  Resumes synchronizing by overwriting any local changes with the remote version of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilemanagerresumesyncbehavior/afteruploadwithfailonconflict)*