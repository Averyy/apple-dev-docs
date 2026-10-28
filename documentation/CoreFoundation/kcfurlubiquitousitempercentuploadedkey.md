# kCFURLUbiquitousItemPercentUploadedKey

**Framework**: Core Foundation  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- iOS 5.0+ - Deprecated in 6.0
- iPadOS 5.0+ - Deprecated in 6.0
- Mac Catalyst 5.0+ - Deprecated in 6.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use NSMetadataQuery and NSMetadataUbiquitousItemPercentUploadedKey on NSMetadataItem instead

## Declaration

```swift
let kCFURLUbiquitousItemPercentUploadedKey: CFString!
```

```c
extern CFStringRef const kCFURLUbiquitousItemPercentUploadedKey;
```

## Discussion

A `CFNumber` value that provides the status of the upload in progress.

Deprecated. Use [`NSMetadataQuery`](../Foundation/nsmetadataquery.md) and [`NSMetadataUbiquitousItemPercentUploadedKey`](../Foundation/nsmetadataubiquitousitempercentuploadedkey.md) on [`NSMetadataItem`](../Foundation/nsmetadataitem.md) instead.

## See Also

### Constants
- [let kCFURLIsUbiquitousItemKey: CFString!](./kcfurlisubiquitousitemkey.md)
  A `CFBoolean` value that tells whether the item is synced to the cloud. (read-only)
- [let kCFURLUbiquitousItemHasUnresolvedConflictsKey: CFString!](./kcfurlubiquitousitemhasunresolvedconflictskey.md)
  A `CFBoolean` value that tells whether the item has conflicts outstanding. (read-only)
- [let kCFURLUbiquitousItemIsDownloadedKey: CFString!](./kcfurlubiquitousitemisdownloadedkey.md)
  A `CFBoolean` value that tells whether there is local data present for the item. (read-only)
- [let kCFURLUbiquitousItemIsDownloadingKey: CFString!](./kcfurlubiquitousitemisdownloadingkey.md)
  A `CFBoolean` value that tells whether data for the item is being downloaded. (read-only)
- [let kCFURLUbiquitousItemIsUploadedKey: CFString!](./kcfurlubiquitousitemisuploadedkey.md)
  A `CFBoolean` value that tells whether there is data present in the cloud for this item. (read-only)
- [let kCFURLUbiquitousItemIsUploadingKey: CFString!](./kcfurlubiquitousitemisuploadingkey.md)
  A `CFBoolean` value that tells whether data for the item is being uploaded. (read-only)
- [let kCFURLUbiquitousItemPercentDownloadedKey: CFString!](./kcfurlubiquitousitempercentdownloadedkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitempercentuploadedkey)*