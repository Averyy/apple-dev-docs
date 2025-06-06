# iCloud Constants

**Framework**: Core Foundation

These constants can be used to determining whether a file is stored in the cloud and to obtain information about its status.

## Topics

### Constants
- [let kCFURLIsUbiquitousItemKey: CFString!](kcfurlisubiquitousitemkey.md)
  A `CFBoolean` value that tells whether the item is synced to the cloud. (read-only)
- [let kCFURLUbiquitousItemHasUnresolvedConflictsKey: CFString!](kcfurlubiquitousitemhasunresolvedconflictskey.md)
  A `CFBoolean` value that tells whether the item has conflicts outstanding. (read-only)
- [let kCFURLUbiquitousItemIsDownloadedKey: CFString!](kcfurlubiquitousitemisdownloadedkey.md)
  A `CFBoolean` value that tells whether there is local data present for the item. (read-only)
- [let kCFURLUbiquitousItemIsDownloadingKey: CFString!](kcfurlubiquitousitemisdownloadingkey.md)
  A `CFBoolean` value that tells whether data for the item is being downloaded. (read-only)
- [let kCFURLUbiquitousItemIsUploadedKey: CFString!](kcfurlubiquitousitemisuploadedkey.md)
  A `CFBoolean` value that tells whether there is data present in the cloud for this item. (read-only)
- [let kCFURLUbiquitousItemIsUploadingKey: CFString!](kcfurlubiquitousitemisuploadingkey.md)
  A `CFBoolean` value that tells whether data for the item is being uploaded. (read-only)
- [let kCFURLUbiquitousItemPercentDownloadedKey: CFString!](kcfurlubiquitousitempercentdownloadedkey.md)
- [let kCFURLUbiquitousItemPercentUploadedKey: CFString!](kcfurlubiquitousitempercentuploadedkey.md)

## See Also

- [Common File System Resource Keys](common-file-system-resource-keys.md)
  Keys that are applicable to file system URLs.
- [File Resource Types](file-resource-types.md)
  Possible values for the [`kCFURLFileResourceTypeKey`](kcfurlfileresourcetypekey.md) key.
- [File Property Keys](file-property-keys.md)
  Keys that apply to properties of files.
- [Volume Property Keys](volume-property-keys.md)
  Keys that apply to volumes.
- [CFError userInfo Dictionary Keys](cferror-userinfo-dictionary-keys.md)
  Keys in the userInfo dictionary of a `CFError` object when certain CFURL functions return an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/icloud-constants)*