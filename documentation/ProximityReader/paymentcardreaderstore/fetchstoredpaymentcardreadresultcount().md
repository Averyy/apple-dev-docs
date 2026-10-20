# fetchStoredPaymentCardReadResultCount()

**Framework**: ProximityReader  
**Kind**: method  
**Role**: Instance Method

Returns the number of reads the framework performed using a Store and Forward session.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
func fetchStoredPaymentCardReadResultCount() async throws -> Int
```

#### Discussion

> **Throws**: This method throws a [`PaymentCardReaderStore.StoreError`](./storeerror.md) if the count cannot be fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreaderstore/fetchstoredpaymentcardreadresultcount())*