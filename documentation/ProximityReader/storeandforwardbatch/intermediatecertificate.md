# intermediateCertificate

**Framework**: ProximityReader  
**Kind**: property

An array that contains the intermediate certificates that the system uses to sign the leaf certificate.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
let intermediateCertificate: [String]
```

## See Also

- [let id: String](storeandforwardbatch/id-swift.property.md)
  The unique identifier for the batch.
- [let count: Int](storeandforwardbatch/count.md)
  The number of payments this batch includes.
- [let leafCertificate: String](storeandforwardbatch/leafcertificate.md)
  The leaf certificate the framework uses to sign this batch.
- [let payments: [StoreAndForwardBatch.StoredPaymentCardReadResult]](storeandforwardbatch/payments.md)
  The payments that are part of the batch.
- [let signature: String](storeandforwardbatch/signature.md)
  The signature, as a Base64-encoded string, that guarantees the integrity of the batch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/storeandforwardbatch/intermediatecertificate)*