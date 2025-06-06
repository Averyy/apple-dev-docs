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

### Structures
- [StoreAndForwardBatch.StoredPaymentCardReadResult](storeandforwardbatch/storedpaymentcardreadresult.md)
  A result structure that represents each payment the framework read using a Store and Forward session.
### Instance Properties
- [let count: Int](storeandforwardbatch/count.md)
  The number of payments this batch includes.
- [let id: String](storeandforwardbatch/id-swift.property.md)
  The unique identifier for the batch.
- [let intermediateCertificate: [String]](storeandforwardbatch/intermediatecertificate.md)
  An array that contains the intermediate certificates that the system uses to sign the leaf certificate.
- [let leafCertificate: String](storeandforwardbatch/leafcertificate.md)
  The leaf certificate the framework uses to sign this batch.
- [let payments: [StoreAndForwardBatch.StoredPaymentCardReadResult]](storeandforwardbatch/payments.md)
  The payments that are part of the batch.
- [let signature: String](storeandforwardbatch/signature.md)
  The signature, as a Base64-encoded string, that guarantees the integrity of the batch.
### Instance Methods
- [func encode(to: any Encoder) throws](storeandforwardbatch/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [StoreAndForwardBatch.ID](storeandforwardbatch/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.

## Relationships

### Conforms To
- [Encodable](../Swift/Encodable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/storeandforwardbatch)*