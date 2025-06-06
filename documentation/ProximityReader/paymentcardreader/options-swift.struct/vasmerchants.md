# vasMerchants

**Framework**: ProximityReader  
**Kind**: property

A global list of merchants to use when reading loyalty cards.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
var vasMerchants: [VASRequest.Merchant]
```

#### Discussion

When you try to read a loyalty card from your [`PaymentCardReaderSession`](paymentcardreadersession.md) object, specify a custom [`VASRequest`](vasrequest.md) object to override this list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/options-swift.struct/vasmerchants)*