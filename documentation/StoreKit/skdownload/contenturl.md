# contentURL

**Framework**: StoreKit  
**Kind**: property

The local location of the downloaded file.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 6.2+

## Declaration

```swift
var contentURL: URL? { get }
```

## Mentions

- [Unlocking purchased content](unlocking-purchased-content.md)

#### Discussion

The value of this property is valid only when the [`downloadState`](skdownload/downloadstate.md) property is set to [`SKDownloadState.finished`](skdownloadstate/finished.md). The URL becomes invalid after the transaction object associated with the download is finalized.

## See Also

- [var error: (any Error)?](skdownload/error.md)
  The error that prevented the content from being downloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/contenturl)*