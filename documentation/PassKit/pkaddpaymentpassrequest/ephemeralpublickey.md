# ephemeralPublicKey

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The ephemeral public key used by elliptic curve cryptography (ECC).

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var ephemeralPublicKey: Data? { get set }
```

#### Discussion

When using an ECC scheme, this property contains your ephemeral public key.

## See Also

- [var activationData: Data?](pkaddpaymentpassrequest/activationdata.md)
  The request’s activation data.
- [var encryptedPassData: Data?](pkaddpaymentpassrequest/encryptedpassdata.md)
  An encrypted JSON file containing the sensitive information needed to add a card to Apple Pay.
- [var wrappedKey: Data?](pkaddpaymentpassrequest/wrappedkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/ephemeralpublickey)*