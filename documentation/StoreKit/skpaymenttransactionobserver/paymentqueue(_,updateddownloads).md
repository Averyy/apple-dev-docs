# paymentQueue(_:updatedDownloads:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Tells the observer that the payment queue has updated one or more download objects.

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
optional func paymentQueue(_ queue: SKPaymentQueue, updatedDownloads downloads: [SKDownload])
```

```objc
- (void) paymentQueue:(SKPaymentQueue *) queue updatedDownloads:(NSArray<SKDownload *> *) downloads;
```

## Mentions

- [Unlocking purchased content](../unlocking-purchased-content.md)

#### Discussion

When a download object is updated, its [`downloadState`](../skdownload/downloadstate.md) property describes how it changed.

## Parameters

- `queue`: The payment queue that updated the downloads.
- `downloads`: The download objects that were updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:updateddownloads:))*