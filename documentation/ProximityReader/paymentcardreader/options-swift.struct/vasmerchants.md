# vasMerchants

**Framework**: ProximityReader  
**Kind**: property  
**Role**: Instance Property

A global list of merchants to use when reading loyalty cards.

**Availability**:
- iOS 15.4+ - Deprecated in 18.0
- iPadOS 15.4+ - Deprecated in 18.0
- Mac Catalyst 17.0+ - Deprecated in 18.0

> **Deprecated**: Use VASRequest to specify VAS merchants

## Declaration

```swift
var vasMerchants: [VASRequest.Merchant]
```

## Discussion

When you try to read a loyalty card from your [`PaymentCardReaderSession`](../../paymentcardreadersession.md) object, specify a custom [`VASRequest`](../../vasrequest.md) object to override this list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/options-swift.struct/vasmerchants)*