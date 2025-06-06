# nonce

**Framework**: StoreKit  
**Kind**: property

A universally unique ID (UUID) value that you define.

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
var nonce: UUID { get }
```

#### Discussion

Your server generates a unique [`nonce`](skpaymentdiscount/nonce.md) when it creates the [`signature`](skpaymentdiscount/signature.md) string for the payment discount. The string representation of the [`nonce`](skpaymentdiscount/nonce.md) must be lowercase.

You can use a [`nonce`](skpaymentdiscount/nonce.md) one time; generate a new one for every buy request.

## See Also

- [var signature: String](skpaymentdiscount/signature.md)
  A string representing the properties of a specific promotional offer, cryptographically signed.
- [var timestamp: NSNumber](skpaymentdiscount/timestamp.md)
  The date and time of the signature’s creation in milliseconds, formatted in Unix epoch time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentdiscount/nonce)*