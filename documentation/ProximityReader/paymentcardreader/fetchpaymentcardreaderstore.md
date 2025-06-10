# fetchPaymentCardReaderStore()

**Framework**: ProximityReader  
**Kind**: method

Returns a store containing the read results the framework obtained using a Store and Forward session.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
func fetchPaymentCardReaderStore() throws -> PaymentCardReaderStore
```

#### Return Value

[`PaymentCardReaderStore`](paymentcardreaderstore.md) when successful.

#### Discussion

> **Note**: [`PaymentCardReaderError`](paymentcardreadererror.md) if the method fails to retrieve the store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/fetchpaymentcardreaderstore())*