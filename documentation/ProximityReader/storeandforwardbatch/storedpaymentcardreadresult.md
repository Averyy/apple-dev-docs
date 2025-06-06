# StoreAndForwardBatch.StoredPaymentCardReadResult

**Framework**: ProximityReader  
**Kind**: struct

A result structure that represents each payment the framework read using a Store and Forward session.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
struct StoredPaymentCardReadResult
```

## Topics

### Instance Properties
- [let generalCardData: String](storeandforwardbatch/storedpaymentcardreadresult/generalcarddata.md)
  A Base64-encoded string that contains general cardholder and terminal data in tag-length-value (TLV) format.
- [let id: String](storeandforwardbatch/storedpaymentcardreadresult/id-swift.property.md)
  The unique identifier for the payment.
- [let paymentCardData: String](storeandforwardbatch/storedpaymentcardreadresult/paymentcarddata.md)
  A Base64-encoded string that contains the encrypted payment information to send to your payment provider.
- [let signature: String](storeandforwardbatch/storedpaymentcardreadresult/signature.md)
  The signature, as a Base64-encoded string, that guarantees the integrity of the payment
### Instance Methods
- [func encode(to: any Encoder) throws](storeandforwardbatch/storedpaymentcardreadresult/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [StoreAndForwardBatch.StoredPaymentCardReadResult.ID](storeandforwardbatch/storedpaymentcardreadresult/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.

## Relationships

### Conforms To
- [Encodable](../Swift/Encodable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/storeandforwardbatch/storedpaymentcardreadresult)*