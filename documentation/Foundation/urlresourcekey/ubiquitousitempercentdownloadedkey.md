# ubiquitousItemPercentDownloadedKey

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The key for a value that indicates the percentage of data that the system downloaded from iCloud storage.

**Availability**:
- iOS 5.0+ - Deprecated in 6.0
- iPadOS 5.0+ - Deprecated in 6.0
- Mac Catalyst 5.0+ - Deprecated in 6.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`NSMetadataQuery`](../nsmetadataquery.md) class to search for [`NSMetadataItem`](../nsmetadataitem.md) objects that have the [`NSMetadataUbiquitousItemPercentDownloadedKey`](../nsmetadataubiquitousitempercentdownloadedkey.md) attribute instead.

## Declaration

```swift
static let ubiquitousItemPercentDownloadedKey: URLResourceKey
```

```c
extern NSURLResourceKey const NSURLUbiquitousItemPercentDownloadedKey;
```

## See Also

### Deprecated
- [static let ubiquitousItemIsDownloadedKey: URLResourceKey](./ubiquitousitemisdownloadedkey.md)
  The key for a Boolean value that indicates whether the system downloaded this item’s data from iCloud storage.
- [static let ubiquitousItemPercentUploadedKey: URLResourceKey](./ubiquitousitempercentuploadedkey.md)
  The key for a value that indicates the percentage of data that the system uploaded to iCloud storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcekey/ubiquitousitempercentdownloadedkey)*