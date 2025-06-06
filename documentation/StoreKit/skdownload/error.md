# error

**Framework**: StoreKit  
**Kind**: property

The error that prevented the content from being downloaded.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 6.2+

## Declaration

```swift
var error: (any Error)? { get }
```

## Mentions

- [Unlocking purchased content](unlocking-purchased-content.md)

#### Discussion

The value of this property is valid only when the [`downloadState`](skdownload/downloadstate.md) property is set to [`SKDownloadState.failed`](skdownloadstate/failed.md).

## See Also

- [var contentURL: URL?](skdownload/contenturl.md)
  The local location of the downloaded file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/error)*