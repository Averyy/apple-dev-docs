# fetchStoredPaymentCardReadResultCount()

**Framework**: Proximityreader  
**Kind**: method

Returns the number of reads the framework performed using a Store and Forward session.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
func fetchStoredPaymentCardReadResultCount() async throws -> Int
```

#### Discussion

> **Note**: This method throws a [`PaymentCardReaderStore.StoreError`](paymentcardreaderstore/storeerror.md) if the count cannot be fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreaderstore/fetchstoredpaymentcardreadresultcount())*