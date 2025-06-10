# fetchStoredPaymentCardReadResultBatch(size:)

**Framework**: ProximityReader  
**Kind**: method

Returns a batch of reads the framework previously stored, in chronological order, of the size you request.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
func fetchStoredPaymentCardReadResultBatch(size: Int = 0) async throws -> StoreAndForwardBatch
```

#### Return Value

[`StoreAndForwardBatch`](storeandforwardbatch.md) when successful.

#### Discussion

There is only one active batch per application at a given time and to fetch a new batch the caller needs to reset or resolve the current batch.

> **Note**: This method throws a [`PaymentCardReaderStore.StoreError`](paymentcardreaderstore/storeerror.md) if the size is smaller than `0` or greater than the number of payments stored, or if there’s no payment stored.  The framework also throws a `StoreError` if a previous batch is pending resolution at the time when you call this  method.

## Parameters

- `size`: The desired batch size, if no size is provided, the framework uses a  batch size of   that returns all the payments   stored  in the batch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreaderstore/fetchstoredpaymentcardreadresultbatch(size:))*