# ubiquitousSharedItemCurrentUserPermissions

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The current user’s permissions for the shared item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
var ubiquitousSharedItemCurrentUserPermissions: URLUbiquitousSharedItemPermissions? { get }
```

## See Also

### Ubiquitous values
- [var isUbiquitousItem: Bool?](./isubiquitousitem.md)
  A Boolean value that indicates whether the item is in the iCloud storage.
- [var ubiquitousItemIsShared: Bool?](./ubiquitousitemisshared.md)
  A Boolean value that indicates a shared item.
- [var ubiquitousItemIsExcludedFromSync: Bool?](./ubiquitousitemisexcludedfromsync.md)
  A Boolean value that indicates the system excludes the item from syncing.
- [var ubiquitousSharedItemCurrentUserRole: URLUbiquitousSharedItemRole?](./ubiquitousshareditemcurrentuserrole.md)
  The current user’s role for the shared item.
- [var ubiquitousSharedItemMostRecentEditorNameComponents: PersonNameComponents?](./ubiquitousshareditemmostrecenteditornamecomponents.md)
  The name components of the most recent editor of the shared item.
- [var ubiquitousSharedItemOwnerNameComponents: PersonNameComponents?](./ubiquitousshareditemownernamecomponents.md)
  The name components of the owner of the shared item.
- [var ubiquitousItemContainerDisplayName: String?](./ubiquitousitemcontainerdisplayname.md)
  The name of the item’s container as the system displays it to users.
- [var ubiquitousItemDownloadRequested: Bool?](./ubiquitousitemdownloadrequested.md)
  A Boolean value that indicates whether the user or the system requests a download of the item.
- [var ubiquitousItemDownloadingError: NSError?](./ubiquitousitemdownloadingerror.md)
  The error when downloading the item from iCloud fails.
- [var ubiquitousItemDownloadingStatus: URLUbiquitousItemDownloadingStatus?](./ubiquitousitemdownloadingstatus.md)
  The download status of the item.
- [var ubiquitousItemHasUnresolvedConflicts: Bool?](./ubiquitousitemhasunresolvedconflicts.md)
  A Boolean value that indicates whether the item has outstanding conflicts.
- [var ubiquitousItemIsDownloading: Bool?](./ubiquitousitemisdownloading.md)
  A Boolean value that indicates whether the system is downloading the item.
- [var ubiquitousItemIsUploaded: Bool?](./ubiquitousitemisuploaded.md)
  A Boolean value that indicates whether data is present in the cloud for the item.
- [var ubiquitousItemIsUploading: Bool?](./ubiquitousitemisuploading.md)
  A Boolean value that indicates whether the system is uploading the item.
- [var ubiquitousItemUploadingError: NSError?](./ubiquitousitemuploadingerror.md)
  The error when uploading the item to iCloud fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcevalues/ubiquitousshareditemcurrentuserpermissions)*