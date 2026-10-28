# nonce

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A universally unique ID (UUID) value that you define.

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
var nonce: UUID { get }
```

```objc
@property (nonatomic, copy, readonly) NSUUID * nonce;
```

## Discussion

Your server generates a unique [`nonce`](./nonce.md) when it creates the [`signature`](./signature.md) string for the payment discount. The string representation of the [`nonce`](./nonce.md) must be lowercase.

You can use a [`nonce`](./nonce.md) one time; generate a new one for every buy request.

## See Also

### Validating the Discount
- [var signature: String](./signature.md)
  A string representing the properties of a specific promotional offer, cryptographically signed.
- [var timestamp: NSNumber](./timestamp.md)
  The date and time of the signature’s creation in milliseconds, formatted in Unix epoch time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentdiscount/nonce)*