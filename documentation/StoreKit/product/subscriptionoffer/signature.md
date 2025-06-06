# Product.SubscriptionOffer.Signature

**Framework**: StoreKit  
**Kind**: struct

A cryptographic signature for a promotional offer.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
struct Signature
```

#### Overview

For information about promotional offers, see [`Implementing promotional offers in your app`](implementing-promotional-offers-in-your-app.md).

The App Store Server Library provides a function that produces signatures for promotional offers. For more information, see [`Simplifying your implementation by using the App Store Server Library`](https://developer.apple.com/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library).

## Topics

### Creating subscription offer signatures
- [init(keyID: String, nonce: UUID, timestamp: Int, signature: Data)](product/subscriptionoffer/signature/init(keyid:nonce:timestamp:signature:).md)
  Creates a subscription offer signature instance.
### Getting signature elements
- [var keyID: String](product/subscriptionoffer/signature/keyid.md)
  A string that identifies the private key you use to generate the cryptographic signature.
- [var nonce: UUID](product/subscriptionoffer/signature/nonce.md)
  A one-time UUID your server generates for the promotional offer.
- [var signature: Data](product/subscriptionoffer/signature/signature.md)
  A cryptographic signature your server generates to sign a promotional offer for an auto-renewable subscription.
- [var timestamp: Int](product/subscriptionoffer/signature/timestamp.md)
  A timestamp your server generates in UNIX time format, in milliseconds, that indicates the time the server generated the signature.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionoffer/signature)*