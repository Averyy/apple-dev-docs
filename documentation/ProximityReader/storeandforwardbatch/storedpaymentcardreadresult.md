# StoreAndForwardBatch.StoredPaymentCardReadResult

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A result structure that represents each payment the framework read using a Store and Forward session.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
struct StoredPaymentCardReadResult
```

## Topics

### Instance Properties
- [let generalCardData: String](./storedpaymentcardreadresult/generalcarddata.md)
  A Base64-encoded string that contains general cardholder and terminal data in tag-length-value (TLV) format.
- [let id: String](./storedpaymentcardreadresult/id.md)
  The unique identifier for the payment.
- [let paymentCardData: String](./storedpaymentcardreadresult/paymentcarddata.md)
  A Base64-encoded string that contains the encrypted payment information to send to your payment provider.
- [let signature: String](./storedpaymentcardreadresult/signature.md)
  The signature, as a Base64-encoded string, that guarantees the integrity of the payment

## Relationships

### Conforms To
- [Encodable](../../Swift/encodable.md)
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/storeandforwardbatch/storedpaymentcardreadresult)*