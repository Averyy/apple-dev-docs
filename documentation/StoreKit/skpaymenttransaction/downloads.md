# downloads

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

An array of download objects representing the downloadable content associated with the transaction.

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
var downloads: [SKDownload] { get }
```

```objc
@property (nonatomic, readonly) NSArray<SKDownload *> * downloads;
```

## Mentions

- [Unlocking purchased content](../unlocking-purchased-content.md)

## Discussion

The contents of this property are undefined except when [`transactionState`](./transactionstate.md) is set to [`SKPaymentTransactionState.purchased`](../skpaymenttransactionstate/purchased.md). The [`SKDownload`](../skdownload.md) objects stored in this property must be used to download the transaction’s content before the transaction is finished. After the transaction is finished, the download objects are no longer queueable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransaction/downloads)*