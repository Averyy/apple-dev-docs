# kCFURLUbiquitousItemPercentDownloadedKey

**Framework**: Core Foundation  
**Kind**: var

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCFURLUbiquitousItemPercentDownloadedKey: CFString!
```

#### Discussion

A `CFNumber` value that provides the status of the download in progress.

Deprecated. Use [`NSMetadataQuery`](https://developer.apple.com/documentation/Foundation/NSMetadataQuery) and [`NSMetadataUbiquitousItemPercentDownloadedKey`](https://developer.apple.com/documentation/Foundation/NSMetadataUbiquitousItemPercentDownloadedKey) on [`NSMetadataItem`](https://developer.apple.com/documentation/Foundation/NSMetadataItem) instead.

## See Also

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
- [let kCFURLUbiquitousItemPercentUploadedKey: CFString!](kcfurlubiquitousitempercentuploadedkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitempercentdownloadedkey)*