# paymentQueue(_:updatedDownloads:)

**Framework**: StoreKit  
**Kind**: method

Tells the observer that the payment queue has updated one or more download objects.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 6.2+

## Declaration

```swift
optional func paymentQueue(_ queue: SKPaymentQueue, updatedDownloads downloads: [SKDownload])
```

## Mentions

- [Unlocking purchased content](unlocking-purchased-content.md)

#### Discussion

When a download object is updated, its [`downloadState`](skdownload/downloadstate.md) property describes how it changed.

## Parameters

- `queue`: The payment queue that updated the downloads.
- `downloads`: The download objects that were updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:updateddownloads:))*