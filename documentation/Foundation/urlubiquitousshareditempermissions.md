# URLUbiquitousSharedItemPermissions

**Framework**: Foundation  
**Kind**: struct

The key for the permissions of a shared item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct URLUbiquitousSharedItemPermissions
```

## Topics

### Creating a Shared Item Permissions Instance
- [init(rawValue: String)](urlubiquitousshareditempermissions/init(rawvalue:).md)
  Creates a shared item permissions instance from the provided constant string.
### Constants
- [static let readOnly: URLUbiquitousSharedItemPermissions](urlubiquitousshareditempermissions/readonly.md)
- [static let readWrite: URLUbiquitousSharedItemPermissions](urlubiquitousshareditempermissions/readwrite.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static let isUbiquitousItemKey: URLResourceKey](urlresourcekey/isubiquitousitemkey.md)
  The key for a Boolean value that indicates whether the item is in iCloud storage.
- [static let ubiquitousSharedItemMostRecentEditorNameComponentsKey: URLResourceKey](urlresourcekey/ubiquitousshareditemmostrecenteditornamecomponentskey.md)
  The key for the name components of the most recent editor.
- [static let ubiquitousItemDownloadRequestedKey: URLResourceKey](urlresourcekey/ubiquitousitemdownloadrequestedkey.md)
  The key for a Boolean value that indicates whether the system has already made a call [`startDownloadingUbiquitousItem(at:)`](filemanager/startdownloadingubiquitousitem(at:).md) to download the item.
- [static let ubiquitousItemIsDownloadingKey: URLResourceKey](urlresourcekey/ubiquitousitemisdownloadingkey.md)
  The key for a Boolean value that indicates whether the system is downloading the item from iCloud.
- [static let ubiquitousItemDownloadingErrorKey: URLResourceKey](urlresourcekey/ubiquitousitemdownloadingerrorkey.md)
  The key for an error object that indicates why downloading the item from iCloud fails.
- [static let ubiquitousItemDownloadingStatusKey: URLResourceKey](urlresourcekey/ubiquitousitemdownloadingstatuskey.md)
  The key for the current download state for the item.
- [struct URLUbiquitousItemDownloadingStatus](urlubiquitousitemdownloadingstatus.md)
  Values that describe the iCloud storage state of a file.
- [static let ubiquitousItemIsExcludedFromSyncKey: URLResourceKey](urlresourcekey/ubiquitousitemisexcludedfromsynckey.md)
  The key of a Boolean value that indicates whether the system excludes the item from syncing.
- [static let ubiquitousItemIsUploadedKey: URLResourceKey](urlresourcekey/ubiquitousitemisuploadedkey.md)
  The key for a Boolean value that indicates whether the system uploads the item’s data to iCloud storage.
- [static let ubiquitousItemIsUploadingKey: URLResourceKey](urlresourcekey/ubiquitousitemisuploadingkey.md)
  The key for a Boolean value that indicates whether the system is uploading the item to iCloud.
- [static let ubiquitousItemUploadingErrorKey: URLResourceKey](urlresourcekey/ubiquitousitemuploadingerrorkey.md)
  The key for an error object that indicates why uploading the item to iCloud fails.
- [static let ubiquitousItemHasUnresolvedConflictsKey: URLResourceKey](urlresourcekey/ubiquitousitemhasunresolvedconflictskey.md)
  The key for a Boolean value that indicates whether this item has outstanding conflicts.
- [static let ubiquitousItemContainerDisplayNameKey: URLResourceKey](urlresourcekey/ubiquitousitemcontainerdisplaynamekey.md)
  The key for a string that contains the name of the item’s container as it appears to the user.
- [static let ubiquitousSharedItemOwnerNameComponentsKey: URLResourceKey](urlresourcekey/ubiquitousshareditemownernamecomponentskey.md)
  The key for the name components of the item’s owner.
- [static let ubiquitousSharedItemCurrentUserPermissionsKey: URLResourceKey](urlresourcekey/ubiquitousshareditemcurrentuserpermissionskey.md)
  The key for the current user’s permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlubiquitousshareditempermissions)*