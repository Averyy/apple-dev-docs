# ubiquitousItemSupportedSyncControlsKey

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The read-only value of the `NSFileManagerSupportedSyncControls` options (value type `NSNumber`).

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static let ubiquitousItemSupportedSyncControlsKey: URLResourceKey
```

```c
extern NSURLResourceKey const NSURLUbiquitousItemSupportedSyncControlsKey;
```

## See Also

### Ubiquitous keys
- [static let isUbiquitousItemKey: URLResourceKey](./isubiquitousitemkey.md)
  The key for a Boolean value that indicates whether the item is in iCloud storage.
- [static let ubiquitousSharedItemMostRecentEditorNameComponentsKey: URLResourceKey](./ubiquitousshareditemmostrecenteditornamecomponentskey.md)
  The key for the name components of the most recent editor.
- [static let ubiquitousItemDownloadRequestedKey: URLResourceKey](./ubiquitousitemdownloadrequestedkey.md)
  The key for a Boolean value that indicates whether the system has already made a call [`startDownloadingUbiquitousItem(at:)`](../filemanager/startdownloadingubiquitousitem%28at%29.md) to download the item.
- [static let ubiquitousItemIsDownloadingKey: URLResourceKey](./ubiquitousitemisdownloadingkey.md)
  The key for a Boolean value that indicates whether the system is downloading the item from iCloud.
- [static let ubiquitousItemDownloadingErrorKey: URLResourceKey](./ubiquitousitemdownloadingerrorkey.md)
  The key for an error object that indicates why downloading the item from iCloud fails.
- [static let ubiquitousItemDownloadingStatusKey: URLResourceKey](./ubiquitousitemdownloadingstatuskey.md)
  The key for the current download state for the item.
- [struct URLUbiquitousItemDownloadingStatus](../urlubiquitousitemdownloadingstatus.md)
  Values that describe the iCloud storage state of a file.
- [static let ubiquitousItemIsExcludedFromSyncKey: URLResourceKey](./ubiquitousitemisexcludedfromsynckey.md)
  The key of a Boolean value that indicates whether the system excludes the item from syncing.
- [static let ubiquitousItemIsUploadedKey: URLResourceKey](./ubiquitousitemisuploadedkey.md)
  The key for a Boolean value that indicates whether the system uploads the item’s data to iCloud storage.
- [static let ubiquitousItemIsUploadingKey: URLResourceKey](./ubiquitousitemisuploadingkey.md)
  The key for a Boolean value that indicates whether the system is uploading the item to iCloud.
- [static let ubiquitousItemUploadingErrorKey: URLResourceKey](./ubiquitousitemuploadingerrorkey.md)
  The key for an error object that indicates why uploading the item to iCloud fails.
- [static let ubiquitousItemHasUnresolvedConflictsKey: URLResourceKey](./ubiquitousitemhasunresolvedconflictskey.md)
  The key for a Boolean value that indicates whether this item has outstanding conflicts.
- [static let ubiquitousItemContainerDisplayNameKey: URLResourceKey](./ubiquitousitemcontainerdisplaynamekey.md)
  The key for a string that contains the name of the item’s container as it appears to the user.
- [static let ubiquitousSharedItemOwnerNameComponentsKey: URLResourceKey](./ubiquitousshareditemownernamecomponentskey.md)
  The key for the name components of the item’s owner.
- [static let ubiquitousSharedItemCurrentUserPermissionsKey: URLResourceKey](./ubiquitousshareditemcurrentuserpermissionskey.md)
  The key for the current user’s permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcekey/ubiquitousitemsupportedsynccontrolskey)*