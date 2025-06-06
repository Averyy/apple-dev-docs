# cancel(_:)

**Framework**: StoreKit  
**Kind**: method

Removes a set of downloads from the download list.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 6.2+

## Declaration

```swift
func cancel(_ downloads: [SKDownload])
```

## Mentions

- [Unlocking purchased content](unlocking-purchased-content.md)

## Parameters

- `downloads`: An array of   objects to cancel.

## See Also

- [func start([SKDownload])](skpaymentqueue/start(_:).md)
  Adds a set of downloads to the download list.
- [func pause([SKDownload])](skpaymentqueue/pause(_:).md)
  Pauses a set of downloads.
- [func resume([SKDownload])](skpaymentqueue/resume(_:).md)
  Resumes a set of downloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/cancel(_:))*