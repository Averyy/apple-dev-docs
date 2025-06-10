# current

**Framework**: Foundation  
**Kind**: property

A local copy of this item exists and is the most up-to-date version known to the device.

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
static let current: URLUbiquitousItemDownloadingStatus
```

## See Also

- [static let downloaded: URLUbiquitousItemDownloadingStatus](urlubiquitousitemdownloadingstatus/downloaded.md)
  A local copy of this item exists, but it is stale. The most recent version will be downloaded as soon as possible.
- [static let notDownloaded: URLUbiquitousItemDownloadingStatus](urlubiquitousitemdownloadingstatus/notdownloaded.md)
  This item has not been downloaded yet. Use [`startDownloadingUbiquitousItem(at:)`](filemanager/startdownloadingubiquitousitem(at:).md) to download it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlubiquitousitemdownloadingstatus/current)*