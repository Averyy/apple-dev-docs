# Product.SubscriptionOffer.Signature

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

A cryptographic signature for a promotional offer.

**Availability**:
- iOS 17.4+ - Deprecated in 26.0
- iPadOS 17.4+ - Deprecated in 26.0
- Mac Catalyst 17.4+ - Deprecated in 26.0
- macOS 14.4+ - Deprecated in 26.0
- tvOS 17.4+ - Deprecated in 26.0
- visionOS 1.1+ - Deprecated in 26.0
- watchOS 10.4+ - Deprecated in 26.0

> **Deprecated**: Sign promotional offers with JWS and use PurchaseOption.promotionalOffer(_:compactJWS:) instead.

## Declaration

```swift
struct Signature
```

## Overview

For information about promotional offers, see [Implementing promotional offers in your app](../../implementing-promotional-offers-in-your-app.md).

The App Store Server Library provides a function that produces signatures for promotional offers. For more information, see [Simplifying your implementation by using the App Store Server Library](../../../AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library.md).

## Topics

### Creating subscription offer signatures
- [init(keyID: String, nonce: UUID, timestamp: Int, signature: Data)](./signature/init%28keyid,nonce,timestamp,signature%29.md)
  Creates a subscription offer signature instance.
### Getting signature elements
- [var keyID: String](./signature/keyid.md)
  A string that identifies the private key you use to generate the cryptographic signature.
- [var nonce: UUID](./signature/nonce.md)
  A one-time UUID your server generates for the promotional offer.
- [var signature: Data](./signature/signature.md)
  A cryptographic signature your server generates to sign a promotional offer for an auto-renewable subscription.
- [var timestamp: Int](./signature/timestamp.md)
  A timestamp your server generates in UNIX time format, in milliseconds, that indicates the time the server generated the signature.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionoffer/signature)*