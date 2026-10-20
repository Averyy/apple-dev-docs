# cancel(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Removes a set of downloads from the download list.

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
func cancel(_ downloads: [SKDownload])
```

```objc
- (void) cancelDownloads:(NSArray<SKDownload *> *) downloads;
```

## Mentions

- [Unlocking purchased content](../unlocking-purchased-content.md)

## Parameters

- `downloads`: An array of [`SKDownload`](../skdownload.md) objects to cancel.

## See Also

### Downloading Content
- [func start([SKDownload])](./start%28_%29.md)
  Adds a set of downloads to the download list.
- [func pause([SKDownload])](./pause%28_%29.md)
  Pauses a set of downloads.
- [func resume([SKDownload])](./resume%28_%29.md)
  Resumes a set of downloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/cancel(_:))*