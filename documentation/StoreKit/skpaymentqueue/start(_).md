# start(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Adds a set of downloads to the download list.

**Availability**:
- iOS 6.0+ - Deprecated in 16.0
- iPadOS 6.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.8+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 6.2+ - Deprecated in 9.0

> **Deprecated**: Hosted content is no longer supported.

## Declaration

```swift
func start(_ downloads: [SKDownload])
```

```objc
- (void) startDownloads:(NSArray<SKDownload *> *) downloads;
```

## Mentions

- [Unlocking purchased content](../unlocking-purchased-content.md)

#### Discussion

In order for a download object to be queued, it must be associated with a transaction that has been successfully purchased, but not yet finished.

## Parameters

- `downloads`: An array of [`SKDownload`](../skdownload.md) objects to begin downloading.

## See Also

### Downloading Content
- [func cancel([SKDownload])](./cancel%28_%29.md)
  Removes a set of downloads from the download list.
- [func pause([SKDownload])](./pause%28_%29.md)
  Pauses a set of downloads.
- [func resume([SKDownload])](./resume%28_%29.md)
  Resumes a set of downloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/start(_:))*