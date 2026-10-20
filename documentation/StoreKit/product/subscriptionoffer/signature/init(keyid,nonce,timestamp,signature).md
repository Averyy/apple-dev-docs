# init(keyID:nonce:timestamp:signature:)

**Framework**: StoreKit  
**Kind**: init  
**Role**: Initializer

Creates a subscription offer signature instance.

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
init(keyID: String, nonce: UUID, timestamp: Int, signature: Data)
```

## Parameters

- `keyID`: A string that identifies the private key you use to generate the signature. You set up this key in App Store Connect. For more information, see [Generate keys for Apple In-App Purchases](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/generate-keys-for-in-app-purchases).
- `nonce`: A one-time UUID value that your server generates. Generate a new nonce for each signature. The string representation of the nonce you use in the signature must be lowercase.
- `timestamp`: A timestamp your server generates in UNIX time format, in milliseconds. The timestamp keeps the offer active for 24 hours.
- `signature`: The cryptographic signature your server generates to sign the promotional offer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionoffer/signature/init(keyid:nonce:timestamp:signature:))*