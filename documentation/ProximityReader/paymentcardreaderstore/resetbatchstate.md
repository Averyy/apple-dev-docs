# resetBatchState()

**Framework**: ProximityReader  
**Kind**: method

Resets the current batch state in the store, allowing you to request a new batch.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
func resetBatchState() async throws
```

#### Discussion

Use this method if the transmission of the batch to the partner service provider fails and the batch processing status is unknown. The framework doesn’t delete the reads; instead, it dissociates them from the batch.

> **Note**: This method throws a [`PaymentCardReaderStore.StoreError`](paymentcardreaderstore/storeerror.md) if there’s no batch for the framework to reset.

This method throws a [`PaymentCardReaderStore.StoreError`](paymentcardreaderstore/storeerror.md) if there’s no batch for the framework to reset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreaderstore/resetbatchstate())*