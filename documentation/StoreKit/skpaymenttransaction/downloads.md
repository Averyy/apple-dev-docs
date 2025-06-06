# downloads

**Framework**: StoreKit  
**Kind**: property

An array of download objects representing the downloadable content associated with the transaction.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 6.2+

## Declaration

```swift
var downloads: [SKDownload] { get }
```

## Mentions

- [Unlocking purchased content](unlocking-purchased-content.md)

#### Discussion

The contents of this property are undefined except when [`transactionState`](skpaymenttransaction/transactionstate.md) is set to [`SKPaymentTransactionState.purchased`](skpaymenttransactionstate/purchased.md). The [`SKDownload`](skdownload.md) objects stored in this property must be used to download the transaction’s content before the transaction is finished. After the transaction is finished, the download objects are no longer queueable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransaction/downloads)*