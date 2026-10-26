# downloadForContentRequest:

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
- (BADownload *) downloadForContentRequest:(BAContentRequest) contentRequest;
```

#### Return Value

A download object.

#### Discussion

> **Remark**: Use this method in your downloader extension; use [`download`](./download.md) instead in your main app.

## Parameters

- `contentRequest`: The content request for the current extension invocation.

## See Also

### Downloading assets
- [- download](./download.md)
  Creates a download object for the asset pack that you schedule using a download manager.
- [downloadSize](./downloadsize.md)
  The size of the download file containing the asset pack in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpack/downloadforcontentrequest:)*