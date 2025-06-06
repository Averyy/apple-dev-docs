# ubiquitousItemDownloadingError

**Framework**: Foundation  
**Kind**: property

The error when downloading the item from iCloud fails.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var ubiquitousItemDownloadingError: NSError? { get }
```

#### Discussion

For error values, see the `NSUbiquitousFile` section in FoundationErrors.h.

## See Also

- [var isUbiquitousItem: Bool?](urlresourcevalues/isubiquitousitem.md)
  A Boolean value that indicates whether the item is in the iCloud storage.
- [var ubiquitousItemIsShared: Bool?](urlresourcevalues/ubiquitousitemisshared.md)
  A Boolean value that indicates a shared item.
- [var ubiquitousItemIsExcludedFromSync: Bool?](urlresourcevalues/ubiquitousitemisexcludedfromsync.md)
  A Boolean value that indicates the system excludes the item from syncing.
- [var ubiquitousSharedItemCurrentUserPermissions: URLUbiquitousSharedItemPermissions?](urlresourcevalues/ubiquitousshareditemcurrentuserpermissions.md)
  The current user’s permissions for the shared item.
- [var ubiquitousSharedItemCurrentUserRole: URLUbiquitousSharedItemRole?](urlresourcevalues/ubiquitousshareditemcurrentuserrole.md)
  The current user’s role for the shared item.
- [var ubiquitousSharedItemMostRecentEditorNameComponents: PersonNameComponents?](urlresourcevalues/ubiquitousshareditemmostrecenteditornamecomponents.md)
  The name components of the most recent editor of the shared item.
- [var ubiquitousSharedItemOwnerNameComponents: PersonNameComponents?](urlresourcevalues/ubiquitousshareditemownernamecomponents.md)
  The name components of the owner of the shared item.
- [var ubiquitousItemContainerDisplayName: String?](urlresourcevalues/ubiquitousitemcontainerdisplayname.md)
  The name of the item’s container as the system displays it to users.
- [var ubiquitousItemDownloadRequested: Bool?](urlresourcevalues/ubiquitousitemdownloadrequested.md)
  A Boolean value that indicates whether the user or the system requests a download of the item.
- [var ubiquitousItemDownloadingStatus: URLUbiquitousItemDownloadingStatus?](urlresourcevalues/ubiquitousitemdownloadingstatus.md)
  The download status of the item.
- [var ubiquitousItemHasUnresolvedConflicts: Bool?](urlresourcevalues/ubiquitousitemhasunresolvedconflicts.md)
  A Boolean value that indicates whether the item has outstanding conflicts.
- [var ubiquitousItemIsDownloading: Bool?](urlresourcevalues/ubiquitousitemisdownloading.md)
  A Boolean value that indicates whether the system is downloading the item.
- [var ubiquitousItemIsUploaded: Bool?](urlresourcevalues/ubiquitousitemisuploaded.md)
  A Boolean value that indicates whether data is present in the cloud for the item.
- [var ubiquitousItemIsUploading: Bool?](urlresourcevalues/ubiquitousitemisuploading.md)
  A Boolean value that indicates whether the system is uploading the item.
- [var ubiquitousItemUploadingError: NSError?](urlresourcevalues/ubiquitousitemuploadingerror.md)
  The error when uploading the item to iCloud fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcevalues/ubiquitousitemdownloadingerror)*