# start(_:)

**Framework**: StoreKit  
**Kind**: method

Adds a set of downloads to the download list.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 6.2+

## Declaration

```swift
func start(_ downloads: [SKDownload])
```

## Mentions

- [Unlocking purchased content](unlocking-purchased-content.md)

#### Discussion

In order for a download object to be queued, it must be associated with a transaction that has been successfully purchased, but not yet finished.

## Parameters

- `downloads`: An array of   objects to begin downloading.

## See Also

- [func cancel([SKDownload])](skpaymentqueue/cancel(_:).md)
  Removes a set of downloads from the download list.
- [func pause([SKDownload])](skpaymentqueue/pause(_:).md)
  Pauses a set of downloads.
- [func resume([SKDownload])](skpaymentqueue/resume(_:).md)
  Resumes a set of downloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/start(_:))*