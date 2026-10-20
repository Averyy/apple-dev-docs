# keyID

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A string that identifies the private key you use to generate the cryptographic signature.

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
var keyID: String
```

## See Also

### Getting signature elements
- [var nonce: UUID](./nonce.md)
  A one-time UUID your server generates for the promotional offer.
- [var signature: Data](./signature.md)
  A cryptographic signature your server generates to sign a promotional offer for an auto-renewable subscription.
- [var timestamp: Int](./timestamp.md)
  A timestamp your server generates in UNIX time format, in milliseconds, that indicates the time the server generated the signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionoffer/signature/keyid)*