# timestamp

**Framework**: StoreKit  
**Kind**: property

A timestamp your server generates in UNIX time format, in milliseconds, that indicates the time the server generated the signature.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
var timestamp: Int
```

## See Also

- [var keyID: String](product/subscriptionoffer/signature/keyid.md)
  A string that identifies the private key you use to generate the cryptographic signature.
- [var nonce: UUID](product/subscriptionoffer/signature/nonce.md)
  A one-time UUID your server generates for the promotional offer.
- [var signature: Data](product/subscriptionoffer/signature/signature.md)
  A cryptographic signature your server generates to sign a promotional offer for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionoffer/signature/timestamp)*