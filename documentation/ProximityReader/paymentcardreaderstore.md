# PaymentCardReaderStore

**Framework**: ProximityReader  
**Kind**: struct

A structure that manages the store that contains all the Store and Forward reads.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
struct PaymentCardReaderStore
```

## Topics

### Instance Methods
- [func fetchStoredPaymentCardReadResultBatch(size: Int) async throws -> StoreAndForwardBatch](paymentcardreaderstore/fetchstoredpaymentcardreadresultbatch(size:).md)
  Returns a batch of reads the framework previously stored, in chronological order, of the size you request.
- [func fetchStoredPaymentCardReadResultCount() async throws -> Int](paymentcardreaderstore/fetchstoredpaymentcardreadresultcount.md)
  Returns the number of reads the framework performed using a Store and Forward session.
- [func resetBatchState() async throws](paymentcardreaderstore/resetbatchstate.md)
  Resets the current batch state in the store, allowing you to request a new batch.
- [func resolveBatch(batchDeletionToken: StoreAndForwardBatchDeletionToken) async throws -> Int](paymentcardreaderstore/resolvebatch(batchdeletiontoken:).md)
  Deletes the current batch and all its Store and Forward payments, allowing you to request a new batch.
### Enumerations
- [PaymentCardReaderStore.StoreError](paymentcardreaderstore/storeerror.md)
  Values that describes errors related to the payments store.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct StoreAndForwardBatch](storeandforwardbatch.md)
  A structure that stores the data to send to the payment service provider to process.
- [struct StoreAndForwardBatchDeletionToken](storeandforwardbatchdeletiontoken.md)
  A secure token that you use to delete a Store and Forward batch.
- [class StoreAndForwardPaymentCardReaderSession](storeandforwardpaymentcardreadersession.md)
  The object you use to start reading a contactless payment or loyalty card in Store and Forward mode.
- [struct StoreAndForwardStatus](storeandforwardstatus.md)
  A structure that describes the Store and Forward session status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreaderstore)*