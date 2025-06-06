# encryptedPassData

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

An encrypted JSON file containing the sensitive information needed to add a card to Apple Pay.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var encryptedPassData: Data? { get set }
```

#### Discussion

The JSON file must contain the following keys:

| Key | Type | Description |
| --- | --- | --- |
| primaryAccountNumber | String | The full primary account number (PAN). Digits only. |
| expiration | String | The expiration date as a string. For example, `"11/18"`. |
| name | String | The name of the card holder. |
| nonce | String | The hex string for the nonce value, provided in the delegate callback. |
| nonceSignature | String | The hex string for the nonce signature, provided in the delegate callback. |

## See Also

- [var activationData: Data?](pkaddpaymentpassrequest/activationdata.md)
  The request’s activation data.
- [var ephemeralPublicKey: Data?](pkaddpaymentpassrequest/ephemeralpublickey.md)
  The ephemeral public key used by elliptic curve cryptography (ECC).
- [var wrappedKey: Data?](pkaddpaymentpassrequest/wrappedkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/encryptedpassdata)*