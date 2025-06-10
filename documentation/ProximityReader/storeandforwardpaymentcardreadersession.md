# StoreAndForwardPaymentCardReaderSession

**Framework**: ProximityReader  
**Kind**: class

The object you use to start reading a contactless payment or loyalty card in Store and Forward mode.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
class StoreAndForwardPaymentCardReaderSession
```

#### Overview

Use a `StoreAndForwardPaymentCardReaderSession` object to read payment and loyalty cards from a properly configured device. You don’t create this object directly. Instead, you obtain one by calling the [`prepareStoreAndForward()`](paymentcardreader/preparestoreandforward().md) method of your [`PaymentCardReader`](paymentcardreader.md) object, which returns a session after the successful configuration of the device.

Maintain a strong reference to a session object for the duration of the card-reading process. You may use the same session object to perform multiple read operations, but you may perform only one read operation at a time

## Topics

### Instance Methods
- [func decline() async throws](storeandforwardpaymentcardreadersession/decline.md)
  Removes the last read from store.
- [func status() async throws -> StoreAndForwardStatus](storeandforwardpaymentcardreadersession/status.md)
  Allows the merchant to check the status of the Store and Forward session.

## Relationships

### Inherits From
- [PaymentCardReaderSession](paymentcardreadersession.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct StoreAndForwardBatch](storeandforwardbatch.md)
  A structure that stores the data to send to the payment service provider to process.
- [struct StoreAndForwardBatchDeletionToken](storeandforwardbatchdeletiontoken.md)
  A secure token that you use to delete a Store and Forward batch.
- [struct StoreAndForwardStatus](storeandforwardstatus.md)
  A structure that describes the Store and Forward session status.
- [struct PaymentCardReaderStore](paymentcardreaderstore.md)
  A structure that manages the store that contains all the Store and Forward reads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/storeandforwardpaymentcardreadersession)*