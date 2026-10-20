# NSMetadataUbiquitousItemDownloadingStatusNotDownloaded

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSMetadataUbiquitousItemDownloadingStatusNotDownloaded: String
```

```c
extern NSString * const NSMetadataUbiquitousItemDownloadingStatusNotDownloaded;
```

#### Discussion

A string used as the value for [`NSMetadataUbiquitousItemPercentUploadedKey`](./nsmetadataubiquitousitempercentuploadedkey.md) to indicate that this item has not been downloaded yet.

You can use [`startDownloadingUbiquitousItem(at:)`](./filemanager/startdownloadingubiquitousitem%28at%29.md) to download the item.

## See Also

### iCloud Download Status Values
- [let NSMetadataUbiquitousItemDownloadingStatusCurrent: String](./nsmetadataubiquitousitemdownloadingstatuscurrent.md)
- [let NSMetadataUbiquitousItemDownloadingStatusDownloaded: String](./nsmetadataubiquitousitemdownloadingstatusdownloaded.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemdownloadingstatusnotdownloaded)*