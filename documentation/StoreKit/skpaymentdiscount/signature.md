# signature

**Framework**: StoreKit  
**Kind**: property

A string representing the properties of a specific promotional offer, cryptographically signed.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var signature: String { get }
```

## Mentions

- [Implementing promotional offers in your app](implementing-promotional-offers-in-your-app.md)

#### Discussion

The [`signature`](skpaymentdiscount/signature.md) is a string signed with your private key that represents the properties of a specific promotional offer. To keep your private key secure, generate the [`signature`](skpaymentdiscount/signature.md) on a server.

Generate the [`signature`](skpaymentdiscount/signature.md) using the Elliptic Curve Digital Signature Algorithm (ECDSA) with SHA 256. For more information, see [`Generating a signature for promotional offers`](generating-a-signature-for-promotional-offers.md).

## See Also

- [var nonce: UUID](skpaymentdiscount/nonce.md)
  A universally unique ID (UUID) value that you define.
- [var timestamp: NSNumber](skpaymentdiscount/timestamp.md)
  The date and time of the signature’s creation in milliseconds, formatted in Unix epoch time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentdiscount/signature)*