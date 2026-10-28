# download

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Creates a download object for the asset pack that you schedule using a download manager.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (BADownload *) download;
```

## Discussion

> **Remark**: Use this method in your main app; use [`downloadForContentRequest:`](./downloadforcontentrequest_.md) instead in your downloader extension.

## See Also

### Downloading assets
- [- downloadForContentRequest:](./downloadforcontentrequest_.md)
  Creates a download object for the asset pack that you schedule using a download manager.
- [downloadSize](./downloadsize.md)
  The size of the download file containing the asset pack in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpack/download)*