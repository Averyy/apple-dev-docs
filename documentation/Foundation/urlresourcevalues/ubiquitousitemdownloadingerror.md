# ubiquitousItemDownloadingError

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

### Ubiquitous values
- [var isUbiquitousItem: Bool?](./isubiquitousitem.md)
  A Boolean value that indicates whether the item is in the iCloud storage.
- [var ubiquitousItemIsShared: Bool?](./ubiquitousitemisshared.md)
  A Boolean value that indicates a shared item.
- [var ubiquitousItemIsExcludedFromSync: Bool?](./ubiquitousitemisexcludedfromsync.md)
  A Boolean value that indicates the system excludes the item from syncing.
- [var ubiquitousSharedItemCurrentUserPermissions: URLUbiquitousSharedItemPermissions?](./ubiquitousshareditemcurrentuserpermissions.md)
  The current user’s permissions for the shared item.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcevalues/ubiquitousitemdownloadingerror)*