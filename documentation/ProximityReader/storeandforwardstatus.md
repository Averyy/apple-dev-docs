# StoreAndForwardStatus

**Framework**: ProximityReader  
**Kind**: struct

A structure that describes the Store and Forward session status.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
struct StoreAndForwardStatus
```

#### Overview

A session’s `StoreAndForwardStatus` tells you when the Store and Forward session expires and how many successful reads the framework performed using a Store and Forward session.

Call [`status()`](storeandforwardpaymentcardreadersession/status().md) to get the current Store and Forward status for your device.

## Topics

### Getting the status
- [let expiration: Date](storeandforwardstatus/expiration.md)
  The date when the Store and Forward session expires.
- [let readCount: Int](storeandforwardstatus/readcount.md)
  The number of successful reads the framework performed using a Store and Forward session.
### Operators
- [static func == (StoreAndForwardStatus, StoreAndForwardStatus) -> Bool](storeandforwardstatus/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](storeandforwardstatus/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](storeandforwardstatus/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](storeandforwardstatus/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct StoreAndForwardBatch](storeandforwardbatch.md)
  A structure that stores the data to send to the payment service provider to process.
- [struct StoreAndForwardBatchDeletionToken](storeandforwardbatchdeletiontoken.md)
  A secure token that you use to delete a Store and Forward batch.
- [class StoreAndForwardPaymentCardReaderSession](storeandforwardpaymentcardreadersession.md)
  The object you use to start reading a contactless payment or loyalty card in Store and Forward mode.
- [struct PaymentCardReaderStore](paymentcardreaderstore.md)
  A structure that manages the store that contains all the Store and Forward reads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/storeandforwardstatus)*