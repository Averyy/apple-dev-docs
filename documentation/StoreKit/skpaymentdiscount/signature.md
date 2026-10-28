# signature

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A string representing the properties of a specific promotional offer, cryptographically signed.

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
var signature: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * signature;
```

## Mentions

- [Implementing promotional offers in your app](../implementing-promotional-offers-in-your-app.md)

## Discussion

The [`signature`](./signature.md) is a string signed with your private key that represents the properties of a specific promotional offer. To keep your private key secure, generate the [`signature`](./signature.md) on a server.

Generate the [`signature`](./signature.md) using the Elliptic Curve Digital Signature Algorithm (ECDSA) with SHA 256. For more information, see [Generating a signature for promotional offers](../generating-a-signature-for-promotional-offers.md).

## See Also

### Validating the Discount
- [var nonce: UUID](./nonce.md)
  A universally unique ID (UUID) value that you define.
- [var timestamp: NSNumber](./timestamp.md)
  The date and time of the signature’s creation in milliseconds, formatted in Unix epoch time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentdiscount/signature)*