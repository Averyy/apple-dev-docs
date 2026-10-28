# NSMetadataUbiquitousItemIsDownloadedKey

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- iOS 5.0+ - Deprecated in 7.0
- iPadOS 5.0+ - Deprecated in 7.0
- Mac Catalyst 5.0+ - Deprecated in 7.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use NSMetadataUbiquitousItemDownloadingStatusKey instead

## Declaration

```swift
let NSMetadataUbiquitousItemIsDownloadedKey: String
```

```c
extern NSString * const NSMetadataUbiquitousItemIsDownloadedKey;
```

## Discussion

The value is an [`NSNumber`](./nsnumber.md) object that contains a Boolean indicating whether the current version of the item has been downloaded and is available locally.

This constant is deprecated in iOS 7 and OS X v10.9; use [`NSMetadataUbiquitousItemDownloadingStatusKey`](./nsmetadataubiquitousitemdownloadingstatuskey.md) instead.

## See Also

### iCloud Keys
- [let NSMetadataItemIsUbiquitousKey: String](./nsmetadataitemisubiquitouskey.md)
- [let NSMetadataUbiquitousItemContainerDisplayNameKey: String](./nsmetadataubiquitousitemcontainerdisplaynamekey.md)
  The display name of the container that stores the ubiquitous item.
- [let NSMetadataUbiquitousItemDownloadRequestedKey: String](./nsmetadataubiquitousitemdownloadrequestedkey.md)
  A Boolean value indicating whether a download has been requested for the ubiquitous item.
- [let NSMetadataUbiquitousItemIsExternalDocumentKey: String](./nsmetadataubiquitousitemisexternaldocumentkey.md)
  A Boolean value indicating whether the ubiquitous item is from an external document.
- [let NSMetadataUbiquitousItemURLInLocalContainerKey: String](./nsmetadataubiquitousitemurlinlocalcontainerkey.md)
  The URL for the ubiquitous item in the local container.
- [let NSMetadataUbiquitousItemHasUnresolvedConflictsKey: String](./nsmetadataubiquitousitemhasunresolvedconflictskey.md)
- [let NSMetadataUbiquitousItemIsDownloadingKey: String](./nsmetadataubiquitousitemisdownloadingkey.md)
- [let NSMetadataUbiquitousItemIsUploadedKey: String](./nsmetadataubiquitousitemisuploadedkey.md)
- [let NSMetadataUbiquitousItemIsUploadingKey: String](./nsmetadataubiquitousitemisuploadingkey.md)
- [let NSMetadataUbiquitousItemPercentDownloadedKey: String](./nsmetadataubiquitousitempercentdownloadedkey.md)
- [let NSMetadataUbiquitousItemPercentUploadedKey: String](./nsmetadataubiquitousitempercentuploadedkey.md)
- [let NSMetadataUbiquitousItemDownloadingStatusKey: String](./nsmetadataubiquitousitemdownloadingstatuskey.md)
- [let NSMetadataUbiquitousItemDownloadingErrorKey: String](./nsmetadataubiquitousitemdownloadingerrorkey.md)
- [let NSMetadataUbiquitousItemUploadingErrorKey: String](./nsmetadataubiquitousitemuploadingerrorkey.md)
- [let NSMetadataUbiquitousItemIsSharedKey: String](./nsmetadataubiquitousitemissharedkey.md)
  A Boolean value indicating whether the ubiquitous item is shared.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisdownloadedkey)*