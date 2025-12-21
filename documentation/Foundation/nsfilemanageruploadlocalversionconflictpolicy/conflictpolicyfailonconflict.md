# NSFileManagerUploadLocalVersionConflictPolicy.conflictPolicyFailOnConflict

**Framework**: Foundation  
**Kind**: case

Resolves the conflict by causing the upload to fail.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case conflictPolicyFailOnConflict
```

#### Discussion

This policy causes an upload to fail if the local version of a file, with any local changes applied, doesn’t match the server version. In this scenario, call [`fetchLatestRemoteVersionOfItem(at:completionHandler:)`](filemanager/fetchlatestremoteversionofitem(at:completionhandler:).md), rebase local changes on top of the newly fetched version, and retry the upload.

This policy is only available on paused items for which the file provider supports the fail-on-conflict behavior. To check that the file provider supports the behavior, get the [`ubiquitousItemSupportedSyncControlsKey`](urlresourcekey/ubiquitousitemsupportedsynccontrolskey.md) URL resource and verify that [`failUploadOnConflict`](nsfilemanagersupportedsynccontrols/failuploadonconflict.md) is `true`.

## See Also

- [NSFileManagerUploadLocalVersionConflictPolicy.conflictPolicyDefault](nsfilemanageruploadlocalversionconflictpolicy/conflictpolicydefault.md)
  Resolves the conflict using the policy defined by the file provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilemanageruploadlocalversionconflictpolicy/conflictpolicyfailonconflict)*