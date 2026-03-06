# MerchantTokenUsageMetadata

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: dictionary

Metadata about where and how to retrieve the latest usage information.

**Availability**:
- Apple Pay Merchant Token Management API 1.0.12+

## Declaration

```swift
object MerchantTokenUsageMetadata
```

#### Discussion

The `merchantPublicKey` includes encrypted metadata. When decrypted, you get a `data` JSON object that contains the `webServiceURL` of the merchant server, which hosts the usage information, and an opaque `authenticationToken`. The user’s devices present the `authenticationToken` when retrieving the latest usage information from the merchant server. This allows the merchant server to authenticate these requests.

## Properties

- `ciphersuite` (string) *(required)*: The cipher suite used for HPKE in authorization mode. Use the value sent as `supportedCiphersuite` in the `Retrieve MerchantToken PublicKey API` response.
- `data` (string) *(required)*: Metadata encyrpted using the merchant token public key.
- `ephemeralPublicKey` (string) *(required)*: The ephemeral public key in X9.63 representation, Base64-encoded.
- `infoHash` (string) *(required)*: A SHA-256 digest of the `info`, hex-encoded.
- `merchantPublicKey` (string) *(required)*: The `merchantPublicKey` in X9.63 representation, Base64-encoded.
- `merchantTokenPublicKeyHash` (string) *(required)*: An SHA-256 digest of the `merchantTokenPublicKey`, hex-encoded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttokenusagemetadata)*