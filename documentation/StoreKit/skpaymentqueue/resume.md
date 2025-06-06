# resume(_:)

**Framework**: StoreKit  
**Kind**: method

Resumes a set of downloads.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 6.2+

## Declaration

```swift
func resume(_ downloads: [SKDownload])
```

## Mentions

- [Unlocking purchased content](unlocking-purchased-content.md)

## Parameters

- `downloads`: An array of   objects to resume.

## See Also

- [func start([SKDownload])](skpaymentqueue/start(_:).md)
  Adds a set of downloads to the download list.
- [func cancel([SKDownload])](skpaymentqueue/cancel(_:).md)
  Removes a set of downloads from the download list.
- [func pause([SKDownload])](skpaymentqueue/pause(_:).md)
  Pauses a set of downloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/resume(_:))*