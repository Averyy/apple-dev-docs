# StoreAndForwardBatch

**Framework**: ProximityReader  
**Kind**: struct

A structure that stores the data to send to the payment service provider to process.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
struct StoreAndForwardBatch
```

#### Overview

The framework invokes these payments using a Store and Forward session.

## Topics

### Getting the batch details
- [let id: String](storeandforwardbatch/id.md)
  The unique identifier for the batch.
- [let count: Int](storeandforwardbatch/count.md)
  The number of payments this batch includes.
- [let intermediateCertificate: [String]](storeandforwardbatch/intermediatecertificate.md)
  An array that contains the intermediate certificates that the system uses to sign the leaf certificate.
- [let leafCertificate: String](storeandforwardbatch/leafcertificate.md)
  The leaf certificate the framework uses to sign this batch.
- [let payments: [StoreAndForwardBatch.StoredPaymentCardReadResult]](storeandforwardbatch/payments.md)
  The payments that are part of the batch.
- [let signature: String](storeandforwardbatch/signature.md)
  The signature, as a Base64-encoded string, that guarantees the integrity of the batch.
### Getting the results
- [StoreAndForwardBatch.StoredPaymentCardReadResult](storeandforwardbatch/storedpaymentcardreadresult.md)
  A result structure that represents each payment the framework read using a Store and Forward session.

## Relationships

### Conforms To
- [Encodable](../Swift/Encodable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct StoreAndForwardBatchDeletionToken](storeandforwardbatchdeletiontoken.md)
  A secure token that you use to delete a Store and Forward batch.
- [class StoreAndForwardPaymentCardReaderSession](storeandforwardpaymentcardreadersession.md)
  The object you use to start reading a contactless payment or loyalty card in Store and Forward mode.
- [struct StoreAndForwardStatus](storeandforwardstatus.md)
  A structure that describes the Store and Forward session status.
- [struct PaymentCardReaderStore](paymentcardreaderstore.md)
  A structure that manages the store that contains all the Store and Forward reads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/storeandforwardbatch)*