# EncryptedTokenMetadata

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: dictionary

Encrypted data about the merchant token, including its Merchant Payment Account Number (MPAN) and expiration date.

**Availability**:
- App Store Connect API 1.0.11+
- Apple Pay Merchant Token Management API 1.0.12+

## Declaration

```swift
object EncryptedTokenMetadata
```

## Properties

- `data` (string) *(required)*: Encrypted merchant token metadata. `data` is a JSON object that contains the MPAN and expiration date. For more information about the unencrypted data, see [`TokenMetadata`](tokenmetadata.md).
- `ephemeralPublicKey` (string) *(required)*: The Base64-encoded ephemeral public key bytes. Present only when the merchant’s public key uses EC_v1.
- `publicKeyHash` (string) *(required)*: A hash of the X.509-encoded public key bytes of the merchant’s certificate.
- `signature` (string) *(required)*: A detached PKCS #7 signature, which is Base64-encoded as a string. The signature includes the signing certificate, its intermediate CA certificate, and information about the signing algorithm. For EC_v1, the signature is a valid ECDSA signature (ecdsa-with-SHA256 1.2.840.10045.4.3.2) of the concatenated values of `ephemeralPublicKey` and `data`. For RSA_v1, the signature is a valid RSA signature (RSA-with-SHA256 1.2.840.113549.1.1.11) of the concatenated values of `wrappedKey` and `data`.
- `wrappedKey` (string) *(required)*: The symmetric key, which is wrapped using your RSA public key. Present only when the merchant’s public key uses RSA_v1.

## See Also

- [Get Details of a Merchant Token Event](merchant-token-event-retrieval.md)
  Get the details of a merchant token event after receiving a notification.
- [object MerchantTokenEventResponse](merchanttokeneventresponse.md)
  A response body that contains information about a life-cycle event for a merchant token.
- [object MerchantTokenMetadata](merchanttokenmetadata.md)
  The card information related to a merchant token, including its card art and metadata.
- [object CardArt](cardart.md)
  Data for displaying art to represent a card.
- [object CardMetadata](cardmetadata.md)
  Data about the card, including its expiration date and suffix.
- [object TokenMetadata](tokenmetadata.md)
  Unencrypted metadata about a merchant token, including its Merchant Payment Account Number (MPAN) and expiration date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/encryptedtokenmetadata)*