# allDownloads

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Creates download objects for every asset pack in this manifest.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (NSSet<BADownload *> *) allDownloads;
```

#### Return Value

A collection of download objects.

#### Discussion

The returned download objects can be scheduled with the download manager.

> **Remark**: Use this method in your main application; use [`allDownloadsForContentRequest:`](./alldownloadsforcontentrequest_.md) in your downloader extension.

## See Also

### Accessing downloads
- [- allDownloadsForContentRequest:](./alldownloadsforcontentrequest_.md)
  Creates download objects for every asset pack in this manifest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanifest/alldownloads)*