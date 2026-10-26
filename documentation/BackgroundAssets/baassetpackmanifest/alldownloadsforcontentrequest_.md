# allDownloadsForContentRequest:

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
- (NSSet<BADownload *> *) allDownloadsForContentRequest:(BAContentRequest) contentRequest;
```

#### Return Value

A collection of download objects.

#### Discussion

The returned download objects can be scheduled with the download manager.

> **Remark**: Use this method in your downloader extension; use [`allDownloads`](./alldownloads.md) instead in your main application.

## Parameters

- `contentRequest`: The content request for the current extension invocation.

## See Also

### Accessing downloads
- [- allDownloads](./alldownloads.md)
  Creates download objects for every asset pack in this manifest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanifest/alldownloadsforcontentrequest:)*