# wrappedKey

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+

## Declaration

```swift
var wrappedKey: Data? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSData * wrappedKey;
```

## See Also

### Accessing request data
- [var activationData: Data?](./activationdata.md)
  The request’s activation data.
- [var encryptedPassData: Data?](./encryptedpassdata.md)
  An encrypted JSON file containing the sensitive information needed to add a card to Apple Pay.
- [var ephemeralPublicKey: Data?](./ephemeralpublickey.md)
  The ephemeral public key used by elliptic curve cryptography (ECC).


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/wrappedkey)*