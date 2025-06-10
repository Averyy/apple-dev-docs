# resolveBatch(batchDeletionToken:)

**Framework**: ProximityReader  
**Kind**: method

Deletes the current batch and all its Store and Forward payments, allowing you to request a new batch.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
func resolveBatch(batchDeletionToken: StoreAndForwardBatchDeletionToken) async throws -> Int
```

#### Return Value

The remaining number of payments to process.

#### Discussion

> **Note**: This method throws a [`PaymentCardReaderStore.StoreError`](paymentcardreaderstore/storeerror.md) if the customer isn’t online at the moment you call it, if there’s no Store and Forward batch to resolve, or if the deletion token is invalid.

## Parameters

- `batchDeletionToken`: The token you receive from the payment service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreaderstore/resolvebatch(batchdeletiontoken:))*