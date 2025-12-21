# StoreAndForwardBatchDeletionToken

**Framework**: ProximityReader  
**Kind**: struct

A secure token that you use to delete a Store and Forward batch.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
struct StoreAndForwardBatchDeletionToken
```

#### Overview

A `StoreAndForwardBatchDeletionToken` holds the token  your payment service provider supplies when they successfully send a batch of Store and Forward payments for processing.

After receiving the raw token data from your provider, create an instance of this structure and pass it to the [`resolveBatch(batchDeletionToken:)`](paymentcardreaderstore/resolvebatch(batchdeletiontoken:).md) method. When resolving a Store and Forward batch, the [`PaymentCardReaderStore`](paymentcardreaderstore.md) uses this token to verify that the payments were delivered to the payment service provider and can now be deleted.

## Topics

### Creating a token
- [init(rawValue: String)](storeandforwardbatchdeletiontoken/init(rawvalue:).md)
  Creates a token with the string your payment service provider provides.
### Getting the token value
- [let rawValue: String](storeandforwardbatchdeletiontoken/rawvalue.md)
  The raw token string your payment service provider supplies.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct StoreAndForwardBatch](storeandforwardbatch.md)
  A structure that stores the data to send to the payment service provider to process.
- [class StoreAndForwardPaymentCardReaderSession](storeandforwardpaymentcardreadersession.md)
  The object you use to start reading a contactless payment or loyalty card in Store and Forward mode.
- [struct StoreAndForwardStatus](storeandforwardstatus.md)
  A structure that describes the Store and Forward session status.
- [struct PaymentCardReaderStore](paymentcardreaderstore.md)
  A structure that manages the store that contains all the Store and Forward reads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/storeandforwardbatchdeletiontoken)*