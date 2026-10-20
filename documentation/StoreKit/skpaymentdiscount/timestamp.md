# timestamp

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The date and time of the signature’s creation in milliseconds, formatted in Unix epoch time.

**Availability**:
- iOS 12.2+ - Deprecated in 18.0
- iPadOS 12.2+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14.4+ - Deprecated in 15.0
- tvOS 12.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Create a Product.PurchaseOption.promotionalOffer to use in Product.purchase(confirmIn:options:).

## Declaration

```swift
@NSCopying
var timestamp: NSNumber { get }
```

```objc
@property (nonatomic, copy, readonly) NSNumber * timestamp;
```

#### Discussion

The [`timestamp`](./timestamp.md) keeps the payment discount active for 24 hours.

## See Also

### Validating the Discount
- [var nonce: UUID](./nonce.md)
  A universally unique ID (UUID) value that you define.
- [var signature: String](./signature.md)
  A string representing the properties of a specific promotional offer, cryptographically signed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentdiscount/timestamp)*