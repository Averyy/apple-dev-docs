# activationData

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The request’s activation data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var activationData: Data? { get set }
```

#### Discussion

This property contains the data provided to the payment network as a cryptographic one-time pad (OTP), per the Payment Network API specification. The cryptographic OTP is not interpreted by Apple or iOS. The OTP should be verified by the issuer and/or payment network upon receipt of the provisioning request to ensure the request’s authenticity. For more information about the activation data’s content, contact your payment network.

> **Note**:  This is the same type of activation data that is accepted by the pass library’s [`activate(_:withActivationData:completion:)`](pkpasslibrary/activate(_:withactivationdata:completion:).md) method.

 This is the same type of activation data that is accepted by the pass library’s [`activate(_:withActivationData:completion:)`](pkpasslibrary/activate(_:withactivationdata:completion:).md) method.

## See Also

- [var encryptedPassData: Data?](pkaddpaymentpassrequest/encryptedpassdata.md)
  An encrypted JSON file containing the sensitive information needed to add a card to Apple Pay.
- [var ephemeralPublicKey: Data?](pkaddpaymentpassrequest/ephemeralpublickey.md)
  The ephemeral public key used by elliptic curve cryptography (ECC).
- [var wrappedKey: Data?](pkaddpaymentpassrequest/wrappedkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/activationdata)*